# Data Quality Report

Running log of every data-quality issue found, in the order discovered.
Each entry follows the same structure so it can be traced back to evidence,
not asserted from memory.

---

## Template (copy this block for each new finding)

### [Table.column] — Short description of the issue

- **What was wrong:**
- **How was it detected:** (exact check/code run)
- **Evidence:** (counts, example rows)
- **Is this a data-quality issue or a legitimate business variation?**
- **Rule applied / correction made:**
- **Records that could not be confidently corrected:** (count, and what
  happens to them — rejected_records.csv with reason, or flagged and
  carried forward with a caveat)
- **Business impact:** (how many downstream metrics/rows affected)

---

## Finding 1 — `agents.csv`: agent_id is not a stable identity key

- **What was wrong:** `agents.csv` has 30,000 rows but only 1,000 unique
  `agent_id` values (30x duplication). Rows sharing the same `agent_id`
  have DIFFERING `employee_code`, `agent_name`, `vendor_id`, and `team` —
  these are not exact duplicate rows, they're conflicting records.
- **How was it detected:** `df['agent_id'].nunique()` vs `len(df)`;
  inspected one agent_id's 31 rows directly.
- **Evidence:** e.g. `AGT0000760` appears with 6 different names, 6
  different employee_codes, 6 different vendor_ids across its 31 rows.
  `employee_code` was checked as an alternative key and also fails
  (1,099 unique employee_codes also map to multiple agent_ids/names).
- **Is this a data-quality issue or legitimate variation?** STILL BEING
  INVESTIGATED. Candidate explanations: (a) ID recycling after attrition
  + SCD-style snapshotting, (b) genuine identity resolution failure,
  (c) intentionally unresolvable at this table's grain.
- **Rule applied:** NOT YET DECIDED — pending overlap test on calls.csv.
- **Records that could not be confidently corrected:** N/A yet.
- **Business impact:** Any agent-level metric (recovery per agent-hour,
  agent tenure analysis, agent-level conversion) is unreliable until this
  is resolved.

**Status: IN PROGRESS — next step is the calls.csv overlap test.**

---

## Finding 2 — `vendor_id` is an overloaded column across tables

- **What was wrong:** `vendor_id` appears in both `agents.csv` and
  `calls.csv` (and `call_attempts.csv`) using the same `VND0000xx` ID
  format, which could wrongly suggest they mean the same entity.
- **How was it detected:** Checked `vendor_telephony.csv`, which is a
  clean 15-row reference table of telephony carriers (Airtel, Exotel,
  Twilio, Knowlarity, TataTele).
- **Evidence:** `calls.vendor_id` values resolve directly to these
  telephony carriers. `agents.vendor_id` almost certainly refers to a
  different concept (staffing/BPO vendor), based on business context —
  this inference itself should be verified against any other reference
  table before being treated as fact.
- **Is this a data-quality issue or legitimate variation?** This is a
  data-modeling ambiguity/trap, not a corruption — both uses are
  "correct" within their own table, but must not be joined or compared
  as if they're the same entity.
- **Rule applied:** Documented the distinction; will NOT join
  `agents.vendor_id` to `vendor_telephony.csv` without further
  verification. Will treat as two logically separate fields even though
  the column name is shared.
- **Records affected:** N/A — this is a modeling/definition finding, not
  a row-level correction.
- **Business impact:** Would have caused a false "vendor performance"
  analysis if the two fields were merged without checking.

**Status: RESOLVED (documented as a modeling caveat).**

---

## Finding 3 — [next finding goes here]

TODO
