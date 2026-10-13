
import pandas as pd
from pathlib import Path


def load_sales_data():
    """Load the sales dataset from the data folder."""
    file_path = Path(__file__).resolve().parent.parent / "data" / "sales.csv"

    df = pd.read_csv(file_path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    # Calculate sales revenue and profit
    df["Revenue"] = df["Quantity"] * df["Unit_Price"]
    df["Cost"] = df["Quantity"] * df["Unit_Cost"]
    df["Profit"] = df["Revenue"] - df["Cost"]

    return df


def get_sales_summary(df):
    """Return key business performance metrics."""
    return {
        "Total Orders": int(df["Order_ID"].nunique()),
        "Total Revenue": float(df["Revenue"].sum()),
        "Total Profit": float(df["Profit"].sum()),
        "Total Units Sold": int(df["Quantity"].sum()),
        "Average Order Value": float(
            df.groupby("Order_ID")["Revenue"].sum().mean()
        ),
    }


def get_category_sales(df):
    """Calculate revenue by product category."""
    return (
        df.groupby("Category", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
    )


def get_region_sales(df):
    """Calculate revenue and profit by region."""
    return (
        df.groupby("Region", as_index=False)[["Revenue", "Profit"]]
        .sum()
        .sort_values("Revenue", ascending=False)
    )

def get_monthly_sales(df):
    """Calculate monthly revenue and profit."""
    monthly_df = df.copy()

    monthly_df["Month"] = (
        monthly_df["Order_Date"].dt.to_period("M").astype(str)
    )

    result = (
        monthly_df.groupby("Month", as_index=False)[["Revenue", "Profit"]]
        .sum()
        .sort_values("Month")
    )

    return result


def get_top_products(df, limit=5):
    """Rank products by total revenue."""
    result = (
        df.groupby("Product", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Units_Sold=("Quantity", "sum"),
        )
        .sort_values("Revenue", ascending=False)
    )

    return result.head(limit)


def get_profit_margin(df):
    """Calculate overall profit margin as a percentage."""
    revenue = df["Revenue"].sum()

    if revenue == 0:
        return 0.0

    return float(df["Profit"].sum() / revenue * 100)
