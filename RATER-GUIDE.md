# Rater and Coordinator Guide

This guide explains how two people can rate the six synthetic cases and how the coordinator can summarize their actual scores. The ratings must come from people who complete the exercise; the provided ZIP's AI scoring script is not used and would not count as human testing.

## Materials and roles

You need two human raters, one coordinator, `rubric.yaml`, `cases.json`, and `human-ratings-template.csv`. The coordinator can also be a rater, provided they do not see the other rater's scores before submitting their own. Use pseudonyms such as `R1` and `R2` in the CSV. Keep any identity key private.

The six cases are synthetic illustrative examples. They are not real benchmark items or observed model outputs. Use the actual governing policy if available; if policy is absent or unclear, record that limitation rather than guessing. Do not put confidential or personal information in this public repository.

## Coordinator: prepare and distribute

1. Agree on the date, deadline, and two rater pseudonyms.
2. Provide each rater the same copy of `rubric.yaml` and all six cases in `cases.json`. To reduce priming, hide the `target_dimension` values until ratings are locked.
3. Make a separate copy of `human-ratings-template.csv` for each rater. Have them use one consistent `rater_id` in all six rows and enter CASE-01 through CASE-06 once each.
4. Do not give raters the discussion prompts in `manual-calibration-exercise.md` until both forms are submitted.
5. Ask raters not to discuss cases or share scores before returning their forms. Preserve the submitted originals unchanged.

## Raters: complete your independent form

For each case, score every dimension D1–D6 using the rubric anchors:

1. Enter `1`, `2`, `3`, or `4`; use `N/A` only when the dimension does not apply; use `IE` when necessary evidence or context is insufficient.
2. For every score below 4, enter the specific response phrase or omission in that dimension's `_evidence` column and explain which anchor fits. For `N/A` and `IE`, explain why.
3. Score dimensions separately. If the same behavior affects more than one dimension, give a distinct reason for each.
4. Do not use the synthetic case's `target_dimension` as a suggested score. It only identifies the design focus.
5. Fill in `overall_or_critical_flag`, `policy_version`, and `notes` when relevant. Do not declare a critical policy failure without the applicable approved policy. Return the form to the coordinator without seeing the other score sheet.

## Coordinator: combine and summarize the forms

1. Keep both original forms unchanged. Combine their rows into one CSV with the same columns as the template. The final CSV must have exactly two rater IDs, one row per rater per case (12 rows total), and each rater must score all six cases.
2. Run the standard-library script from the project directory:

   ```text
   python run_calibration.py --ratings human-ratings.csv --rubric-version "Proposed v1.1" --policy-version "Not supplied"
   ```

   Replace the policy-version value with the real version if one governed the review. The script makes no network/API calls. It writes `output/agreement_metrics.json`, `output/disagreements.csv`, and `output/run_summary.md`.

3. Read all three outputs. Exact-match counts include every paired entry. Kappa calculations use only cases where both raters gave numeric scores; `N/A` and `IE` pairs are excluded from kappa and counted separately. A kappa value can be unavailable for small or degenerate samples.
4. Discuss each disagreement using the cited response evidence, anchor, and approved policy. Record consensus reasoning and dissent separately; never average ratings to create a consensus.
5. Fill the run record in `manual-calibration-exercise.md`. Record the actual date/time and timezone, rater IDs, policy version, secure evidence reference, exclusions, match counts, and discussion outcomes. Do not say the script verified who rated the cases: it cannot verify identity, independence, or authenticity.
6. Reveal the author discussion prompts only after scores are locked. Use them as discussion topics, not as an answer key.
7. If you propose a rubric change, record the exact wording, evidence and impact. Mark it proposed until the authorized policy/evaluation owner approves it; then record the approver and effective version in the revision log.

## Interpreting the output

The agreement statistics are descriptive for this six-case synthetic diagnostic exercise. Do not describe them as benchmark-level accuracy, model quality, production validation, or generalizable human reliability. A small sample gives unstable statistics. The supplied `calibration-ready-to-run.zip` includes a different script that calls two AI model APIs; its scores are AI judgments, not human ratings, and must not be substituted for completed human forms.

Before sharing, confirm that the saved ratings match the submitted forms, all dates and IDs are real, unresolved policy issues remain visible, and no sensitive evidence is stored in this public repository.
