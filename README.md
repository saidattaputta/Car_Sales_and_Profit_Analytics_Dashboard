# Car Sales & Service Analytics Dashboard

An exploratory analytics project using a car sales workbook to study sales volume, profitability, dealer performance, model-level results, recalls, and customer sentiment across the 2018–2019 period described by the project dataset.

## Project Objective

Provide an accessible view of commercial and after-sales performance so stakeholders can compare vehicle models and dealers, monitor changes over time, and investigate service-related signals.

## Data

The repository contains the Excel workbook `CarSalesByModelStart copy.xlsx`. The README and analysis script refer to a `CarSales` worksheet with fields such as date, model, dealer, quantity sold, and profit.

## Workflow

1. Load the workbook using pandas.
2. Remove rows with missing values in the current cleaning script.
3. Parse the transaction date.
4. Derive a year-month field for time-based grouping.
5. Aggregate units sold by model and profit by dealer.
6. Review the accompanying sales and service dashboard screenshots and reported insights.

## Reported Results

The existing project documentation reports:

- Total profit: **$29,968,866**
- Total quantity sold: **58,118 units**
- Labrador and Salish as leading models by sales/profit
- Dealer 1288 as a strong performer
- Sales/profit seasonality around May–June
- Recall and sentiment patterns that warrant after-sales investigation

These figures and conclusions are transcribed from the project's existing analysis notes and should be validated against the workbook when the analysis is rerun.

## Repository Contents

```text
.
├── CarSalesByModelStart copy.xlsx
├── data_.py
└── README.md
```

## Run the Python Analysis

Prerequisites: Python 3 and pandas, openpyxl.

```bash
pip install pandas openpyxl
python data_.py
```

The script expects the workbook path configured in the file to resolve from the working directory. Run it from the repository root and adjust the path locally if your environment differs.

## Tools

- Python
- pandas
- Excel
- Dashboard / visualization deliverables referenced in the project documentation

## Limitations

- The current Python script is a compact cleaning and aggregation workflow, not a complete automated dashboard pipeline.
- The script drops every row containing a missing value; this can remove useful records and should be reviewed before production use.
- Findings depend on the supplied workbook and its definitions of profit, sales, recalls, and sentiment.

## Author

Sai Datta Putta
