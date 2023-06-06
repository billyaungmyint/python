import pandas as pd
import streamlit as st

# import iris.csv
df = pd.read_csv('LearnStreamlit\\Module01\\iris.csv')

# Method 1
# st.dataframe(df ,200,100)
# st.dataframe(df)
# high max values in each column
st.dataframe(df.style.highlight_max(axis = 0))

# Mthod 2 : static table - not good for huge data
# st.table(df)

# Method 3
st.write(df.head())