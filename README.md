# KGD

OCR and analysis of the food-safety records in this repository.

`Document 2.pdf` holds eight statutory **Form VIIA "Report of the Food Analyst"**
certificates from the Government Public Analyst Laboratory, Aliganj, Lucknow (FSDA, Uttar
Pradesh), plus a Hindi covering summary. The accompanying PDFs — an **FIR**, three
**sampling notices**, a **contractor's letter** and an **FSSAI licence** — establish what
the reports belong to.

**The case:** on **16 July 2026**, around **49 of ~700 children** at Atal Awasiya
Vidyalaya, Dhaurra (District Lalitpur) were hospitalised with vomiting and abdominal pain.
**FIR 0158/2026** was registered at PS Jakhlaun the next day under **BNS 125, 271, 274 and
275**. These eight samples are the laboratory evidence.

Only the licence has a text layer; everything else is a scan, so the contents were
recovered by optical character recognition.

## Result: 5 of 8 samples substandard

| # | Sample | Verdict | Reason |
|---|---|---|---|
| 1 | Refined Soyabean Oil | Substandard | Saponification value 196.8 (limit 189–195), acid value 0.91 (limit 0.6) |
| 2 | Reused kadhai cooking oil | Substandard | Saponification 212.2, unsaponifiable matter 1.74%, moisture 0.58% |
| 3 | Prepared Roti | Pass | No adulterant detected |
| 4 | Prepared Kadhi | Pass | No adulterant detected |
| 5 | Prepared Rice | Pass | No adulterant detected |
| 6 | Dahi | Substandard | Milk fat 0.64% vs 4.5% minimum |
| 7 | Dahi, Samooh brand | Substandard | Milk fat 0.53% vs 4.5% minimum |
| 8 | Besan, Tulsi Gold brand | Substandard | Admixture of wheat and pea starches |

## Contents

| Path | What it is |
|---|---|
| [`ocr_output/case_context.md`](ocr_output/case_context.md) | **The underlying case** — outbreak, FIR 0158/2026, parties, timeline |
| [`ocr_output/defects_register.md`](ocr_output/defects_register.md) | **Every defect found across all eight reports**, graded by severity |
| [`ocr_output/reused_oil_review.md`](ocr_output/reused_oil_review.md) | **Close review of the kadhai-oil report** and its four defects |
| [`ocr_output/analysis.md`](ocr_output/analysis.md) | Document analysis, findings, and points needing a second look |
| [`ocr_output/full_text.md`](ocr_output/full_text.md) | Page-by-page reconstructed transcription |
| [`ocr_output/results_summary.csv`](ocr_output/results_summary.csv) | Machine-readable sample → verdict table |
| [`ocr_output/ocr_method.md`](ocr_output/ocr_method.md) | Pipeline, engine choice, confidence scores, limitations |
| [`ocr_output/run_ocr.py`](ocr_output/run_ocr.py) | Reproducible OCR pipeline |
| `ocr_pages/` | 180 dpi PNG render of each PDF page (git-ignored, ~37 MB; regenerate with `run_ocr.py`) |
| `ocr_text/` | Raw RapidOCR output (English), per page + JSON with coordinates |
| `ocr_text_hindi/` | Raw EasyOCR output (Hindi + English), per page |

## Reproducing the OCR

```bash
pip install pymupdf rapidocr-onnxruntime easyocr
pip uninstall -y opencv-python && pip install opencv-python-headless
python3 ocr_output/run_ocr.py
```

Two engines are used because neither suffices alone: RapidOCR is more accurate on the
printed English text and numeric results but cannot read Devanagari, while EasyOCR
(`hi`+`en`) recovers the Hindi sample names and the page-12 summary table. See
[`ocr_output/ocr_method.md`](ocr_output/ocr_method.md) for detail.

> Transcription is OCR-derived and machine-assisted. The pass/fail conclusions above are
> the laboratory's own opinions as printed, not an independent assessment. Verify against
> the original scan before relying on any figure.
