# Uber CRM Intelligence Pipeline
### CSCI 6991 Data Engineering Capstone

## Project Overview
An end-to-end data engineering pipeline that transforms 150,000 raw Uber trip records into actionable CRM insights. This project uses an adjusted RFM (Recency, Frequency, Monetary) model to identify "At-Risk" users, helping protect an estimated $47M in potential revenue.

## Tech Stack
- **Language:** Python 3.12 (Pandas)
- **Database:** SQL (SQLite3)
- **Visualization:** Power BI Cloud
- **Architecture:** Relational Star Schema

## Key Engineering Features
- **Contextual Feature Engineering:** Created `is_rush_hour` and `is_success` flags to analyze churn triggers.
- **Star Schema:** Optimized data retrieval by separating entities into Fact and Dimension tables.
- **Dynamic SQL Views:** Implemented automated RFM segmentation logic.

## How to Run
1. Run `python3 02_python/01_clean_data.py` to sanitize raw data.
2. Run `python3 02_python/02_load_to_sql.py` to build the Star Schema and load data.
3. Access the `03_sql/uber_crm.db` to run the RFM views.

