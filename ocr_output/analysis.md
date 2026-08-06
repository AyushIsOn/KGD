# Document 2.pdf — Document Analysis

## What the file is

A 12-page scanned PDF containing **eight statutory food-analysis certificates** plus a
**one-page covering summary**, issued by the Government Public Analyst Laboratory,
Sector-C Aliganj, Lucknow-226024 (Food Safety and Drug Administration, Uttar Pradesh).

Every certificate is a **Form VIIA — "Report of the Food Analyst"** (see rule 2.4.2(5)
& 2.4.4(6)) issued under the Food Safety and Standards Act, 2006 (34 of 2006). All
samples were lifted in **District Lalitpur**, received by the lab on **17–18 July 2026**,
and reported between **24 and 29 July 2026**.

| Property | Value |
|---|---|
| Pages | 12 (pages 1–11 portrait A4, page 12 landscape) |
| PDF version | 1.3 |
| Producer | Haru Free PDF Library 2.4.5 |
| Embedded text layer | **None** — 0 text characters on every page |
| Page content | Exactly one full-page raster image per page |
| Lab file reference | FDA/LAB/LKO/QSF/26/01 |
| NABL / TC code | TC-13779 |

Because there is no text layer, the file is a pure scan and OCR was mandatory. See
[`ocr_method.md`](ocr_method.md) for the pipeline and [`full_text.md`](full_text.md) for
the page-by-page transcription.

## Page map

| Pages | Report No. | Sample | Signed by |
|---|---|---|---|
| 1 | TC-1377926000007236F | Refined Soyabean Oil | Mamta Mishra |
| 2 | TC-1377926000007243F | Reused / cooking oil from kadhai | Mamta Mishra |
| 3 | TC-1377926000007242F | Prepared Roti (wheat) | Rajnee Yadav |
| 4 | TC-1377926000007240F | Prepared Kadhi (besan) | Rajnee Yadav |
| 5 | TC-1377926000007239F | Prepared Rice | Rajnee Yadav |
| 6–7 | TC-1377926000007241F | Dahi | Manju Pandey |
| 8–9 | TC-1377926000007238F | Dahi, Samooh brand | Manju Pandey |
| 10–11 | TC-1377926000007237F | Besan, Tulsi Gold brand | (Govt. Public Analyst Lab) |
| 12 | — | Hindi covering summary of all 8 samples | — |

## Outcome: 5 substandard, 3 pass

Verdicts below are taken from the covering table on page 12 and cross-checked against
each report's own Opinion paragraph.

| # | Code slip no. | Sample (Hindi as printed) | Verdict | Reason given |
|---|---|---|---|---|
| 1 | FSDA/UP/940232/2026-27 | रिफाइण्ड सोयाबीन तेल | **Substandard** | Saponification value and Acid value both above limit |
| 2 | FSDA/UP/SURV/86430/2026-27 | खाद्य तेल रिफाइण्ड सोयाबीन आयल कढ़ाई | **Substandard** | Report states data only; DO recorded substandard |
| 3 | FSDA/UP/SURV/86429/2026-27 | रोटी गेंहू से निर्मित | Pass | No adulterant detected |
| 4 | FSDA/UP/SURV/86427/2026-27 | कढी पकी हुई बेसन से निर्मित | Pass | No adulterant detected |
| 5 | FSDA/UP/SURV/86426/2026-27 | चावल पका हुआ | Pass | No adulterant detected |
| 6 | FSDA/UP/SURV/86428/2026-27 | दही | **Substandard** | Milk fat 0.64% vs 4.5% minimum |
| 7 | FSDA/UP/940231/2026-27 | दही समूह ब्राण्ड, १० किग्रा॰ बाल्टी से नमूना संग्रह किया | **Substandard** | Milk fat 0.53% vs 4.5% minimum |
| 8 | FSDA/UP/940230/2026-27 | बेसन तुलसी गोल्ड ब्राण्ड | **Substandard** | Admixture of wheat and pea starches |

Reports 6, 7 and 8 invoke **section 3(1)(zx)** of the FSS Act 2006 (definition of
"sub-standard") explicitly.

## Key analytical findings

### Refined Soyabean Oil — page 1, two parameters out of specification
Standard: Regulation 2.2.1(16)(14), FSS (Food Products Standards and Food Additives)
Regulations 2011.

