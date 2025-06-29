import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Kết nối SQL Server
server = 'localhost\\SQLSERVER1'
database = 'ElectricityETL'
driver = 'ODBC Driver 17 for SQL Server'
conn_str = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver={driver}'
engine = create_engine(conn_str)

# Cấu hình Streamlit
st.set_page_config(page_title="Electricity Dashboard", layout="wide")
st.title("🔌 Electricity Bill Dashboard")

# Tạo layout 2 cột
col1, col2 = st.columns(2)

# 1. Biểu đồ: Avg Bill by Number of People
query_people = """
SELECT num_people, COUNT(*) AS households, AVG(amount_paid) AS avg_bill
FROM electricity_bills
GROUP BY num_people
ORDER BY num_people
"""
df_people = pd.read_sql(query_people, engine)
fig_people = px.bar(
    df_people,
    x="num_people",
    y="avg_bill",
    text_auto=".2s",
    title="Avg Bill by Number of People"
)
fig_people.update_layout(xaxis_title="Number of People", yaxis_title="Avg Bill", xaxis_tickangle=0)
col1.plotly_chart(fig_people, use_container_width=True)

# 2. Biểu đồ: Avg Bill by House Size
query_area = """
SELECT
    CASE 
        WHEN housearea < 500 THEN 'Under 500 sqft'
        WHEN housearea BETWEEN 500 AND 1000 THEN '500 - 1000 sqft'
        ELSE 'Over 1000 sqft'
    END AS house_size,
    COUNT(*) AS households,
    AVG(amount_paid) AS avg_bill
FROM electricity_bills
GROUP BY
    CASE 
        WHEN housearea < 500 THEN 'Under 500 sqft'
        WHEN housearea BETWEEN 500 AND 1000 THEN '500 - 1000 sqft'
        ELSE 'Over 1000 sqft'
    END
ORDER BY house_size;
"""
df_area = pd.read_sql(query_area, engine)
fig_area = px.bar(
    df_area,
    x="house_size",
    y="avg_bill",
    text_auto=".2s",
    title="Avg Bill by House Size"
)
fig_area.update_layout(xaxis_title="House Size", yaxis_title="Avg Bill", xaxis_tickangle=0)
col2.plotly_chart(fig_area, use_container_width=True)

# Tạo dòng thứ 2
col3, col4 = st.columns(2)

# 3. Biểu đồ: Urban vs Rural
query_urban = """
SELECT is_urban, AVG(amount_paid) AS avg_bill
FROM electricity_bills
GROUP BY is_urban;
"""
df_urban = pd.read_sql(query_urban, engine)
df_urban["area"] = df_urban["is_urban"].map({1: "Urban", 0: "Rural"})
fig_urban = px.bar(
    df_urban,
    x="area",
    y="avg_bill",
    text_auto=".2s",
    title="Urban vs Rural Avg Bill"
)
fig_urban.update_layout(xaxis_title="Area Type", yaxis_title="Avg Bill", xaxis_tickangle=0)
col3.plotly_chart(fig_urban, use_container_width=True)

# 4. Biểu đồ: Avg Bill by Number of Children
query_children = """
SELECT num_children, COUNT(*) AS households, AVG(amount_paid) AS avg_bill
FROM electricity_bills
GROUP BY num_children
ORDER BY num_children;
"""
df_children = pd.read_sql(query_children, engine)
fig_children = px.bar(
    df_children,
    x="num_children",
    y="avg_bill",
    text_auto=".2s",
    title="Avg Bill by Number of Children"
)
fig_children.update_layout(xaxis_title="Number of Children", yaxis_title="Avg Bill", xaxis_tickangle=0)
col4.plotly_chart(fig_children, use_container_width=True)
