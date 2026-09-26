<div align="center">

# 📊 Financial Analytics with Python

### Junior Data Analyst Internship | End-to-End Financial Data Analysis

[![Python](https://img.shields.io/badge/Python-3.10.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)](https://seaborn.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

**A five-week applied project covering financial analytics fundamentals, data preparation, exploratory analysis, forecasting, and professional reporting using Python.**

[Project Repository](https://github.com/SommayDewat/Financial-Analytics-with-Python) · [Author Profile](https://github.com/SommayDewat)

</div>

---

## 📌 Project Overview

This repository contains my **Junior Data Analyst – Financial Analytics with Python** internship work. Across five weeks, I followed an end-to-end analytical workflow: understanding financial analytics, setting up a Python environment, preparing and validating a simulated stock-market dataset, performing exploratory data analysis (EDA), building and evaluating a next-day closing-price forecasting baseline, and consolidating findings into a final report.

> **Dataset disclaimer:** The stock-market data used in this project is simulated/synthetic. Findings and model scores are for learning and demonstration only; they do not represent real market behavior or investment advice.

## 🗺️ Project Roadmap

| Week | Topic | Main Deliverables | Status |
|---|---|---|---|
| 1 | Financial Analytics Orientation & Python Setup | Orientation report, setup notebook, and setup screenshots | Completed |
| 2 | Data Preparation & Cleaning | Raw and cleaned CSVs, cleaning notebook, validation scripts, and report | Completed |
| 3 | Exploratory Data Analysis & Visualization | EDA notebook, summary outputs, charts, and report | Completed |
| 4 | Financial Forecasting & Model Evaluation | Forecasting notebook, predictions, metrics, diagnostic plots, and report | Completed |
| 5 | Comprehensive Financial Analytics Report | Consolidated report and recommendations | Completed |

---

## ✨ Project Highlights

- Cleaned and validated a simulated dataset from **503 raw rows to 499 analysis-ready rows**.
- Explored closing-price and daily-return distributions, OHLC relationships, volume behavior, and potential outliers.
- Created a next-observation closing-price target and prepared **497 modeling rows**.
- Used a chronological split of **397 training rows and 100 test rows**.
- Compared a current-close Naive Baseline with Linear Regression using MAE, RMSE, and R².
- Organized notebooks, scripts, datasets, charts, and reports by project week.

## 📈 Key Findings

### Exploratory Data Analysis

| Metric | Finding |
|---|---:|
| Cleaned dataset size | 499 rows |
| Mean closing price | ~123.05 |
| Median closing price | 122.30 |
| Closing-price range | 87.28–166.35 |
| Average daily return | ~0.094% |
| Daily-return range | ~−3.893% to 5.246% |

OHLC variables showed strong relationships in this simulated dataset. Trading volume had a weak linear relationship with closing price. IQR screening identified potential daily-return outliers for review; an outlier flag alone does not establish that a record is erroneous.

### Forecasting Evaluation

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Naive Baseline (current close) | 1.2784 | 1.5876 | 0.8718 |
| Linear Regression | 1.3218 | 1.6241 | 0.8658 |

**Result:** On the documented test split, the Naive Baseline had lower MAE and RMSE and a higher R² than Linear Regression. These scores apply only to this synthetic dataset and split. Feature availability and possible look-ahead leakage should be checked before treating the workflow as a valid real-time forecasting setup.

---

## 📚 Weekly Work Summary

### Week 1 — Financial Analytics Orientation & Python Setup
- Reviewed financial analytics concepts and common financial data analysis approaches.
- Set up Python **3.10.11**, a project virtual environment, and the analysis libraries.
- Verified Python, package installation, Jupyter, and the project structure.
- **Files:** [Notebook](Week_1/notebooks/Week_1_Financial_Analytics_Analysis.ipynb) · [Orientation Report](Week_1/reports/Week_1_Financial_Analytics_Orientation_Report.docx)
- Setup evidence is stored in `Week_1/screenshots/`.

### Week 2 — Data Preparation & Cleaning
- Inspected the raw dataset and performed data-quality checks.
- Cleaned and validated the dataset and generated derived fields such as `Price_Change` and `Daily_Return_Pct`.
- Organized raw and cleaned data, reusable Python scripts, a notebook, and a written report.
- **Files:** [Cleaning Notebook](Week_2/notebooks/Week_2_Data_Cleaning.ipynb) · [Cleaned Dataset](Week_2/data/cleaned/stock_market_cleaned.csv) · [Report](Week_2/reports/Week_2_Data_Preparation_and_Cleaning_Report.docx)

### Week 3 — Exploratory Data Analysis & Visualization
- Calculated descriptive statistics and examined price movements and return distributions.
- Analyzed correlations among OHLC variables and the relationship between volume and closing price.
- Used IQR-based screening to flag potential outliers.
- Created price, return, volume, distribution, and relationship visualizations.
- **Files:** [EDA Notebook](Week_3/notebooks/Week_3_EDA_and_Financial_Visualization.ipynb) · [Visualizations](Week_3/visualizations/) · [Report](Week_3/reports/)

### Week 4 — Financial Forecasting & Model Evaluation
- Created `Target_Next_Day_Close` by shifting the `Close` series by one observation.
- Prepared 497 modeling rows and applied a chronological 397/100 train-test split.
- Compared a current-close Naive Baseline with Linear Regression.
- Exported predictions, model metrics, and diagnostic plots.
- **Files:** [Forecasting Notebook](Week_4/notebooks/Week_4_Financial_Forecasting.ipynb) · [Predictions](Week_4/outputs/forecast_predictions.csv) · [Metrics](Week_4/outputs/model_evaluation_metrics.csv) · [Report](Week_4/reports/Week_4_Financial_Forecasting_Model_Report.docx)

### Week 5 — Comprehensive Report & Recommendations
- Consolidated the project workflow, key findings, evaluation results, and limitations.
- Summarized practical recommendations for data quality, time-aware validation, feature timing, and responsible model use.
- **File:** [Week 5 Comprehensive Report](Week_5/reports/Week_5_Comprehensive_Financial_Analytics_Report_Professional.docx)

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.10.11 | Programming and analysis |
| Pandas | Data loading, cleaning, transformation, and summaries |
| NumPy | Numerical operations |
| Matplotlib & Seaborn | Data visualization |
| SciPy | Statistical analysis tools |
| Scikit-learn | Regression and model evaluation |
| Jupyter Notebook | Interactive analysis |
| VS Code | Development environment |
| Git & GitHub | Version control and project sharing |

---

## 🗂️ Repository Structure

The structure below follows the folders and filenames visible in the project workspace screenshots. The `.venv/` directory is local environment content and is typically excluded from version control.

```text
Financial-Analytics-with-Python/
├── .venv/                              # Local Python virtual environment
├── Week_1/
│   ├── notebooks/
│   │   └── Week_1_Financial_Analytics_Analysis.ipynb
│   ├── reports/
│   │   └── Week_1_Financial_Analytics_Orientation_Report.docx
│   └── screenshots/
│       ├── 01_python_environment_verification.png
│       ├── 02_pip_upgrade.png
│       ├── 03_library_verification.png
│       ├── 04_jupyter_verification.png
│       ├── 05_project_structure.png
│       ├── 06_vscode_jupyter_kernel_verification.png
│       └── 07_notebook_library_verification.png
├── Week_2/
│   ├── data/
│   │   ├── cleaned/
│   │   │   └── stock_market_cleaned.csv
│   │   └── raw/
│   │       └── stock_market_raw.csv
│   ├── notebooks/
│   │   └── Week_2_Data_Cleaning.ipynb
│   ├── outputs/
│   │   ├── assess_raw_data.py
│   │   ├── clean_financial_data.py
│   │   ├── generate_raw_dataset.py
│   │   └── validate_cleaned_data.py
│   └── reports/
│       └── Week_2_Data_Preparation_and_Cleaning_Report.docx
├── Week_3/
│   ├── data/
│   │   └── stock_market_cleaned.csv
│   ├── notebooks/
│   │   └── Week_3_EDA_and_Financial_Visualization.ipynb
│   ├── outputs/
│   │   ├── final_correlation_matrix.csv
│   │   └── final_statistical_summary.csv
│   ├── reports/
│   │   └── Week_3_Exploratory_Data_Analysis_and_Visualization_Report.docx
│   └── visualizations/
│       ├── closing_price_boxplot.png
│       ├── closing_price_histogram.png
│       ├── closing_price_trend.png
│       ├── daily_returns_boxplot.png
│       ├── daily_returns_histogram.png
│       ├── daily_volume_trend.png
│       ├── volume_distribution.png
│       └── volume_vs_closing_price.png
├── Week_4/
│   ├── data/
│   │   └── stock_market_cleaned.csv
│   ├── notebooks/
│   │   └── Week_4_Financial_Forecasting.ipynb
│   ├── outputs/
│   │   ├── forecast_predictions.csv
│   │   └── model_evaluation_metrics.csv
│   ├── reports/
│   │   └── Week_4_Financial_Forecasting_Model_Report.docx
│   ├── scripts/
│   └── visualizations/
│       ├── actual_vs_predicted.png
│       └── model_residuals.png
├── Week_5/
│   └── reports/
│       └── Week_5_Comprehensive_Financial_Analytics_Report_Professional.docx
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SommayDewat/Financial-Analytics-with-Python.git
cd Financial-Analytics-with-Python
```

### 2. Create and activate a virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Open the project

Open the repository folder in VS Code. Launch the relevant `.ipynb` notebook and run its cells in order. Confirm that any data paths in the notebook are relative to the repository root and that the required dataset is present.

---

## 🔍 Recommendations & Next Steps

1. **Document outlier decisions:** Include the IQR thresholds, flagged records, and rationale for retaining, correcting, or excluding any observations. The exact thresholds and flagged-row details are not reproduced here because they were not available in the verified project summary.
2. **Use time-aware validation:** Evaluate forecasting models with rolling- or expanding-window validation in addition to a chronological holdout.
3. **Check feature timing:** Ensure every feature would be available at the actual forecast timestamp. Same-day High, Low, Close, and derived fields may introduce look-ahead leakage depending on the prediction setup.
4. **Compare with simple baselines:** Keep a clearly defined naive baseline when testing more complex forecasting approaches.
5. **Improve reproducibility:** Record dataset-generation assumptions, package versions, validation rules, and run instructions.

## ⚠️ Limitations & Responsible Use

- The dataset is simulated/synthetic, not live market data.
- Model results are based on one chronological holdout split and do not establish generalization to real markets.
- Feature timing needs review to rule out potential look-ahead leakage.
- Outlier flags indicate observations for investigation; they do not automatically mean data errors.
- This project is educational and is not financial or investment advice.

---

## 👤 Author

**Sommay Dewat**  
Junior Data Analyst | Financial Analytics with Python

- **GitHub:** [SommayDewat](https://github.com/SommayDewat)
- **Project Repository:** [Financial Analytics with Python](https://github.com/SommayDewat/Financial-Analytics-with-Python)

<div align="center">

**Data preparation · Exploratory analysis · Forecasting · Evidence-based reporting**

</div>
