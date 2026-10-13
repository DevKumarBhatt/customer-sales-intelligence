# Customer Sales Intelligence Dashboard

An interactive sales analytics dashboard built with Python, Pandas, SQLite, Plotly, and Streamlit.

## Project Overview

The Customer Sales Intelligence Dashboard helps analyze sales performance, revenue, profitability, product performance, and regional trends through interactive charts and business metrics.

## Features

- **Sales KPIs:** Total orders, revenue, profit, and units sold.
- **Interactive Filters:** Filter data by region and product category.
- **Revenue Trends:** Analyze revenue over time.
- **Category Analysis:** Compare revenue across product categories.
- **Regional Analysis:** Evaluate revenue and profit by region.
- **Monthly Analysis:** Compare monthly revenue and profit.
- **Product Ranking:** Identify the top-performing products.
- **Profit Margin:** Calculate profit margin as a percentage.
- **CSV Export:** Download filtered sales records.
- **SQLite Database:** Store and retrieve sales records using SQL.

## Tech Stack

- Python
- Pandas
- NumPy
- SQLite and SQL
- Plotly
- Streamlit

## Project Structure

```text
customer-sales-intelligence/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── sales.csv
└── src/
    ├── analysis.py
    └── database.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-sales-intelligence.git
cd customer-sales-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## Learning Outcomes

This project demonstrates practical skills in data cleaning, data aggregation, KPI calculation, SQL database operations, interactive data visualization, and dashboard development.

## Future Improvements

- Larger real-world sales dataset
- Date-range filters
- Customer segmentation
- Advanced profitability analysis
- Cloud deployment

## Author

**Dev Kumar Bhatt**

Python | SQL | Data Analytics | Streamlit
