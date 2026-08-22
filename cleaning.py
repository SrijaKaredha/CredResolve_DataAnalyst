"""
cleaning.py
-----------
Stage 7: Golden Dataset construction.

RULE: every function here must be traceable to a documented decision in
data_quality_report.md. Do not add a cleaning step here until we've agreed
on: what's wrong, how we detected it, what evidence supports the fix, and
what rule we're applying. Records that can't be confidently corrected go
to `rejected_records.csv`, not silently dropped.
"""

import pandas as pd


def dedupe_exact(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Remove 100%-identical duplicate rows.
    Returns (deduped_df, removed_rows_df) — removed_rows_df goes to the
    rejected/corrected log with a reason column.
    """
    # TODO
    raise NotImplementedError


def resolve_agent_identity(agents_df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply whatever identity-resolution rule we decide on after the
    agent_id overlap investigation (Stage 1). Document the rule here
    once it's settled — do not implement before that discussion.
    """
    # TODO — placeholder until Stage 1 conclusion is reached
    raise NotImplementedError


def dedupe_payments(payments_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Stage 4: collapse duplicate payment events (e.g. same payment_reference
    appearing more than once, or retried ingestion events).
    Returns (clean_payments_df, rejected_or_merged_df).
    """
    # TODO
    raise NotImplementedError


def build_golden_dataset(
    corrected_tables: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    """
    Final assembly step: join the corrected tables into the analytical
    golden dataset used for metrics in Stage 8-9.
    Log row counts at each join step (Raw -> Rejected/Corrected -> Golden).
    """
    # TODO
    raise NotImplementedError


def log_correction(
    log_path: str,
    table: str,
    issue: str,
    detection_method: str,
    evidence: str,
    rule_applied: str,
    n_records_affected: int,
) -> None:
    """
    Append a structured row to a running correction log (CSV or markdown).
    Use this every time a cleaning decision is made, so data_quality_report.md
    can be generated/traced from it rather than written from memory.
    """
    # TODO
    raise NotImplementedError
