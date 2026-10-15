# Handover and Operating Notes

## Package contents

- rubric-v1.md: proposed six-dimension scoring framework, anchors, provisional weights/cutoffs, gates, and arbitration steps.
- calibration-exemplars.md: invented good/borderline/bad examples for each dimension; training illustrations only.
- manual-calibration-exercise.md: six synthetic diagnostic cases, independent rating forms, and an uncompleted run record.
- RATER-GUIDE.md: step-by-step instructions for raters and coordinator, including how to count matches and report disagreements.
- rubric.yaml and cases.json: machine-readable proposed rubric and six synthetic cases supplied by the user.
- human-ratings-template.csv: blank row template; duplicate it for each rater, then combine both forms before running the script.
- run_calibration.py: standard-library-only summarizer of two submitted human forms. It makes no model/API calls and cannot verify identity or rating independence.
- review-dossier.json: empty real-case queue schema plus one explicitly synthetic worked arbitration example.
- disputed-grade-queue.csv: header-only data-entry template for actual disputes.
- evaluation-summary.md: methodology, quality controls, findings, limitations, and team next steps.
- weekly-revision-log.md: weekly review process and blank/current-status log.

## Workflow for the receiving team

1. Supply the governing benchmark/policy, existing grading dimensions, team quality criteria, and secure evidence-retention rules.
2. Add real anonymized cases to the CSV or JSON queue; do not place secrets or personal identifiers in this public repository.
3. Have raters score independently with the approved rubric version before comparison.
4. Adjudicate dimension-level disagreements with cited evidence; record final rationale and unresolved dissent without overwriting initial scores.
5. Run weekly revision review with the evaluation lead; update rubric and exemplars only after approval and impact assessment.

## Testing environment and verification status

This repository contains one small Python utility for summarizing CSV ratings; it uses only the standard library and makes no network or model calls. The manual calibration exercise is **pending** and must be run by actual independent human raters before describing the work as human-tested. The user's ZIP also contained an AI judge version; that was not used because agreement between AI model outputs is not evidence of human calibration. Before operational use, check that JSON parses, CSV templates import, README links resolve, and the team approves the proposed scoring rules. No human inter-rater reliability, quality benchmark pass, or production performance claim is made.

## Execution and open items

No real disputed-grade queue or team feedback was provided, so the real queue remains empty and no actual grade was arbitrated. The rubric and exemplars are proposed, not team-approved. The supplied cases are synthetic. The optional external/cloud document link was not supplied. Weekly reviews are scheduled by the team; this package does not claim a completed weekly cycle. Personal work time is not measured or certified here.

## Evidence map

See evaluation-summary.md for methods and author analysis, review-dossier.json for the machine-readable dossier, rubric-v1.md for rubric definitions, calibration-exemplars.md for examples, manual-calibration-exercise.md for the pending human run, and weekly-revision-log.md for change governance.
