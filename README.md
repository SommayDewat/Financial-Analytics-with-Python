<div align="center">

# 📊 Financial Analytics with Python

### Junior Data Analyst Internship | End-to-End Financial Data Analysis

[![Python](https://img.shields.io/badge/Python-3.10.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)](https://seaborn.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

**A five-week learning project focused on preparing, exploring, visualizing, forecasting, and analyzing financial data with Python.**

</div>

---

## 📌 Project Overview

This repository documents my work for the **Junior Data Analyst – Financial Analytics with Python** internship. It follows a structured analytical workflow, beginning with financial analytics fundamentals and progressing through data preparation, exploratory data analysis (EDA), visualization, forecasting, and reporting.

The project uses a **simulated stock-market dataset** for practice. The dataset is synthetic and should not be interpreted as actual market data or investment advice.

## 🎯 Project Objectives

- Build a foundation in financial analytics and analytical methods.
- Prepare and validate structured financial datasets using Pandas.
- Explore distributions, trends, relationships, and potential anomalies.
- Build and evaluate a baseline and a machine-learning forecasting model.
- Communicate findings through clear statistical summaries, visualizations, and reports.
- Maintain reproducible notebooks, scripts, datasets, and reports.

## 🗂️ Internship Roadmap

| Week | Focus | Status |
|---|---|---|
| **Week 1** | Financial Analytics Orientation & Python Setup | Completed |
| **Week 2** | Data Preparation & Cleaning | Completed |
| **Week 3** | Exploratory Data Analysis & Visualization | Completed |
| **Week 4** | Financial Forecasting & Model Evaluation | Completed |
| **Week 5** | Final Analysis & Reporting | Upcoming |

> **Progress note:** Weeks 1–4 have been completed and documented. Week 5 is the remaining stage of the internship workflow.

---

## 🔎 Week 1 — Financial Analytics Orientation

### Objective
Establish a foundation in financial analytics and configure a reproducible Python environment for the remaining tasks.

### Work Completed
- Researched financial analytics fundamentals, financial statements, indicators, and common analysis methods.
- Set up Python **3.10.11** and a project-specific virtual environment.
- Installed and tested the core data-analysis libraries.
- Verified the environment in VS Code and Jupyter Notebook.
- Documented setup steps, challenges, and a workflow for subsequent tasks.

### Output
- Financial analytics orientation report and Python environment setup documentation.

---

## 🧹 Week 2 — Data Preparation & Cleaning

### Objective
Prepare a simulated stock-market dataset for analysis by identifying and handling data-quality issues.

### Dataset
The raw stock-market dataset contains **503 rows** and includes deliberately introduced quality issues for cleaning practice. After cleaning and validation, the analysis-ready dataset contains **499 rows**.

**Main fields:** `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`.

### Cleaning Workflow
- Inspected data types, missing values, duplicate records, and inconsistent entries.
- Converted fields to appropriate data types and handled invalid dates.
- Removed duplicate rows and addressed missing values.
- Corrected invalid volume and OHLC records.
- Created derived features: `Price_Change` and `Daily_Return_Pct`.
- Validated the cleaned data for missing values, duplicates, negative volume, and OHLC consistency.

### Outputs
- Raw and cleaned CSV datasets
- Python scripts for dataset generation, assessment, cleaning, and validation
- Jupyter Notebook and Word report

---

## 📈 Week 3 — Exploratory Data Analysis & Visualization

### Objective
Use descriptive statistics and visual analysis to understand the simulated stock-market dataset's behavior, relationships, and potential outliers.

### Analysis Performed
- Reviewed dataset structure, date coverage, data types, and missing values.
- Calculated descriptive statistics such as mean, median, standard deviation, quartiles, minimum, and maximum.
- Examined correlations among OHLC prices, trading volume, price change, and daily returns.
- Applied the IQR method to identify potential outliers in closing prices and daily returns.

### Visualizations
- Closing-price time-series line chart
- Closing-price distribution histogram
- Daily-return distribution histogram
- Trading-volume distribution histogram
- Trading-volume trend over time
- Trading volume vs. closing-price scatter plot
- Box plots for closing prices and daily returns
- Correlation heatmap

### Preliminary Findings
Based on the simulated dataset:

- The closing price has a mean of approximately **123.05** and a median of **122.30**.
- Closing prices range from **87.28 to 166.35**.
- The average daily return is approximately **0.094%**; observed daily returns range from about **−3.893% to 5.246%**.
- OHLC variables are very strongly correlated in this dataset, while trading volume has a weak linear relationship with closing price.
- The IQR check identifies several daily-return observations outside the calculated bounds. These are potential statistical outliers, not automatically data errors.

These findings describe the simulated dataset only and do not represent real-world market behavior.

---

## 🤖 Week 4 — Financial Forecasting & Model Evaluation

### Objective
Develop and evaluate a next-day closing-price forecasting workflow using the cleaned simulated stock-market dataset.

### Dataset & Preparation
- Used the Week 3 cleaned dataset containing **499 rows** and 8 columns.
- Checked data quality and handled the remaining missing values in `Price_Change` and `Daily_Return_Pct` for modeling.
- Created the target variable, `Target_Next_Day_Close`, by shifting the `Close` price forward by one row.
- Prepared **497 modeling rows** after target creation and removal of rows without a valid next-day target.
- Used a chronological train-test split: **397 training rows** and **100 test rows**.

### Models Evaluated
1. **Naive baseline:** Uses the current closing price as the next-day closing-price estimate.
2. **Linear Regression:** Uses `Open`, `High`, `Low`, `Close`, `Volume`, `Price_Change`, and `Daily_Return_Pct` as input features to estimate the next-day close.

### Evaluation Metrics

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Naive Baseline (current close) | 1.2784 | 1.5876 | 0.8718 |
| Linear Regression | 1.3218 | 1.6241 | 0.8658 |

**Interpretation:** On this test set, the naive baseline produced slightly lower MAE and RMSE and a slightly higher R² than Linear Regression. This indicates that the trained model did not outperform simply using the current close as the next-day estimate in this experiment.

### Outputs
- Forecasting notebook: `Week_4/notebooks/Week_4_Financial_Forecasting.ipynb`
- Prediction results: `Week_4/outputs/forecast_predictions.csv`
- Model metrics: `Week_4/outputs/model_evaluation_metrics.csv`
- Actual vs. predicted chart: `Week_4/visualizations/actual_vs_predicted.png`
- Residual chart: `Week_4/visualizations/model_residuals.png`
- Forecasting report: `Week_4/reports/Week_4_Financial_Forecasting_Model_Report.docx`

### Limitations
The dataset is synthetic and the results are educational rather than financial guidance. The feature set includes same-day OHLC values and derived variables; whether these inputs are available at the intended forecast time must be considered. The evaluation does not establish that the model will generalize to real market data.

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python 3.10.11** | Programming and analysis |
| **Pandas** | Data loading, cleaning, transformation, and summary statistics |
| **NumPy** | Numerical operations |
| **Matplotlib** | Chart creation |
| **Seaborn** | Statistical visualization and correlation heatmaps |
| **SciPy** | Statistical analysis tools |
| **Scikit-learn** | Linear Regression and model evaluation |
| **Jupyter Notebook** | Interactive analysis and documentation |
| **VS Code** | Development environment |
| **Git & GitHub** | Version control and project sharing |

---

## 📁 Repository Structure

```text
Financial-Analytics-with-Python/
│
├── Week_1/
│   └── reports/
│
├── Week_2/
│   ├── data/
│   │   ├── raw/
│   │   └── cleaned/
│   ├── notebooks/
│   ├── outputs/
│   └── reports/
│
├── Week_3/
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   ├── reports/
│   └── visualizations/
│
├── Week_4/
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   ├── reports/
│   └── visualizations/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SommayDewat/Financial-Analytics-with-Python.git
cd Financial-Analytics-with-Python
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If `requirements.txt` is available and up to date:

```bash
pip install -r requirements.txt
```

### 4. Open the notebooks

Open the relevant `.ipynb` file in VS Code or Jupyter Notebook and run the cells in order. Confirm that the notebook's dataset paths match the repository folder structure.

---

## 📄 Deliverables

The repository contains project materials organized by week, including:

- Jupyter notebooks for analysis and modeling
- Python scripts for repeatable data-processing steps
- Raw and cleaned datasets
- Visualizations and statistical/model-evaluation outputs
- Word reports documenting methods, results, and interpretations

---

## ⚠️ Data & Interpretation Note

The stock-market data used for the cleaning, EDA, and forecasting exercises is **simulated**. Statistical relationships and model performance are specific to the generated dataset. Correlation does not establish causation. The analysis is for educational purposes only and is not financial or investment advice.

---

## 👤 Author

**Sommay Dewat**  
Junior Data Analyst Internship Project

- **GitHub:** [SommayDewat](https://github.com/SommayDewat)
- **Project Repository:** [Financial Analytics with Python](https://github.com/SommayDewat/Financial-Analytics-with-Python)

---

<div align="center">

**Learning through data • Exploring with Python • Communicating insights**

</div>
