import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# @st.cache
data = {
    "Age": [18,22,35,50,62,77],
    "Income": [3500, 4700, 5360, 7500, 9550, 10500],
    "Sex" : ['M','F','F','M','M','F']
}
df = pd.DataFrame(data)

def main():
    page = st.sidebar.selectbox(
        "Select a page",
        [
            "Data",
            "Plots",
            "Machine Learning"

        ]
    )

    if page == "Data":
        st.balloons()
        st.header('A Linear Regression Program in Streamlit')
        st.write(df)
    elif page == "Plots":
        st.header('Plots of the data')
        make_plot()
        make_plot2()

def make_plot():
    fig = plt.figure()
    bar_data = df.sort_values(by="Income",ascending=False)
    plt.bar(bar_data["Age"],bar_data["Income"])
    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.title("Age vs Income")
    st.pyplot(fig)

def make_plot2():
    fig = plt.figure()
    bar_data = df.sort_values(by="Income",ascending=False)
    plt.bar(bar_data["Sex"],bar_data["Income"])
    plt.xlabel("Sex")
    plt.ylabel("Income")
    plt.title("Sex vs Income")
    st.pyplot(fig)


if __name__ == "__main__":
    main()