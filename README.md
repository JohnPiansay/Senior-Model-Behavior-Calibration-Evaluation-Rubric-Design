# Senior Model-Behavior Calibration & Evaluation Rubric Design

This repository is a starter workbench for consistent model-behavior grading: an anchored rubric, calibration exemplars, a disputed-grade record, and weekly revision controls.

## Deliverables

- [Primary review dossier (JSON)](review-dossier.json) — queue schema plus a clearly synthetic arbitration walkthrough; real queue remains empty pending actual disputes.
- [Disputed-grade queue (CSV)](disputed-grade-queue.csv) — header-only template for real cases.
- [Proposed rubric dimensions](rubric-v1.md) — six dimensions, 1–4 anchors, provisional weights/cutoffs, safety gate, and adjudication process.
- [Calibration exemplars](calibration-exemplars.md) — illustrative good, borderline, and bad examples for each dimension.
- [Manual calibration exercise](manual-calibration-exercise.md) — six synthetic cases, independent rating form, and run record. Human run is pending; this is not evidence of completed testing.
- [Rater and coordinator guide](RATER-GUIDE.md) — step-by-step instructions for independent scoring, comparison, and entering real run results.
- [Human rating template (CSV)](human-ratings-template.csv), [machine-readable rubric](rubric.yaml), and [synthetic case set](cases.json) — companion inputs for the manual exercise.
- [Calibration summary script](run_calibration.py) — summarizes two manually entered human rating forms; uses only Python's standard library and makes no model/API calls.
- [Evaluation summary and findings](evaluation-summary.md) — methodology, edge cases, quality controls, status, and limitations.
- [Weekly revision log](weekly-revision-log.md) — revision cadence and change record; no completed weekly cycle claimed.
- [Handover notes](HANDOVER.md) — package guide, workflow, validation boundary, and outstanding team inputs.

## Status and evidence

This is a proposed rubric-design package, not a record of decisions made with an evaluation team. The user supplied a complete synthetic case set; no real disputed cases, existing rubric, benchmark-specific quality guidelines, governing policy, or team feedback were supplied. The examples and calibration cases are synthetic and labeled as such. The manual exercise has not been run by human raters. Before resubmission as empirically tested work, complete its run record using genuine independent ratings; before production use, align dimensions and anchors with the team's policy and validate them against representative cases.

The queue template is intentionally empty until real, anonymized disputes and their evidence are supplied. No actual grades are represented as arbitrated, no inter-rater reliability is claimed, and no weekly revisions are represented as completed.

## Suggested workflow

1. Record anonymized context, benchmark criterion, original grades, evidence, rubric version, and precise disagreement.
2. Rate independently before comparing scores; cite observable evidence for each rating.
3. Resolve dimension-level disagreement; escalate missing evidence or policy ambiguity rather than guessing.
4. Preserve initial ratings and record final rationale, disposition, reviewer/date, and any dissent.
5. Review one dimension weekly with the evaluation team; publish changes only with examples, impact assessment, and approval.

The proposed weights, score bands, and critical-failure gate are provisional assumptions requiring team approval. The AI-judge script in the supplied ZIP is not included as evidence: AI model agreement is not human calibration. See the rater guide for how to run the human process. Do not present this package as containing completed human testing, real adjudication, or approved policy decisions.
