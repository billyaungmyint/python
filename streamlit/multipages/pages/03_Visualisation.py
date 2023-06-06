import streamlit as st

def home_page():
    st.markdown("# Home Page 3")
    # st.sidebar.markdown("# Main page 🎈")

def data():
    st.markdown("# Data 3")
    # st.sidebar.markdown("# Page 2 ❄️")

def visualisation():
    st.markdown("# Visualisation 3")
    # st.sidebar.markdown("# Page 3 🎉")

def statistics():
    st.markdown("# Statistics 3")
    # st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Home Page": home_page,
    "Data": data,
    "Visualisation": visualisation,
    "Statistics": statistics,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()