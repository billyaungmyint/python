import streamlit as st
import settings


st.set_page_config(page_title="Info", page_icon="")

st.markdown("Information Page")
st.sidebar.header("Info Page")

st.write("This is info page!")
st.write(settings.PI)