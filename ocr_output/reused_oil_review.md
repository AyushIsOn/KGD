# Report TC-1377926000007243F — the kadhai oil. A close review.

Of the eight certificates in `Document 2.pdf`, this is the one that matters most to the
underlying case and the one least able to bear weight. It is the sample taken **from the
frying vessel in which the children's food was actually cooked**, on the day 49 of them
were hospitalised — and it is the only report in the set that reaches **no conclusion at
all**.

Read [`case_context.md`](case_context.md) first for the outbreak, the FIR and the parties.

## Verified verbatim from the certificate

Read directly off the scan at 180 dpi, not inferred from OCR:

> Certified that I, **Mamta Mishra**, duly appointed as Food Analyst under the provision of
> Food Safety And Standards Act, 2006 (34 of 2006) for U.P. received from Food Safety
> Officer, **Lalitpur** sample of **खाद्य तेल (रिफाइण्ड सोयाबीन आयल कढ़ाई से)** bearing code
> Number and serial Number **FSDA/UP/SURV/86430/2026-27** of Designated Officer of
> **Lalitpur** on **18/07/2026** for analysis.
>
> The condition of the seals on the container and the outer covering on receipt was as
> follows: **Intact and Unbroken.**
>
> I found the sample to be **Reused oil** falling under Regulation No. **\*\*\*** of Food
> Safety and Standards (Food Products Standards and Food Additives) Regulation 2011.

The Hindi parenthetical translates as *edible oil (refined soyabean oil, **from the
kadhai**)*. The Rule 2.4.1(3) sampling notice independently describes the article as
**रिफाइन्ड सोयाबीन ऑयल … कढ़ाई से**. The chain of identity is therefore sound: this is the
working frying oil, lifted at the school on 16/07/2026, from M/s Shalu Associates.

- Physical appearance: *"Oily liquid sample is in ordinary plastic bottle **having
  suspended particle**."*
- Analysed 18/07/2026 to 25/07/2026; signed **25/07/2026**; sample destroyed after
  certification.
- Opinion, in full: *"**On the basis of tests performed, analytical data are as above.**"*

## Defect 1 — no standard was applied, and the report says so twelve times

The regulation field reads `***`. That alone is unusual. But the "Prescribed Standards"
column was also examined pixel by pixel across all twelve rows, and it is **not blank** —
each row contains an explicit **dash**:

| Row | Parameter | Result | Prescribed standard |
|---|---|---|---|
| 1 | Butyrorefractometer @ 40 °C | 63.2 | – |
| 2 | Refractive index @ 40 °C | 1.46798 | – |
| 3 | Saponification value | **212.2** | – |
| 4 | Iodine value | 122.21 | – |
| 5 | Acid value | 0.68 | – |
| 6 | Test for synthetic colour | Negative | – |
| 7 | Unsaponifiable matter | **1.74%** | – |
| 8 | **Test for mineral oil** | **–** | – |
| 9 | Test for rancidity / Peroxide value | Negative / 5.18 Meq/kg | – |
| 10 | **Test for Vitamin A** | **–** | – |
| 11 | Test for presence of sesame oil | Negative | – |
| 12 | Moisture | 0.58% | – |

So this is not an oversight. The laboratory **affirmatively recorded that no prescribed
standard applies to any parameter measured**, and then measured twelve of them anyway.

The consequence is structural. "Substandard" under **section 3(1)(zx)** of the FSS Act
means food that fails to meet *specified* standards without being unsafe. Where the
certificate declares that no standard is specified, there is nothing for a substandard
finding to attach to. Yet the Hindi covering summary at page 12 of `Document 2.pdf`
records this sample's result as **Substandard**.

**That verdict has no author.** The Food Analyst declined to reach it; it appears only in
the Designated Officer's summary table. An adverse finding that the analyst's own
certificate does not support is the first thing a competent defence will attack.

## Defect 2 — the report contains no opinion

Form VIIA is the *Report of the Food Analyst*, and the analyst's **opinion** is its
operative part. Compare the four reports in this same batch that do their job:

| Report | Opinion |
|---|---|
| 7236F (sealed oil) | Does not conform; saponification and acid value exceed limits; **substandard** |
| 7241F (dahi) | Does not conform to Reg. 2.1.13; milk fat below 4.5%; substandard **under s.3(1)(zx)** |
| 7238F (dahi) | Same, with statutory citation |
| 7237F (besan) | Admixture of wheat and pea starches; substandard |
| **7243F (kadhai oil)** | **"analytical data are as above"** |

"Analytical data are as above" is a data transmittal, not an opinion. On the sample most
directly connected to the alleged offence, the expert declined to opine — and the sample
was then destroyed.

## Defect 3 — two tests were listed, cited, and left unreported

Rows 8 and 10 name a method but report no result. Both cells were checked by ink density
against the populated cells on the same page: roughly 75–80 dark pixels versus 600–1,900
for every cell containing text — gridlines only. Then confirmed visually.

