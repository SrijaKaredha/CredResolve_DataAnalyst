"""
validation.py
--------------
Reusable functions for Stage 1 (identity resolution) and Stage 3
(timestamp/timezone forensics) and referential integrity checks.

Fill in the logic yourself as we work through each stage.
"""

import pandas as pd


def detect_overlapping_events(
    df: pd.DataFrame,
    group_col: str,
    start_col: str,
    duration_sec_col: str,
) -> pd.DataFrame:
    """
    Detect physically-impossible overlapping events for the same entity
    (e.g. same agent_id on two calls at once).

    This is the agent_id overlap test we're currently running on calls.csv.
    Returns a DataFrame of the overlapping row-pairs, with an 'overlaps_prev'
    flag, for inspection.
    """
    # TODO: implement using groupby + shift, as discussed
    raise NotImplementedError


def orphan_foreign_keys(
    child_df: pd.DataFrame,
    child_key: str,
    parent_df: pd.DataFrame,
    parent_key: str,
) -> pd.DataFrame:
    """
    Referential integrity check: find rows in child_df whose child_key
    value does NOT exist in parent_df's parent_key column.
    E.g. calls.account_id values that don't exist in accounts.account_id.
    """
    # TODO
    raise NotImplementedError


def timezone_distribution(df: pd.DataFrame, tz_col: str = "timezone") -> pd.Series:
    """Count how many rows fall into each distinct timezone value."""
    # TODO
    raise NotImplementedError


def normalize_to_utc(df: pd.DataFrame, ts_col: str, tz_col: str) -> pd.DataFrame:
    """
    Convert a naive/local timestamp column to a single canonical UTC column,
    using the per-row timezone label in tz_col.
    Returns df with a new column: f"{ts_col}_utc"
    IMPORTANT: discuss the assumption here before implementing — are the raw
    timestamps naive-local (need localization) or already tz-aware?
    """
    # TODO
    raise NotImplementedError


def events_before_account_open(
    events_df: pd.DataFrame,
    event_ts_col: str,
    accounts_df: pd.DataFrame,
    account_open_col: str = "opened_at",
    account_key: str = "account_id",
) -> pd.DataFrame:
    """
    Sanity check: flag any event (call, payment, etc.) that is timestamped
    BEFORE its account was opened. Should be zero/near-zero if data is clean.
    """
    # TODO
    raise NotImplementedError