| Parameter | Result | Standard | Verdict |
|---|---|---|---|
| Saponification value | **196.8** | 189–195 | **Fail (high)** |
| Acid value | **0.91** | not more than 0.6 | **Fail (high)** |
| Butyrorefractometer @ 40 °C | 62.0 | 58.5–68.0 | Pass |
| Refractive index @ 40 °C | 1.46717 | 1.4649–1.4710 | Pass |
| Iodine value | 123.7 | 120–141 | Pass |
| Unsaponifiable matter | 0.71% | ≤ 1.5% | Pass |
| Peroxide value | 3.9 meq/kg | ≤ 10 meq/kg | Pass |
| Moisture | 0.04% | ≤ 0.1% | Pass |
| Synthetic colour / mineral oil / rancidity / sesame oil | Negative | Negative | Pass |
| Vitamin A | Positive | (fortification required) | Pass |

The elevated acid value together with the elevated saponification value is the classic
signature of a **hydrolysed / poorly refined or degraded oil**.

### Reused kadhai oil — page 2, no standard column populated
This report is filed against "Regulation No. **\*\*\***" — i.e. no specific product
standard was cited, because reused frying oil has no compositional standard of its own.
The lab therefore printed results without pass/fail comparison and the Opinion reads only
*"analytical data are as above."* The measured values are nevertheless well outside
refined soyabean oil norms:

| Parameter | Result | Refined soyabean oil norm (for reference) |
|---|---|---|
| Saponification value | **212.2** | 189–195 |
| Unsaponifiable matter | **1.74%** | ≤ 1.5% |
| Acid value | 0.68 | ≤ 0.6 |
| Moisture | 0.58% | ≤ 0.1% |
| Peroxide value | 5.18 meq/kg | ≤ 10 meq/kg |
| Butyrorefractometer @ 40 °C | 63.2 | 58.5–68.0 |
| Refractive index @ 40 °C | 1.46798 | 1.4649–1.4710 |
| Iodine value | 122.21 | 120–141 |

Physical appearance was recorded as *"oily liquid sample is in ordinary plastic bottle
**having suspended particle**"* — consistent with used frying oil. Note that FSSAI's
separate limit for used cooking oil is **Total Polar Compounds ≤ 25%**, which was not
tested here.

### Dahi — pages 6–7 and 8–9, gross milk-fat deficiency
Standard: Regulation 2.1.13.

| Parameter | Report 7241F (p.6–7) | Report 7238F (p.8–9) | Standard |
|---|---|---|---|
| Milk fat | **0.64%** | **0.53%** | ≥ 4.5% (mixed milk) |
| Solids not fat | 11.93% | 10.23% | ≥ 8.5% |
| B.R. of extracted fat @ 40 °C | Insufficient | Insufficient | 40.0–44.0 |
| Anionic detergents, sucrose, starch, neutraliser/carbonate, added urea | Negative | Negative | Negative |

Milk fat is roughly **one-eighth of the legal minimum** in both samples, while SNF is
comfortably above minimum — the pattern expected from dahi set from **skimmed or heavily
separated milk** sold as full-fat curd. There was too little fat to even run the
Butyro-refractometer test on the extracted fat.

Part-B testing (outside NABL scope) on both dahi samples returned **BLOQ** (below limit
of quantification) for all six heavy metals (Cu, As, Cd, Sn, Hg, Pb) and all twelve
pesticides screened by GC-MS.

### Besan "Tulsi Gold" — pages 10–11, adulterated with foreign starch
All Part-A chemistry passed:

| Parameter | Result | Standard |
|---|---|---|
| Moisture | 9.50% | ≤ 12.0% |
| Ash insoluble in dilute HCl | 0.15% | ≤ 0.3% |
| Alcoholic acidity (90% alcohol, as H₂SO₄) | 0.09% | ≤ 0.18% |
| Khesari dal powder (BOAA) | Negative | Negative |
| Synthetic colour | Negative | Negative |

The failure came from **Part-B microscopy** (FSSAI Manual 03:024:2023):
*"Gram starches are seen along with wheat & pea starches."* Opinion: the sample is an
**admixture of wheat and pea starches**, hence substandard. Rodent hair/excreta and
living/dead insects were **Absent**; 20 GC-MS pesticides, one LC-MS pesticide (atrazine)
and six heavy metals were all **BLOQ**.