| Row | Test | Method cited | Result |
|---|---|---|---|
| 8 | Test for mineral oil | FSSAI Manual 2021 / FSSAI 02.029.2021 | **–** |
| 10 | Test for Vitamin A | FSSAI 02.040.2021 | **–** |

The comparison that makes this hard to explain: **the sealed-oil sample from the same
premises, analysed by the same analyst in the same week, reports both** — mineral oil
*Negative*, Vitamin A *Positive*.

Why each omission bites:

- **Mineral oil is not a quality test, it is an adulteration test.** Mineral oil in edible
  oil is prohibited; its presence would push the article from *substandard* toward
  *unsafe*, which is the territory BNS 274/275 occupies. Leaving it unreported on the oil
  taken from the cooking vessel removes the one screen in the panel that could have
  supported the criminal charge.
- **Vitamin A would have measured thermal abuse independently.** Fortificant vitamin A
  degrades rapidly on repeated heating. The sealed oil tested Positive. Had the kadhai oil
  been tested and come back negative or weak, that would have been direct, cheap evidence
  of how hard the oil had been worked. The comparison was available and was not made.

## Defect 4 — the one legally operative test for used oil was never run

Used frying oil has no compositional standard, which is presumably why the regulation
field reads `***`. But it does have **one** enforceable limit. Under the 2017 amendment to
Regulation 2.2.1, **Total Polar Compounds (TPC) must not exceed 25%**, beyond which the
oil [is not suitable for use](https://fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Quality_Vegetable_Oil_03_11_2017.pdf)
and, per FSSAI's own framing, is [considered unsafe for human consumption](https://fssai.gov.in/upload/media/FSSAI_NEws_Oil_FNB_23_07_2019.pdf).
FSSAI's RUCO programme is built on that threshold.

**TPC was not measured.** Instead the laboratory ran the refined-soyabean-oil panel —
against a product this sample, by the analyst's own finding, was not.

This is the crux of the whole review. There *was* an applicable standard. It is the only
standard under which "reused oil" means anything in law. It would have produced a clean
binary answer on the sample that came out of the frying pan on the day the children fell
ill. It was omitted, and the sample was then destroyed, so it cannot now be obtained.

## What the numbers do show

Taken as chemistry rather than as compliance, the results are coherent and they do
describe a degraded oil. Read against the sealed oil from the same premises:

| Parameter | Sealed oil (7236F) | Kadhai oil (7243F) | Refined soyabean norm | Direction |
|---|---|---|---|---|
| Saponification value | 196.8 | **212.2** | 189–195 | sharply up |
| Unsaponifiable matter | 0.71% | **1.74%** | ≤ 1.5% | up, over limit |
| Moisture | 0.04% | **0.58%** | ≤ 0.1% | ~15× up |
| Refractive index @ 40 °C | 1.46717 | 1.46798 | 1.4649–1.4710 | up, in range |
| Butyro reading @ 40 °C | 62.0 | 63.2 | 58.5–68.0 | up, in range |
| Iodine value | 123.7 | 122.21 | 120–141 | down slightly |
| **Acid value** | **0.91** | **0.68** | ≤ 0.6 | **down** |
| Peroxide value | 3.9 | 5.18 | ≤ 10 | up, in range |

Rising saponification value means falling mean fatty-acid molecular weight — chain
scission from prolonged heating. Rising unsaponifiable matter reflects accumulation of
polymerised, non-saponifiable degradation products. Rising refractive index tracks
polymerisation. Falling iodine value tracks loss of unsaturation. Moisture at ~15× the
refined-oil limit is what wet food dropped into hot oil produces, and it accelerates
hydrolysis. Suspended particulate is carbonised food debris. Every one of these vectors
points the same way: **this oil had been used hard.**

### Two traps in this table

**The peroxide value proves nothing, and it looks reassuring.** 5.18 Meq/kg against a
limit of 10 reads like a pass. It is not evidence of good oil. Hydroperoxides are
thermally labile and decompose above frying temperature into secondary carbonyls —
aldehydes and ketones — so a heavily used frying oil characteristically returns a *low*
peroxide value. Peroxide value is a meaningful index for stored oil, not for oil taken hot
out of a kadhai. Anyone reading this certificate without that caveat will draw the wrong
inference, and the certificate offers no caveat.

**The acid value moves the wrong way, and that is the most interesting number here.**
Free fatty acids accumulate on frying, so the used oil should have the *higher* acid
value. It has the lower one: **0.68 in the kadhai versus 0.91 in the sealed tin.** Only a
few things explain that, and each is worth pursuing:

1. The kadhai oil had been **topped up with fresh oil** shortly before sampling — routine
   practice, and it dilutes exactly the markers being measured.
2. The two samples were **not the same base oil** — different tin, different consignment,
   different supplier.
3. The **sealed oil was already substantially degraded before it was ever heated.**

Option 3 deserves emphasis, because the sealed-oil report (7236F) failed on saponification
value at **196.8 against a ceiling of 195** — and **degradation cannot explain that
figure in an unopened tin.** Saponification value is a compositional property. In oil that
has never been fried, an out-of-range saponification value points not to abuse but to the
oil **not being what it is sold as** — poor refining, or blending with a cheaper oil of
different fatty-acid chain length. Combined with an acid value 52% over limit in sealed
stock, the more troubling inference is about the **oil being supplied to the school in the
first place**, independent of how it was later used.

The 7236F certificate attributes its failure to those two parameters and stops. It does
not ask why a sealed tin of refined soyabean oil is off-specification on a compositional
index. Nobody appears to have followed the oil back to its supplier.

## Why the oil is probably not the answer anyway

It should be said plainly: **this oil almost certainly did not cause the outbreak.**

Degraded frying oil is a chronic-exposure hazard. It does not produce ~49 children
vomiting within hours of a single meal. That presentation — rapid onset, vomiting
predominant, large simultaneous cluster, full recovery within days — is the signature of a
**preformed bacterial toxin** (*Staphylococcus aureus*, *Bacillus cereus* emetic toxin) or
of **waterborne contamination**.

And that is where the whole evidentiary set fails, not just this report: **there is no
microbiological testing anywhere in the eight certificates.** No plate counts, no
coliforms, no *E. coli*, *Salmonella*, *S. aureus* or *B. cereus*, no water sample. The
dahi — dairy, drawn from a 10 kg bucket, held at ambient temperature in July, the single
highest-risk item in the batch — was tested for fat, solids-not-fat, adulterants, heavy
metals and pesticides. Not for one organism.

Two independent pointers were also left unfollowed. The FIR pleads **BNS 271, negligent
act likely to spread infection** — an infection theory with no microbiology behind it. And
the contractor's own remedial step was to **install an RO unit**, which means the
contractor's working hypothesis was the water. No water was analysed.

## Where this leaves the kadhai oil report

Summarising bluntly:

| Question | Answer from 7243F |
|---|---|
| Was the oil degraded? | Yes — saponification, unsaponifiable matter, moisture and particulate all say so |
| Was it *legally* unfit? | **Unknown.** TPC, the only applicable limit, was not measured |
| Was it adulterated? | **Unknown.** The mineral oil result was not reported |
| Is it substandard? | Not per the analyst — no standard was cited, no opinion given |
| Does it support BNS 274/275? | **No.** Neither adulteration nor noxiousness is established |
| Can any of this be fixed? | **No.** Sample destroyed after certification |

The report is not wrong. Every number in it is plausible and internally consistent. It is
**unusable**, which is a different and worse problem: it measures a used frying oil against
the specification of a product it is not, omits the one test that governs used frying oil,
withholds two results it cites methods for, and expressly declines to conclude — after
which the material was destroyed and an adverse verdict was recorded elsewhere by someone
who did no testing.

## Questions worth putting to the file

1. **Was TPC tested and not reported, or never tested?** The laboratory's scope and
   worksheets for 18–25 July would settle it.
2. **Why are the mineral oil and Vitamin A cells dashed** when both were reported for the
   sealed-oil sample days earlier?
3. **On what basis did the Designated Officer record "Substandard"** for a sample whose
   certificate cites no standard and offers no opinion?
4. **Do counterpart parts of the sample survive with the Designated Officer?** The
   certificate records destruction of the laboratory's portion. If counterparts exist, TPC
   may still be recoverable; if not, that avenue is closed and the FBO's re-analysis right
   is affected.
5. **Was the kadhai oil topped up with fresh oil before sampling,** and was that recorded?
   It would explain the acid-value inversion and would materially change interpretation.
6. **Where did the sealed refined soyabean oil come from?** A sealed tin failing on
   saponification value is a supplier-side authenticity question that no report addresses.
7. **Why was no microbiological sample taken** in a vomiting outbreak of this size, and
   was any water sample lifted?
8. **Does M/s Shalu Associates hold a licence covering the Lalitpur premises** where the
   food was cooked? The notices record licence 12726014000034 and an **Ayodhya** business
   address, roughly 500 km from the school. Whether the licence extends to the school
   kitchen is a separate compliance question from anything in the lab reports.
9. **Reconcile the Jay Ambey Foods person-in-charge** named on licence 12719013000109
   against the manager named in the FIR.
10. **Report 7239F (rice)** records analysis beginning 17/07 but receipt on 18/07. Clerical,
    but it should be corrected on the record before the exhibit is relied on.

---

*This is a documentary and technical review of scanned records, produced with OCR
assistance; figures should be confirmed against the originals before use. It is not legal
advice. Source citations: [FSSAI 2017 gazette notification on vegetable oil quality](https://fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Quality_Vegetable_Oil_03_11_2017.pdf),
[FSSAI note on TPC and used oil](https://fssai.gov.in/upload/media/FSSAI_NEws_Oil_FNB_23_07_2019.pdf),
[FSSAI RUCO](https://westregion.fssai.gov.in/RUCO.php). Content from these sources was
rephrased for compliance with licensing restrictions.*
