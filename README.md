<div align="center">

# 📊 Financial Analytics with Python

### Junior Data Analyst Internship | End-to-End Financial Data Analysis

[![Python](https://img.shields.io/badge/Python-3.10.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)](https://seaborn.pydata.org/)

**A five-week learning project focused on preparing, exploring, visualizing, and analyzing financial data with Python.**

</div>

---

## 📌 Project Overview

This repository documents my work for the **Junior Data Analyst – Financial Analytics with Python** internship. It follows a structured analytical workflow, beginning with financial analytics fundamentals and progressing toward data preparation, exploratory data analysis (EDA), visualization, forecasting, and final reporting.

The project uses a **simulated stock-market dataset** for practice. The dataset is synthetic and should not be interpreted as actual market data or investment advice.

## 🎯 Project Objectives

- Build a foundation in financial analytics and analytical methods.
- Prepare and validate structured financial datasets using Pandas.
- Explore distributions, trends, relationships, and potential anomalies.
- Communicate findings through clear statistical summaries and visualizations.
- Maintain reproducible notebooks, scripts, datasets, and reports.

## 🗂️ Internship Roadmap

| Week | Focus | Work |
|---|---|---|
| **Week 1** | Financial Analytics Orientation & Python Setup | Financial concepts, analytical methods, Python environment, and project workflow |
| **Week 2** | Data Preparation & Cleaning | Simulated stock data, data-quality checks, cleaning, feature creation, and validation |
| **Week 3** | Exploratory Data Analysis & Visualization | Descriptive statistics, correlations, trend charts, distributions, scatter plots, and box plots |
| **Week 4** | Forecasting | Planned next stage of the internship workflow |
| **Week 5** | Final Analysis & Reporting | Planned consolidation of analysis and project findings |

> **Progress note:** Weeks 1 and 2 have been completed and documented. Week 3 is currently focused on EDA and financial data visualization. Weeks 4 and 5 are upcoming stages.

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
- Jupyter Notebook and a Word report

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
Based on the current simulated dataset:

- The closing price has a mean of approximately **123.05** and a median of **122.30**.
- Closing prices range from **87.28 to 166.35**.
- The average daily return is approximately **0.094%**; observed daily returns range from about **−3.893% to 5.246%**.
- OHLC variables are very strongly correlated in this dataset, while trading volume has a weak linear relationship with closing price.
- The IQR check identifies several daily-return observations outside the calculated bounds. These are potential statistical outliers, not automatically data errors.

These findings describe the simulated dataset only and do not represent real-world market behavior.

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
├── requirements.txt
├── .gitignore
└── README.md
```

*The folder structure may expand as the remaining internship tasks are completed.*

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

The repository is organized to include the following materials as each task is completed:

- Jupyter notebooks for analysis
- Python scripts for repeatable data-processing steps
- Raw and cleaned datasets
- Visualizations and statistical outputs
- Word reports documenting methods, results, and interpretations

---

## ⚠️ Data & Interpretation Note

The stock-market data used for the cleaning and EDA exercises is **simulated**. Statistical relationships and patterns are specific to the generated dataset. Correlation does not establish causation, and the analysis is for educational purposes only—not financial or investment advice.

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
