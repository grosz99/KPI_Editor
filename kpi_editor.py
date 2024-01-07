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
start_date = st.sidebar.date_input("Start Ship Date", df['Order Date'].min().date())
end_date = st.sidebar.date_input("End Ship Date", df['Order Date'].max().date())
# Convert the Streamlit dates to datetime64[ns] format
start_date_np = np.datetime64(start_date)
end_date_np = np.datetime64(end_date)

filtered_df = df[(df['Order Date'] >= start_date_np) & (df['Order Date'] <= end_date_np)]

# Step 2: Data Validation & Editing
st.header("Validate values and you can change them if they are not right")
if st.checkbox("Edit Data"):
    # Example: Allow editing the 'Sales' for a specific city
    cities = filtered_df['City'].unique()
    selected_city = st.selectbox("Select City to Edit", cities)
    city_data = filtered_df[filtered_df['City'] == selected_city]
    
    # Display data for the selected city
    st.dataframe(city_data[['City', 'State', 'Region', 'Sales', 'Quantity', 'Profit']])
    
    # Allow editing sales for the selected city
    new_sales = st.number_input(f"Edit Sales for {selected_city}", value=city_data['Sales'].mean())
    if st.button("Update Sales"):
        filtered_df.loc[filtered_df['City'] == selected_city, 'Sales'] = new_sales
        st.success(f"Sales for {selected_city} updated successfully!")

st.write(filtered_df)

if __name__ == "__main__":
    st.run()
