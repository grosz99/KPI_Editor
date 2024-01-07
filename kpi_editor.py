import streamlit as st
import pandas as pd
import numpy as np
import pygwalker as pyg
import streamlit.components.v1 as components



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
st.header("Chart Creator")
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
