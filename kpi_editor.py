import streamlit as st
import pandas as pd
import numpy as np



# Load the dataset
data_url = "https://raw.githubusercontent.com/grosz99/KPI_Editor/main/Sample_Superstore_Streamlit_Github.csv?token=GHSAT0AAAAAACMGXKXOJBA4EXP4MH4M3534ZM3DC5A"
df = pd.read_csv(data_url)
# Convert 'Order Date' to datetime format for consistent comparison
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 1: Filters
st.sidebar.header("Filters")

