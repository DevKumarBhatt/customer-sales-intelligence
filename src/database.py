
import sqlite3
from pathlib import Path

import pandas as pd


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "sales.db"


def get_connection():
    """Create a connection to the SQLite database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database(df):
    """Create the sales table and load the dataset."""
    with get_connection() as connection:
        df.to_sql("sales", connection, if_exists="replace", index=False)


def fetch_sales_data():
    """Read sales records from SQLite using SQL."""
    query = "SELECT * FROM sales"

    with get_connection() as connection:
        df = pd.read_sql_query(query, connection)

    if not df.empty:
        df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    return df
