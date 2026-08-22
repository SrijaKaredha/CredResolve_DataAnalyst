"""
analysis.py
-----------
Stage 8-11: metric definitions, the 11% claim test, mix-adjustment,
and the counterfactual (diff-in-diff or similar).

Each metric function should include a docstring explaining WHY it's
defined this way and how it differs from the "reported" definition,
per the assignment's Part 3 requirement ("explain why your definitions
are appropriate").
"""

import pandas as pd


def contact_rate(calls_df: pd.DataFrame) -> pd.Series:
    """
    Define and compute contact rate by month.
    TODO: decide numerator/denominator — e.g. answered calls / total
    dialed attempts, and whether denominator should be unique accounts
    or unique attempts. Document the choice.
    """
    raise NotImplementedError


def right_party_contact_rate(calls_df: pd.DataFrame, dispositions_df: pd.DataFrame) -> pd.Series:
    """RPC = confirmed contact with the actual borrower, not just 'answered'."""
    raise NotImplementedError


def ptp_rate(ptp_df: pd.DataFrame, calls_df: pd.DataFrame) -> pd.Series:
    """PTP rate = promises-to-pay / (RPCs or contacted accounts). Define denominator."""
    raise NotImplementedError


def ptp_kept_rate(ptp_df: pd.DataFrame, payments_df: pd.DataFrame) -> pd.Series:
    """% of PTPs where a matching payment was actually received by promised_date."""
    raise NotImplementedError


def recovery_rate(payments_df: pd.DataFrame, accounts_df: pd.DataFrame) -> pd.Series:
    """
    TODO: decide the denominator carefully — this is the crux of testing
    the 11% claim. Total outstanding at start of period? Active account
    count? Watch for denominator manipulation (Part 2G in the brief).
    """
    raise NotImplementedError


def mix_adjusted_recovery_rate(
    payments_df: pd.DataFrame,
    accounts_df: pd.DataFrame,
    mix_dims: list[str],
) -> pd.Series:
    """
    Stage 6/9: hold portfolio mix (e.g. dpd bucket, risk_segment) constant
    across months to isolate genuine operational improvement from mix shift.
    Simplest approach: standardize each month's rate to a fixed reference
    mix (e.g. month-1 mix) — document as 'Fact/Strong Evidence/Correlation/
    Hypothesis' per the assignment's classification requirement.
    """
    raise NotImplementedError


def diff_in_diff(
    df: pd.DataFrame,
    treatment_col: str,
    time_col: str,
    outcome_col: str,
    treatment_period_start,
) -> dict:
    """
    Stage 10 counterfactual: estimate what recovery would have looked like
    without the targeting-strategy change, using diff-in-diff.
    Define treatment group, control group, and pre/post periods before
    implementing — this must be discussed and justified, not assumed.
    """
    raise NotImplementedError
