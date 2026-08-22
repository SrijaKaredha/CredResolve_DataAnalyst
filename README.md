# CredResolve Data Analyst Assignment

## Status: IN PROGRESS

This repository is being built incrementally, stage by stage, with every
finding backed by evidence run against the actual dataset (not assumed).
See `data_quality_report.md` for the running log of findings.

## Project Roadmap

- [x] Stage 0 — Setup & orientation (all 17 tables confirmed, README + data
      dictionary reviewed)
- [ ] Stage 1 — Entity & identity resolution
  - [x] `agents.csv`: found 30,000 rows / 1,000 unique `agent_id`, with
        conflicting values per id (not exact duplicates)
  - [x] Ruled out `vendor_id` confusion as an explanation (telephony vendor
        in `calls.csv` != staffing vendor in `agents.csv`, confirmed via
        `vendor_telephony.csv`)
  - [ ] Overlap test on `calls.csv` to determine if `agent_id` is
        recycled/shared, a timestamp bug, or something else — IN PROGRESS
- [ ] Stage 2 — Table-by-table data profiling
- [ ] Stage 3 — Timestamp & timezone forensics
- [ ] Stage 4 — Payment forensics
- [ ] Stage 5 — Denominator & population checks
- [ ] Stage 6 — Portfolio mix & cohort analysis
- [ ] Stage 7 — Golden dataset construction
- [ ] Stage 8 — Metric redefinition
- [ ] Stage 9 — Testing the reported 11% improvement claim
- [ ] Stage 10 — Counterfactual (targeting strategy change)
- [ ] Stage 11 — ₹10 Cr investment recommendation
- [ ] Stage 12 — Final deliverables (dashboard, memo, architecture diagram)

## Repository Structure

```
data/raw/           -- original 17 CSVs, untouched
data/processed/      -- rejected_records.csv, corrected_records.csv, golden_dataset.csv
notebooks/           -- 01_data_profiling, 02_data_quality, 03_data_corrections, 04_analysis
src/                 -- reusable functions (profiling, validation, cleaning, analysis)
outputs/figures/     -- exported charts for the dashboard/memo
outputs/reports/     -- executive memo, data quality report exports
```

## How to run

```
pip install -r requirements.txt
jupyter notebook notebooks/01_data_profiling.ipynb
```

## Principles followed in this project

- No cleaning decision is made without evidence checked against the actual
  data (not assumed from column names).
- Every correction is logged: what was wrong, how it was detected, what
  evidence supports the fix, what rule was applied, what happens to records
  that can't be confidently corrected.
- Conclusions about *why* metrics moved are classified as
  Fact / Strong Evidence / Correlation / Hypothesis — correlation is never
  presented as causation.
