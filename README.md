# Forecasting of peak hour for urban planning

Predictive analytics pipeline forecasting peak bus travel demand for Hampshire
bus services (Go-Ahead / Go South Coast), built for an Urban Planner / Smart
City Team stakeholder to support evidence-based infrastructure and public
transport investment decisions.

**Data source**: [UK Bus Open Data Service (BODS)](https://data.bus-data.dft.gov.uk/)

## Summary

This pipeline ingests, cleans, and joins four bus operational datasets
(Timetables, Fares, Location/AVL, and synthetic Disruptions) at scale using
PySpark, stores them in a MySQL relational database, and compares three
regression models to forecast route-level peak-hour demand. Results are
presented via an interactive Streamlit dashboard.


## Setup Instructions


### Prerequisites
- Python 3.12
- Java (required for PySpark)
- MySQL Server + MySQL Workbench
- MySQL Connector/J (JDBC driver, `.jar` file)

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up MySQL
1. Create a database: `CREATE DATABASE bus_analytics;`
2. Set your MySQL password as an environment variable:
```bash
   setx MYSQL_PASSWORD "your_password_here"
```
3. Download MySQL Connector/J and update the `spark.jars` path in
   `DatabaseWork.ipynb` to match your local `.jar` file location.

### 3. Run the pipeline (in order)
1. `DatasetPrep.ipynb` — ingest and clean all datasets, build `combined_dataset`
2. `DatabaseWork.ipynb` — load cleaned data into MySQL, run SQL queries
3. `EDA.ipynb` — exploratory analysis and profiling
4. `ML_Modeling.ipynb` — train and evaluate models, export prediction CSVs

### 4. Run the dashboard
```bash
streamlit run dashboard.py
```
Opens at `http://localhost:8501`.

## Data Scale

| Dataset | Records |
|---|---|
| Timetables | 14,391 |
| Fares | 8,980 |
| Location (AVL) | 128,621 |
| Disruptions (synthetic) | 3,000 |
| **Total ingested** | **154,992** |

The full technical report includes complete methodology, evaluation, and
critical reflection.