
import streamlit as st
import plotly.express as px

from src.analysis import (
    load_sales_data,
    get_sales_summary,
    get_category_sales,
    get_region_sales,
)
from src.database import initialize_database, fetch_sales_data


st.set_page_config(
    page_title="Customer Sales Intelligence",
    page_icon="📊",
    layout="wide",
)
from src.analysis import (
    get_monthly_sales,
    get_top_products,
    get_profit_margin,
)

st.title("📊 Customer Sales Intelligence Dashboard")
st.caption("Analyze sales, profitability, products, and regional performance.")

# Load CSV and initialize the database
try:
    csv_df = load_sales_data()
    initialize_database(csv_df)
    df = fetch_sales_data()
except Exception as error:
    st.error(f"Unable to load sales data: {error}")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")

regions = sorted(df["Region"].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect(
    "Select regions",
    regions,
    default=regions,
)

categories = sorted(df["Category"].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect(
    "Select categories",
    categories,
    default=categories,
)

filtered_df = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
]

if filtered_df.empty:
    st.warning("No sales records match these filters.")
    st.stop()

# KPI metrics
summary = get_sales_summary(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", f"{summary['Total Orders']:,}")
col2.metric("Revenue", f"₹{summary['Total Revenue']:,.0f}")
col3.metric("Profit", f"₹{summary['Total Profit']:,.0f}")
col4.metric("Units Sold", f"{summary['Total Units Sold']:,}")

st.divider()

# Revenue trend
st.subheader("📈 Revenue Trend")

daily_sales = (
    filtered_df.groupby("Order_Date", as_index=False)["Revenue"].sum()
    .sort_values("Order_Date")
)

fig_trend = px.line(
    daily_sales,
    x="Order_Date",
    y="Revenue",
    markers=True,
    title="Revenue by Order Date",
)
st.plotly_chart(fig_trend, use_container_width=True)

# Category and regional analysis
left, right = st.columns(2)

with left:
    st.subheader("🏷️ Sales by Category")
    category_sales = get_category_sales(filtered_df)

    fig_category = px.bar(
        category_sales,
        x="Category",
        y="Revenue",
        color="Category",
        title="Category Revenue",
    )
    st.plotly_chart(fig_category, use_container_width=True)

with right:
    st.subheader("🌍 Regional Performance")
    region_sales = get_region_sales(filtered_df)

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Revenue",
        color="Region",
        title="Revenue by Region",
    )
    st.plotly_chart(fig_region, use_container_width=True)

# Detailed records
st.subheader("📋 Sales Transactions")
st.dataframe(
    filtered_df.sort_values("Order_Date", ascending=False),
    use_container_width=True,
    hide_index=True,
)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Filtered Sales CSV",
    data=csv_data,
    file_name="sales_report.csv",
    mime="text/csv",
)

st.caption("Built with Python, Pandas, SQLite, SQL, Plotly, and Streamlit.")

st.divider()

# Monthly Sales Analysis
st.subheader("📅 Monthly Sales & Profit Analysis")

monthly_sales = get_monthly_sales(filtered_df)

fig_monthly = px.bar(
    monthly_sales,
    x="Month",
    y=["Revenue", "Profit"],
    barmode="group",
    title="Monthly Revenue vs Profit",
)
st.plotly_chart(fig_monthly, use_container_width=True)

# Top Products
st.subheader("🏆 Top 5 Products by Revenue")

top_products = get_top_products(filtered_df)

fig_products = px.bar(
    top_products,
    x="Revenue",
    y="Product",
    orientation="h",
    color="Profit",
    title="Best Performing Products",
)
fig_products.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig_products, use_container_width=True)

# Profit Margin
profit_margin = get_profit_margin(filtered_df)

st.metric("Overall Profit Margin", f"{profit_margin:.2f}%")
