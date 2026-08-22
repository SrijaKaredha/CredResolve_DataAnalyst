"""
profiling.py
------------
Reusable functions for Stage 2: Table-by-Table Data Profiling.

Goal: for every raw table, answer:
  - How many rows? How many unique keys?
  - What % of each column is missing?
  - Are there exact duplicate rows?
  - Are there same-key-different-values conflicts (like we found in agents.csv)?

Fill in the logic yourself — these are stubs with the shape of what's needed.
Discuss each function's output with Claude before moving to the next table.
"""

import pandas as pd


def load_table(path: str, parse_dates: list[str] | None = None) -> pd.DataFrame:
    """Load a raw CSV. parse_dates: list of column names that are timestamps."""
    # TODO: read_csv with parse_dates
    raise NotImplementedError


def key_cardinality(df: pd.DataFrame, key_col: str) -> dict:
    """
    Compare total row count vs unique key count.
    Returns: {"total_rows": ..., "unique_keys": ..., "duplication_factor": ...}
    This is the check that caught agents.csv (30,000 rows / 1,000 unique agent_id).
    """
    # TODO
    raise NotImplementedError


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each column: count and % of missing (NaN / empty string) values.
    Returns a DataFrame sorted by % missing, descending.
    """
    # TODO
    raise NotImplementedError


def exact_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return rows that are 100% identical across ALL columns (true duplicates,
    as opposed to same-key-different-value conflicts).
    """
    # TODO: df[df.duplicated(keep=False)]
    raise NotImplementedError


def conflicting_key_records(df: pd.DataFrame, key_col: str) -> pd.DataFrame:
    """
    Return rows where the same key_col value appears multiple times
    WITH DIFFERING values in other columns (the agents.csv identity problem).
    """
    # TODO
    raise NotImplementedError


def profile_table(path: str, key_col: str, parse_dates: list[str] | None = None) -> dict:
    """
    Convenience wrapper: run all of the above on one table and return
    a summary dict you can log into your Data Quality Report.
    """
    # TODO: call the functions above and assemble a summary
    raise NotImplementedError
