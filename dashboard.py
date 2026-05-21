import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Store Dashboard", layout="wide")

st.title("🛒 Store Analytics Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("sales_data.csv")

# ---------------- CLEAN ----------------
df.columns = df.columns.str.strip()

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filters")

product_filter = st.sidebar.multiselect(
    "Select Product",
    df["product_name"].unique(),
    default=df["product_name"].unique()
)

day_filter = st.sidebar.multiselect(
    "Select Day",
    df["day_of_week"].unique(),
    default=df["day_of_week"].unique()
)

filtered_df = df[
    (df["product_name"].isin(product_filter)) &
    (df["day_of_week"].isin(day_filter))
]

# ---------------- KPI METRICS ----------------
total_sales = filtered_df["total_amount (Rs.)"].sum()
total_qty = filtered_df["quantity_sold"].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"₹ {total_sales:,.0f}")
col2.metric("📦 Quantity Sold", total_qty)
col3.metric("🧾 Total Orders", total_orders)

st.divider()

# ---------------- TOP PRODUCTS ----------------
top_products = filtered_df.groupby("product_name")["quantity_sold"].sum().sort_values(ascending=False).head(10)

fig1 = px.bar(
    top_products,
    x=top_products.index,
    y=top_products.values,
    title="Top Selling Products",
    labels={"x": "Product", "y": "Quantity"}
)

st.plotly_chart(fig1, width="stretch")

# ---------------- SALES BY DAY ----------------
day_sales = filtered_df.groupby("day_of_week")["total_amount (Rs.)"].sum().reset_index()

fig2 = px.line(
    day_sales,
    x="day_of_week",
    y="total_amount (Rs.)",
    title="Sales by Day"
)

st.plotly_chart(fig2, width="stretch")

# ---------------- SIZE ANALYSIS ----------------
size_sales = filtered_df.groupby("size")["quantity_sold"].sum().reset_index()

fig3 = px.pie(
    size_sales,
    names="size",
    values="quantity_sold",
    title="Size Distribution"
)

st.plotly_chart(fig3, width="stretch")

st.success("Dashboard Loaded Successfully ✔")
