import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Superstore Sales & Profit Dashboard")
st.write("Interactive analysis of sales, profit, orders, categories, and regions.")

# Load dataset
df = pd.read_csv("cleaned_superstore.csv")

# Sidebar filters
st.sidebar.header("🔎 Filters")

# Region filter
regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

# Category filter
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Apply filters
filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# Key metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
average_discount = filtered_df["Discount"].mean()

# Display metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Discount", f"{average_discount:.2%}")

st.divider()

# Sales by Category
st.subheader("📦 Sales by Category")

category_sales = (
    filtered_df.groupby("Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Total Sales by Category",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

# Profit by Region
st.subheader("🌎 Profit by Region")

region_profit = (
    filtered_df.groupby("Region", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit", ascending=False)
)

fig2 = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    title="Total Profit by Region",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

# Sales by Segment
st.subheader("👥 Sales by Customer Segment")

segment_sales = (
    filtered_df.groupby("Segment", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig3 = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    title="Sales Distribution by Customer Segment"
)

st.plotly_chart(fig3, use_container_width=True)

# Discount vs Profit
st.subheader("💰 Discount vs Profit")

fig4 = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category",
    title="Relationship Between Discount and Profit",
    hover_data=["Product Name", "Sales"]
)

st.plotly_chart(fig4, use_container_width=True)

# Data table
st.subheader("📋 Filtered Data")

st.dataframe(filtered_df, use_container_width=True)