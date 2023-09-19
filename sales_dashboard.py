"""StreamLit Sales Dashboard
This script will create a StreamLit app to visualize sales data.
"""

# Imports
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Connect to the data warehouse (SQLite database)
conn_data_warehouse = sqlite3.connect("warehouse.db")


# Create a Streamlit app
st.title("Sales Dashboard")


# Add tabs to the app
tabs = st.sidebar.radio(
    "Select a Tab:", ("Sales Trends", "Product Performance"))

if tabs == "Sales Trends":
    # Tab 1: Sales Trends
    st.header("Sales Trends")

    # Load data from the data warehouse
    sales_data = pd.read_sql_query(
        "SELECT * FROM warehouse", conn_data_warehouse)

    # Display a table with sales data
    st.write("Sales Data:")
    st.write(sales_data)

    # Create a line chart to visualize sales trends
    st.subheader("Sales Trends Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=sales_data, x="sale_date", y="quantity", ax=ax)
    st.pyplot(fig)

elif tabs == "Product Performance":
    # Tab 2: Product Performance
    st.header("Product Performance")

    # Load data from the data warehouse
    product_data = pd.read_sql_query(
        "SELECT * FROM Products", conn_data_warehouse)

    # Display a table with product data
    st.write("Product Data:")
    st.write(product_data)

    # Create a bar chart to visualize product sales
    st.subheader("Product Sales")
    fig, ax = plt.subplots()
    sns.barplot(data=product_data, x="name", y="price", ax=ax)
    ax.set_xlabel("Product")
    ax.set_ylabel("Price")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                       horizontalalignment='right')
    st.pyplot(fig)


# Close the data warehouse connection
conn_data_warehouse.close()
