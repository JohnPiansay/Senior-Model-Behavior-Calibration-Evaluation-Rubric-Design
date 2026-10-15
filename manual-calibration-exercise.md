# Manual Calibration Exercise — Human Run Pending

**Status: not run.** The six cases in `cases.json` are synthetic illustrative examples supplied in the user's `calibration-ready-to-run.zip`. They are not real benchmark items or observed model outputs. No human scores, timing, discussion, or reliability result is reported in this repository.

## Purpose and limits

Use this small diagnostic set to see whether two human reviewers interpret the proposed rubric anchors similarly. It does not represent a benchmark sample, establish production reliability, or validate the proposed weights. The separate `run_calibration.py` script summarizes manually entered human ratings; it does not contact AI services or verify that ratings were entered by the named people.

## Cases

Rate every case in `cases.json` (CASE-01 through CASE-06) using `rubric.yaml`. The `target_dimension` field indicates the dimension each synthetic case was designed to probe; it is not a gold score, and raters should score all six dimensions independently. Preserve all supplied context and response text when presenting the cases. Do not show the `target_dimension` during blind scoring if you want to avoid priming raters.

## Procedure

1. A coordinator supplies both raters the same rubric and case materials, without the target-dimension hints if blind scoring is desired.
2. Each rater independently fills one copy of `human-ratings-template.csv`, using the same rater ID on all six rows. Raters do not discuss cases or share scores until both forms are submitted.
3. Raters enter 1–4, `N/A`, or `IE` per dimension. Every score below 4 and every N/A/IE entry requires an explanation in that dimension's evidence column.
4. Coordinator preserves the original forms and combines the two sets of six rows into one CSV file. Do not overwrite original ratings with consensus values.
5. Coordinator runs the summary script (instructions in `RATER-GUIDE.md`) on the combined CSV. Review exact matches, numeric agreement statistics, excluded N/A/IE pairs, and every disagreement.
6. Discuss disagreements from cited evidence and anchors. Record consensus rationale and dissent separately. If governing policy is missing or unclear, mark the item unresolved rather than guessing.
7. Complete the run record below only after the raters finish. Add any rubric change as proposed until the authorized owner approves it.

## Run record — complete after real human ratings

| Field | Record |
|---|---|
| Date and time (include timezone) | Pending |
| Rater IDs (pseudonyms) | Pending |
| Coordinator ID (pseudonym) | Pending |
| Rubric version | Proposed v1.1; confirm version used |
| Policy / benchmark version | Pending / not supplied |
| Independent forms evidence reference | Pending |
| Cases rated / excluded and reason | Pending |
| Exact-match counts by dimension | Pending; calculate from the completed forms |
| Agreement statistics and numeric-pair counts | Pending; script output is descriptive only |
| Disagreements discussed and consensus decisions | Pending |
| Unresolved questions or dissent | Pending |
| Proposed rubric changes | Pending |
| Approval, approver, effective version | Pending |

Do not substitute AI-judge outputs, synthetic worked examples, or guessed values for the human rating forms. Do not report agreement statistics from this six-case synthetic set as benchmark-level reliability.

## Author discussion prompts — reveal after independent forms are locked

The cases are intended to make these distinctions discussable, not to prescribe authoritative labels:

- CASE-01 probes whether the safety guidance and escalation language are complete enough for the context. Any D3 judgment depends on the governing policy; none was supplied with the case.
- CASE-02 contains unsupported and contradicted financial figures and an unsupported regional claim; discuss D2 separately from certainty (D5).
- CASE-03 omits the requested risk sub-question while implying completeness; discuss partial fulfillment and the misleading closing sentence.
- CASE-04 conflicts with the user's stated vegetarian constraint in prior context; discuss D1 and D4 evidence separately.
- CASE-05 presents casualty and cause claims as certain despite the supplied source stating those details are unconfirmed or unavailable; discuss D2 and D5 separately.
- CASE-06 gives a long, difficult-to-scan explanation with inline code; discuss whether usability is impaired and whether the code advice is factually grounded.
