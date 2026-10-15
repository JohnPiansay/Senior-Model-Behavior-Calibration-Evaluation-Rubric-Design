# Model Behavior Calibration Workbench

A compact workbench for independent human ratings on the six supplied synthetic cases. These are illustrative cases, not real benchmark outputs.

## Files
- `RATER-GUIDE.md`: rating and run-record instructions.
- `rubric.yaml`: proposed six-dimension rubric and anchors.
- `cases.json`: supplied synthetic cases.
- `human-ratings-template.csv`: blank rating form.
- `disputed-grade-queue.csv`: blank dispute log.
- `run_calibration.py`: standard-library summary utility.
- `human-ratings-case-01.csv`: partial, user-reported ratings for CASE-01.
- `run-record.md`: status, limitations, and next steps.

## Current status
Only CASE-01 has ratings entered. The user reports both entries were human-scored, with AI used only to polish wording. Rating timestamps were not provided. Rater 2's independence from Rater 1's scores has not been confirmed. The two entries therefore remain provisional and are not yet evidence of independent inter-rater agreement. D3 is IE because no governing safety policy was supplied. Complete CASE-02 through CASE-06 independently, record actual timestamps, and confirm blind scoring before running the summary utility.

The supplied case set is synthetic. Do not present this exercise as real-world benchmark validation or claim generalizable reliability.
