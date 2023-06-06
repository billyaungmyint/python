import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv('../../data/ted.csv')
    return df

df = load_data()

def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "Bar Plot",
            "Horizontal Bar Plot",
            "Scatter Plot"
        ]
    )

    if page == "Homepage":
        st.header("Data Application")
        '''
        ### Building App with Streamlit
        Please select a page
        '''
        st.balloons()
        st.write(df)
    elif page == "Bar Plot":
        bar_chart()
    elif page  =="Horizontal Bar Plot":
        horizontal_bar()
    elif page == "Scatter Plot":
        visualise_scatter()

def bar_chart():
    fig = plt.figure(figsize=(12,5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by='views' , ascending=False)
    bar_data = bar_data.head(20)
    plt.ticklabel_format(style="plain")
    plt.bar(bar_data['event'],bar_data['views'])
    plt.xlabel('Event')
    plt.ylabel('Views')
    plt.title('Event and View Plots')
    st.pyplot(fig)

def horizontal_bar():
    fig = plt.figure(figsize=(12,5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by='views' , ascending=False)
    bar_data = bar_data.head(20)
    plt.ticklabel_format(style="plain")
    # barh here not bar
    plt.barh(bar_data['event'],bar_data['views'])
    plt.xlabel('Event')
    plt.ylabel('Views')
    plt.title('Event and View Plots')
    st.pyplot(fig)

def visualise_scatter():
    fig = plt.figure(figsize=(10,8))
    plt.scatter(
        x = df['comments'],
        y = df['views'],
        marker='*',
        s = df['languages'],
        c = df['languages'],
        alpha = 0.5

    )
    plt.ticklabel_format(style="plain")
    plt.xlabel('Comments')
    plt.ylabel('Views')
    st.pyplot(fig)


if __name__ == '__main__':
    main()