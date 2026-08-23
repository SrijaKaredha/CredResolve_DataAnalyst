# CredResolve – Data Quality Assessment & Monitoring Framework

## Project Overview

CredResolve is a data quality assessment project designed to identify, measure, and interpret data-quality issues across operational datasets.

The project evaluates data from multiple business processes and focuses on important data-quality dimensions such as completeness, uniqueness, consistency, identity integrity, payment integrity, timestamp validity, and campaign targeting.

The analysis was performed using Python in Google Colab, with data profiling, validation, analytical checks, and visualization techniques.

---

## Project Objective

The main objective of this project is to:

- Assess the quality of operational datasets.
- Identify missing values and incomplete records.
- Detect duplicate records and duplicate identifiers.
- Identify borrower and agent identity conflicts.
- Validate payment references and transaction integrity.
- Validate timestamp consistency.
- Analyze campaign targeting patterns.
- Prioritize critical data-quality risks.
- Provide practical recommendations for improving data reliability.

---

## Dataset Overview

The project evaluates **18 operational datasets containing 639,328 records**.

The datasets represent different operational areas such as:

- Borrower information
- Payment transactions
- Calls
- WhatsApp events
- Agent activities
- Field visits
- Campaign activities
- Other operational records

The analysis was performed across these datasets to identify cross-dataset quality issues and inconsistencies.

---

## Methodology

The project follows a structured data-quality assessment workflow:

1. **Data Profiling**
   - Understand dataset structure, columns, records, and identifiers.

2. **Completeness Analysis**
   - Identify missing values in important fields.

3. **Uniqueness Analysis**
   - Detect duplicate records and repeated identifiers.

4. **Consistency Analysis**
   - Check borrower, agent, and transaction identity consistency.

5. **Validation**
   - Validate timestamps, payment references, and other logical conditions.

6. **Business Interpretation**
   - Convert technical data-quality findings into business risks and recommendations.

---

## Key Data Quality Checks

### 1. Completeness

Missing-value analysis was performed across important operational fields such as:

- Borrower email
- Borrower phone
- Agent ID
- Vendor ID
- Payment reference
- Scheduled timestamps

### 2. Uniqueness

Duplicate records and duplicate keys were identified across major datasets.

### 3. Identity Resolution

Borrower and agent identity consistency was evaluated across related operational datasets.

### 4. Payment Integrity

Payment references were analyzed to identify inconsistent or conflicting mappings.

### 5. Timestamp Validation

Timestamp relationships were checked to identify invalid event ordering.

### 6. Campaign Targeting

Campaign records were analyzed by communication channel and campaign distribution.

---

## Key Findings

The analysis produced the following major findings:

- **77.33% of unique borrower IDs have identity conflicts**, indicating significant borrower identity inconsistency.
- **100% of agent IDs show identity conflicts**, highlighting the need for stronger agent identity validation.
- **16.36% of payment references have conflicts**, creating a risk of incorrect payment mapping.
- Borrowers contain **600 duplicate records (1.96%)**.
- Payments contain **486 duplicate records (1.91%)**.
- Calls contain **1,271 duplicate records (1.39%)**.
- WhatsApp events contain **600 duplicate records (0.99%)**.
- The highest missing-value issue is **borrower email with 895 missing records (2.92%)**.
- Call attempts contain **2,400 missing vendor IDs (2.00%)**.
- No timestamp ordering violation was detected in the agent-session analysis.
- Campaign targeting contains **45,000 records across 120 campaigns**.

---

## Business Impact

The identified data-quality issues can affect:

- Customer identification
- Payment reconciliation
- Operational reporting
- Campaign targeting
- Customer communication
- Agent performance tracking
- Business decision-making
- Data-driven analytics

High identity and payment inconsistencies can reduce confidence in downstream reporting and analytical processes.

---

## Recommendations

The project recommends:

1. Implement unique borrower and agent identity validation.
2. Standardize and validate payment references before reporting.
3. Detect and manage duplicate transaction records.
4. Improve collection of borrower phone numbers and email addresses.
5. Validate mandatory foreign-key fields such as `agent_id`, `vendor_id`, and `borrower_id`.
6. Introduce automated data-quality monitoring for duplicates and identity conflicts.
7. Use campaign and communication-channel analysis to improve targeting decisions.

---

## Technology Stack

| Category | Technology |
|---|---|
| Programming | Python |
| Data Analysis | Pandas |
| Numerical Analysis | NumPy |
| Visualization | Matplotlib |
| Development Environment | Google Colab |
| Approach | Data Profiling & Data Quality Validation |

---

## Project Structure

```text
CredResolve_Data_Analyst/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_data_quality.ipynb
│   ├── 03_data_corrections.ipynb
│   └── 04_analysis.ipynb
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── src/
│   ├── profiling.py
│   ├── cleaning.py
│   ├── validation.py
│   └── analysis.py
│
├── README.md
├── data_quality_report.md
└── requirements.txt
