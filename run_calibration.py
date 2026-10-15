#!/usr/bin/env python3
"""Summarize two manually completed human rating forms; makes no model/API calls."""
import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASE_FILE = ROOT / "cases.json"
TEMPLATE = ROOT / "human-ratings-template.csv"
DIMENSIONS = [f"D{i}" for i in range(1, 7)]
VALID = {"1", "2", "3", "4", "N/A", "IE"}
NUMERIC = {"1", "2", "3", "4"}


def read_cases():
    cases = json.loads(CASE_FILE.read_text(encoding="utf-8"))
    ids = [case.get("id") for case in cases]
    if not ids or len(ids) != len(set(ids)) or any(not x for x in ids):
        raise ValueError("cases.json must contain unique, non-empty case IDs")
    return cases


def read_ratings(path, case_ids):
    ratings = {}
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        required = {"rater_id", "case_id", *DIMENSIONS,
                    *(f"{d}_evidence" for d in DIMENSIONS)}
        absent = required - set(reader.fieldnames or [])
        if absent:
            raise ValueError(f"ratings CSV missing columns: {', '.join(sorted(absent))}")
        for line, row in enumerate(reader, start=2):
            rid, cid = (row.get("rater_id") or "").strip(), (row.get("case_id") or "").strip()
            if not rid or not cid:
                raise ValueError(f"line {line}: rater_id and case_id are required")
            if cid not in case_ids:
                raise ValueError(f"line {line}: unknown case_id {cid!r}")
            key = (rid, cid)
            if key in ratings:
                raise ValueError(f"line {line}: duplicate rating for {rid}/{cid}")
            entry = {"rater_id": rid, "case_id": cid}
            for dim in DIMENSIONS:
                score = (row.get(dim) or "").strip().upper()
                evidence = (row.get(f"{dim}_evidence") or "").strip()
                if score not in VALID:
                    raise ValueError(f"line {line}: {dim} must be 1-4, N/A, or IE; got {score!r}")
                if score != "4" and not evidence:
                    raise ValueError(f"line {line}: add evidence/rationale for {dim}={score}")
                entry[dim] = score
                entry[f"{dim}_evidence"] = evidence
            ratings[key] = entry

    raters = sorted({rid for rid, _ in ratings})
    if len(raters) != 2:
        raise ValueError(f"expected exactly two rater IDs; found {len(raters)}: {raters}")
    expected = {(rid, cid) for rid in raters for cid in case_ids}
    missing = expected - set(ratings)
    if missing:
        pretty = ", ".join(f"{r}/{c}" for r, c in sorted(missing))
        raise ValueError(f"every rater must score every case; missing: {pretty}")
    return raters, ratings


def cohen_kappa(a, b, quadratic=False):
    """Cohen's kappa; N/A and IE are excluded by caller."""
    n = len(a)
    if n < 2:
        return None
    labels = [1, 2, 3, 4]
    marginal_a = Counter(a)
    marginal_b = Counter(b)
    observed_disagreement = 0.0
    expected_disagreement = 0.0
    for i in labels:
        for j in labels:
            weight = ((i - j) ** 2 / 9.0) if quadratic else float(i != j)
            observed_disagreement += weight * sum(x == i and y == j for x, y in zip(a, b)) / n
            expected_disagreement += weight * marginal_a[i] * marginal_b[j] / (n * n)
    if expected_disagreement == 0:
        return None
    return 1.0 - observed_disagreement / expected_disagreement


def summarize(raters, ratings, cases):
    r1, r2 = raters
    per_dim, disagreements = {}, []
    for case in cases:
        cid = case["id"]
        left, right = ratings[(r1, cid)], ratings[(r2, cid)]
        for dim in DIMENSIONS:
            a, b = left[dim], right[dim]
            if a != b:
                disagreements.append({
                    "case_id": cid, "dimension": dim,
                    "rater_1": r1, "score_1": a, "evidence_1": left[f"{dim}_evidence"],
                    "rater_2": r2, "score_2": b, "evidence_2": right[f"{dim}_evidence"],
                })

    for dim in DIMENSIONS:
        pairs = [(ratings[(r1, c["id"])][dim], ratings[(r2, c["id"])][dim]) for c in cases]
        numeric = [(int(a), int(b)) for a, b in pairs if a in NUMERIC and b in NUMERIC]
        per_dim[dim] = {
            "exact_matches": sum(a == b for a, b in pairs),
            "all_paired_cases": len(pairs),
            "numeric_pairs_for_kappa": len(numeric),
            "na_or_ie_pairs_excluded_from_kappa": len(pairs) - len(numeric),
            "cohen_kappa_unweighted": cohen_kappa([a for a, _ in numeric], [b for _, b in numeric]),
            "cohen_kappa_quadratic_weighted": cohen_kappa([a for a, _ in numeric], [b for _, b in numeric], True),
        }
    return {"raters": raters, "case_count": len(cases), "per_dimension": per_dim,
            "disagreement_count": len(disagreements), "disagreements": disagreements}


def write_outputs(result, args, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "agreement_metrics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    fields = ["case_id", "dimension", "rater_1", "score_1", "evidence_1", "rater_2", "score_2", "evidence_2"]
    with (output_dir / "disagreements.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(result["disagreements"])

    def show(x):
        return "not estimable" if x is None else f"{x:.3f}"

    lines = [
        "# Human Calibration Run Summary", "",
        f"- **Run date/time (UTC):** {datetime.now(timezone.utc).isoformat(timespec='minutes')}",
        "- **Source:** manually entered ratings; this script makes no model/API calls.",
        f"- **Raters (self-reported IDs):** {result['raters'][0]}, {result['raters'][1]}",
        f"- **Rubric version (self-reported):** {args.rubric_version}",
        f"- **Policy version (self-reported):** {args.policy_version}",
        f"- **Cases:** {result['case_count']} synthetic diagnostic cases.",
        f"- **Pairwise disagreements:** {result['disagreement_count']}", "",
        "| Dimension | Exact matches | Pairs | Numeric pairs | Unweighted kappa | Quadratic weighted kappa |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for dim, stats in result["per_dimension"].items():
        lines.append(f"| {dim} | {stats['exact_matches']} | {stats['all_paired_cases']} | "
                     f"{stats['numeric_pairs_for_kappa']} | {show(stats['cohen_kappa_unweighted'])} | "
                     f"{show(stats['cohen_kappa_quadratic_weighted'])} |")
    lines += ["", "> These are descriptive results from a small, authored synthetic case set. They do not establish benchmark-level accuracy, production reliability, or generalizable human agreement. Kappa may be not estimable for small or degenerate samples. The script cannot verify rater identity, independence, or authenticity.", ""]
    (output_dir / "run_summary.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ratings", type=Path, default=TEMPLATE, help="completed two-rater CSV")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output")
    parser.add_argument("--rubric-version", default="Proposed v1.1")
    parser.add_argument("--policy-version", default="Not supplied")
    args = parser.parse_args()
    cases = read_cases()
    raters, ratings = read_ratings(args.ratings, {c["id"] for c in cases})
    result = summarize(raters, ratings, cases)
    write_outputs(result, args, args.output_dir)
    print(f"Wrote human-rating summary for {len(cases)} cases and {len(raters)} raters to {args.output_dir}")
    print("Review run_summary.md, agreement_metrics.json, and disagreements.csv; do not present this synthetic diagnostic exercise as benchmark validation.")


if __name__ == "__main__":
    main()
