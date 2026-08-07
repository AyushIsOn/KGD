#!/usr/bin/env python3
"""
Reproducible OCR pipeline for "Document 2.pdf" (scanned, no text layer).

Stage 1  render  : PyMuPDF rasterises each PDF page to PNG at 180 dpi.
Stage 2  latin   : RapidOCR (PP-OCR / ONNX) -> high-accuracy English + numerals.
Stage 3  devanagari : EasyOCR ['hi','en'] -> Hindi sample names RapidOCR cannot read.

Install:
    pip install pymupdf rapidocr-onnxruntime opencv-python-headless easyocr

Run from the repository root:
    python3 ocr_output/run_ocr.py
"""

import glob
import json
import os
import re

PDF = "Document 2.pdf"
IMG_DIR = "ocr_pages"
LATIN_DIR = "ocr_text"
DEVA_DIR = "ocr_text_hindi"
DPI = 180
DEVANAGARI = re.compile(r"[\u0900-\u097F]")


def to_native(obj):
    """EasyOCR returns numpy int32 coords, which json cannot serialise."""
    if isinstance(obj, dict):
        return {k: to_native(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_native(v) for v in obj]
    return obj.item() if hasattr(obj, "item") else obj


def reading_order(rows, line_height=18):
    """Sort detected boxes top-to-bottom then left-to-right."""
    return sorted(rows, key=lambda d: (round(d["y"] / line_height), d["x"]))


def render():
    import fitz

    os.makedirs(IMG_DIR, exist_ok=True)
    doc = fitz.open(PDF)
    print(f"{PDF}: {doc.page_count} pages, producer={doc.metadata.get('producer')}")
    for i, page in enumerate(doc):
        chars = len(page.get_text().strip())
        pix = page.get_pixmap(dpi=DPI)
        out = f"{IMG_DIR}/page_{i + 1:02d}.png"
        pix.save(out)
        print(f"  page {i + 1:02d}: {pix.width}x{pix.height} embedded_text_chars={chars}")


def ocr_latin():
    from rapidocr_onnxruntime import RapidOCR

    engine = RapidOCR()
    os.makedirs(LATIN_DIR, exist_ok=True)
    everything = {}
    for path in sorted(glob.glob(f"{IMG_DIR}/page_*.png")):
        page = os.path.basename(path)[:-4]
        result, _ = engine(path)
        rows = [
            {
                "text": text,
                "score": round(float(score), 3),
                "y": min(p[1] for p in box),
                "x": min(p[0] for p in box),
            }
            for box, text, score in (result or [])
        ]
        rows = reading_order(rows)
        everything[page] = rows
        with open(f"{LATIN_DIR}/{page}.txt", "w") as fh:
            fh.write("\n".join(r["text"] for r in rows))
        mean = sum(r["score"] for r in rows) / len(rows) if rows else 0.0
        print(f"  {page}: {len(rows)} lines, mean confidence {mean:.3f}")
    with open(f"{LATIN_DIR}/all_pages.json", "w") as fh:
        json.dump(to_native(everything), fh, indent=1, ensure_ascii=False)


def ocr_devanagari():
    import easyocr

    reader = easyocr.Reader(["hi", "en"], gpu=False, verbose=False)
    os.makedirs(DEVA_DIR, exist_ok=True)
    hindi_only = {}
    for path in sorted(glob.glob(f"{IMG_DIR}/page_*.png")):
        page = os.path.basename(path)[:-4]
        rows = [
            {
                "text": text,
                "conf": round(float(conf), 3),
                "y": min(p[1] for p in box),
                "x": min(p[0] for p in box),
            }
            for box, text, conf in reader.readtext(path, detail=1, paragraph=False)
        ]
        rows = reading_order(rows)
        with open(f"{DEVA_DIR}/{page}.txt", "w") as fh:
            fh.write("\n".join(r["text"] for r in rows))
        hindi_only[page] = [r["text"] for r in rows if DEVANAGARI.search(r["text"])]
        print(f"  {page}: {len(rows)} lines, {len(hindi_only[page])} containing Devanagari")
    with open(f"{DEVA_DIR}/devanagari_lines.json", "w") as fh:
        json.dump(to_native(hindi_only), fh, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    print("[1/3] rendering pages")
    render()
    print("[2/3] RapidOCR latin pass")
    ocr_latin()
    print("[3/3] EasyOCR devanagari pass")
    ocr_devanagari()
    print("done")
