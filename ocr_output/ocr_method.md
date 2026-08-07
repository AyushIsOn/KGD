# OCR method

## Why OCR was required

`Document 2.pdf` has **no text layer at all**. PyMuPDF reports 0 extractable characters on
every one of the 12 pages, and each page holds exactly one full-page raster image:

```
pages: 12
producer: Haru Free PDF Library 2.4.5
page 01..11: Rect(0, 0, 595.28, 841.89)  textchars=0  images=1   # A4 portrait
page 12    : Rect(0, 0, 841.89, 595.28)  textchars=0  images=1   # A4 landscape
```

So the file is a pure scan. `pdftotext`-style extraction returns nothing and real optical
recognition was unavoidable.

## Environment constraint

Tesseract is not packaged for Amazon Linux 2023 (`dnf install tesseract` →
`No match for argument: tesseract`), and neither is poppler-utils' `pdftoppm`. The
pipeline is therefore entirely Python:

| Stage | Tool | Purpose |
|---|---|---|
| Render | PyMuPDF (`fitz`) 1.26.5 | Rasterise PDF pages to PNG at 180 dpi |
| Latin OCR | `rapidocr-onnxruntime` (PP-OCR, ONNX Runtime, CPU) | English text, numerals, method codes |
| Devanagari OCR | `easyocr` with `['hi','en']` | Hindi sample names and the page-12 table |

`opencv-python` had to be swapped for `opencv-python-headless`; the full build fails at
import with `libGL.so.1: cannot open shared object file` because the sandbox has no
OpenGL libraries.

```bash
pip install pymupdf rapidocr-onnxruntime easyocr
pip uninstall -y opencv-python && pip install opencv-python-headless
```

## Two engines, deliberately

Neither engine alone is sufficient for this document:

- **RapidOCR** is markedly more accurate on the printed English body text, the FSSAI
  method identifiers (`FSSAI 02.007.2021`), and the numeric results — but its default
  recognition model has no Devanagari character set, so it silently drops or mangles every
  Hindi sample name.
- **EasyOCR** with `['hi','en']` reads the Devanagari correctly, which is what recovered
  the sample names (`रिफाइण्ड सोयाबीन तेल`, `कढी पकी हुई बेसन से निर्मित`,
  `बेसन तुलसी गोल्ड ब्राण्ड`) and the entire page-12 summary table. Its Latin output on
  this scan is noisier, and it transliterates Arabic numerals into Devanagari digits in
  mixed-script regions (`२०२6` for `2026`), so it was not used for the numbers.

The transcription in `full_text.md` takes English text and all numeric values from the
RapidOCR pass and Hindi text from the EasyOCR pass.

## Reading-order reconstruction

Both engines emit unordered bounding boxes. Boxes are sorted into human reading order by
quantising the vertical coordinate into ~18 px bands, then sorting left-to-right within
each band:

```python
rows.sort(key=lambda d: (round(d["y"] / 18), d["x"]))
```

This recovers normal prose reliably. It does **not** reliably reassemble the multi-column
result tables, because a table row's cells are often further apart vertically than the
band height. Those tables were reassembled by hand from the OCR box coordinates, so
cell-to-column assignment there is the part of `full_text.md` most worth spot-checking
against the original scan.

## Reproducing

```bash
cd /path/to/KGD
python3 ocr_output/run_ocr.py
```

## Measured confidence

RapidOCR mean per-line confidence:

| Page | Lines | Mean confidence |
|---|---|---|
| 01 | 117 | 0.950 |
| 02 | 100 | 0.954 |
| 03 | 67 | 0.942 |
| 04 | 69 | 0.947 |
| 05 | 66 | 0.940 |
| 06 | 92 | 0.939 |
| 07 | 137 | 0.975 |
| 08 | 94 | 0.935 |
| 09 | 139 | 0.978 |
| 10 | 161 | 0.967 |
| 11 | 96 | 0.959 |
| 12 | 50 | 0.922 |

Page 12 scores lowest, as expected for a mixed printed/handwritten Hindi table.

## Output layout

```
ocr_pages/                  180 dpi PNG render of each page
ocr_text/page_NN.txt        RapidOCR text, reading order
ocr_text/all_pages.json     RapidOCR boxes with coordinates + confidence
ocr_text_hindi/page_NN.txt  EasyOCR (hi+en) text, reading order
ocr_text_hindi/devanagari_lines.json   Devanagari-containing lines only
ocr_output/full_text.md     Human-readable reconstructed transcription
ocr_output/analysis.md      Document analysis and findings
ocr_output/results_summary.csv  Machine-readable sample/verdict table
ocr_output/run_ocr.py       The pipeline
```

## Known limitations

1. Result tables were reassembled with human judgement, not automatically; cell-to-column
   assignment in the wide oil tables (pages 1–2) is the likeliest place for an error.
2. Handwritten annotations, particularly in the page-12 remarks column, are not
   transcribed.
3. Rubber-stamp impressions overlap printed text at the foot of every certificate,
   producing artefacts such as `UtanRaYkoo`, `MouxapeAsqeuptan`, `ARTIR`, `BTR`. These are
   noise, not content.
4. Some `0.01` MRL values on page 10 scanned as `10'0` / `10:0` / `100`; these are flagged
   inline in `full_text.md`.
5. Nothing in this pipeline validates the reports against FSSAI standards independently —
   the pass/fail statements in `analysis.md` are the lab's own conclusions, transcribed.