Note that **khesari dal was negative** — the adulteration is economic (cheaper wheat and
pea flour bulking out gram flour), not the toxic lathyrism-causing kind.

### Prepared foods — pages 3, 4, 5, all pass
Roti, kadhi and rice were all filed as **Proprietary Food under Regulation 2.12.1**, so
they were screened only for adulterants rather than against a compositional standard.

| Sample | NaCl | Starch | Synthetic colour | Butyro @ 40 °C | Other |
|---|---|---|---|---|---|
| Prepared Roti (p.3) | Negative | Positive | Negative | Insufficient fat | — |
| Prepared Kadhi (p.4) | Positive | Positive | Negative | 62.2 | Boric acid test for turmeric: **Positive** |
| Prepared Rice (p.5) | Negative | Positive | Negative | Insufficient fat | — |

Positive starch in roti and rice is expected and is listed with "Positive" as the
prescribed value. All three opinions read *"no adulterant is detected."*

## Points worth a second look

1. **Page 4 (Kadhi) internal inconsistency.** Row 5 records *"Boric Acid Test for
   Turmeric — **Positive**"* with no prescribed-standard value printed, yet the Opinion
   states "no adulterant is detected" and the covering table marks the sample **Pass**.
   Boric acid is not a permitted additive in food. This may be a naming artefact (the
   turmeric-paper method is the classical *reagent* for detecting boric acid, so the row
   may be reporting detection of turmeric rather than of boric acid) but as printed the
   result and the opinion pull in opposite directions. Worth confirming against the
   original worksheet.

2. **Page 2 (reused oil) verdict originates outside the report.** The Form VIIA itself
   reaches no conclusion — Regulation No. is "\*\*\*" and the Opinion is purely
   descriptive — but page 12 records the sample as Substandard. The adverse conclusion is
   therefore the Designated Officer's, not the Food Analyst's, which matters if the
   finding is ever contested.

3. **Dahi milk-fat basis.** Both dahi reports were judged against the **4.5% mixed-milk**
   minimum. The standard row also lists 3.0% (toned), 1.3% (double toned) and ≤0.5%
   (skimmed). At 0.64% and 0.53% the samples fail every category except skimmed, so the
   verdict holds regardless — but the milk class chosen should match the label
   declaration.

4. **Dates are in 2026.** Sampling 17–18 July 2026, reporting 24–29 July 2026, and the
   ICP-MS/GC-MS SOPs carry issue date 15.11.2025. These are internally consistent.

5. **Sample numbering split.** Two prefixes are in use: `FSDA/UP/SURV/...` for the five
   survey samples (86426–86430) and `FSDA/UP/...` for the three enforcement samples
   (940230–940232). All five substandard results but one (86428, 86430) fall in the
   enforcement series.

6. **All samples destroyed after certification**, as noted on every report — so
   re-analysis of these specific samples is not possible.

## OCR confidence and known gaps

Mean per-page character confidence from the Latin pass was **0.92–0.98**. Remaining
weak spots:

- **Devanagari digits.** EasyOCR transcribes Hindi numerals correctly but the Latin pass
  renders some as `२०२6`-style hybrids. Dates and report numbers in this analysis were
  read from the Latin pass, which handles them correctly.
- **Page 6 sample number** was garbled by the Latin pass; recovered from the Devanagari
  pass as `एफ०एस०डी०ए०/यू०पी०/SURV/86428/2026-27`.
- **Rubber stamps and signatures** overlap printed text at the foot of every report,
  producing noise such as `UtanRaYkoo`, `MouxapeAsqeuptan`, `BTR`, `ARTIR`. These are
  stamp impressions of "Food Analyst, Uttar Pradesh, Lucknow", not data.
- **Page 12** is a handwritten-and-typed Hindi table; the `किस्म` (type) column and code
  slip numbers read cleanly, and the remarks column (`अभ्युक्ति`) contains handwritten
  notes that did not resolve reliably.
- Analyst name on page 3/4/5 reads as "Rajnee Yadav" / "Rajncc Yadav" across passes; the
  spelling of the given name is not fully certain from the scan.
