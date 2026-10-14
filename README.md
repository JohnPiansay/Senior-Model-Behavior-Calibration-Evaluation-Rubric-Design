# Senior Model-Behavior Calibration & Evaluation Rubric Design

This repository is a starter workbench for consistent model-behavior grading: an anchored rubric, calibration exemplars, a disputed-grade record, and weekly revision controls.

## Deliverables

- [Rubric dimension set](rubric/rubric-v1.md) — proposed v1 dimensions, score anchors, weighting, and adjudication rules.
- [Calibration exemplars](rubric/calibration-exemplars.md) — illustrative good, borderline, and bad cases for each dimension.
- [Disputed-grade queue](review/disputed-grade-queue.csv) — blank evidence-first template; no actual cases were supplied for arbitration.
- [Evaluation summary and findings](reports/evaluation-summary.md) — methodology, edge cases, quality controls, and known limitations.
- [Weekly revision log](rubric/weekly-revision-log.md) — versioning and review cadence; no completed weekly cycles are claimed.
- [Handover](handover/README.md) — workflow, operating assumptions, and test/verification boundary.

## Status and evidence

This is an initial rubric proposal prepared from the task description, not a record of calibration decisions made with an evaluation team. No disputed examples, benchmark guideline, existing rubric, or team feedback were provided. The sample cases are synthetic and explicitly illustrative. Before production use, calibrate these anchors against the team's policy, benchmark definitions, and adjudicated examples.

The queue template is intentionally empty until real disputed items and their evidence are provided. No grades are represented as having been arbitrated, and no weekly rubric revisions are represented as completed.

## Suggested workflow

1. Record each disputed case with its prompt/context, response, current grades, evidence, rubric version, and exact point of disagreement. Exclude secrets and unnecessary personal data.
2. Rate independently before discussion. Cite observable response evidence and the relevant rubric anchor.
3. Resolve dimension-level disagreement first. Escalate policy ambiguity or missing evidence rather than inferring intent.
4. Document the rationale, final disposition, reviewer, date, and any rubric change. Preserve the original ratings and version for auditability.
5. Review the rubric weekly with the evaluation team; version changes only after examples, impact, and approval are recorded.

## Proposed scoring

The v1 rubric uses a 1–4 ordinal scale per dimension, with anchored behavior descriptions. A safety-critical violation is separately flagged and cannot be hidden by an average. See the rubric for proposed weights and non-applicability rules; these are starting assumptions and require team approval.
