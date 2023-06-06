import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'Asia' : ['Singapore'],
    'lat' : [1.3521],
    'lon' : [103.8198]
})

st.map(data)