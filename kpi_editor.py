import streamlit as st
import pandas as pd
import numpy as np



# Load the dataset
data_url = "https://raw.githubusercontent.com/grosz99/KPI_Editor/main/Sample_Superstore_Streamlit_Github.csv?token=GHSAT0AAAAAACMGXKXO3WEEIFUXUQZEMC5CZM3DKZQ"
df = pd.read_csv(data_url)
# Convert 'Order Date' to datetime format for consistent comparison
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 1: Filters
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start Ship Date", df['Order Date'].min().date())
end_date = st.sidebar.date_input("End Ship Date", df['Order Date'].max().date())
# Convert the Streamlit dates to datetime64[ns] format
start_date_np = np.datetime64(start_date)
end_date_np = np.datetime64(end_date)

filtered_df = df[(df['Order Date'] >= start_date_np) & (df['Order Date'] <= end_date_np)]

# Step 2: Data Validation & Editing
st.header("Validate values and you can change them if they are not right")
st.data_editor(filtered_df)

# Step 3: Chart Creator
st.header("Chart Creator (Click On Fields To Create Charts)")
fields = ["City", "State", "Region", "Sales", "Quantity", "Profit"]
selected_field = st.selectbox("Select Field to Visualize", fields)

if selected_field in ["City", "State", "Region"]:
    chart_data = filtered_df.groupby(selected_field)["Sales"].sum()
    st.bar_chart(chart_data)
elif selected_field in ["Sales", "Quantity", "Profit"]:
    st.line_chart(filtered_df[selected_field])
