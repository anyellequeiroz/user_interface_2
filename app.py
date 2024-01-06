import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Hello")

st.markdown("# Streamlit is awesome")

query = st.text_input("What is your name?")
st.write('Hello ', query)


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

@st.cache
def get_slider_data():

    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

df = get_slider_data()

option = st.slider('Select a modulus', 1, 10, 3)

filtered_df = df[df['first column'] % option == 0]

st.write(filtered_df)


@st.cache
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)
