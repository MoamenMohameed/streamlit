import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Data Visualization",
    page_icon="📉",
    layout="wide"
)
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload File", type="csv")



if file is not None: 
    df = load_data(file)

    rows = st.slider("Chosse number of rows", min_value=5, max_value=len(df) , step=1)

    columns = st.multiselect("Select Columns to Show" , df.columns.to_list() , default=df.columns.to_list())
    st.write(df[:rows][columns]) 


    numerical_col = df.select_dtypes(include=np.number).columns.to_list()
    col1 , col2, col3, col4 = st.columns(4)
    with col1:
        x_cols = st.selectbox("Select Column on X Axis:" , numerical_col)
    with col2:
        y_cols = st.selectbox("Select Column on Y Axis:" , numerical_col)
    with col3:
        color = st.selectbox("Select Column to be Color" , df.columns)
    with col4:
        size = st.selectbox("Select Column to be Size" , df.columns)


    tab1,tab2 = st.tabs(["Scatter Plot", "Histogram"])
    with tab1:
        scat = px.scatter(df , x = x_cols , y = y_cols , color=color , size=size)
        st.plotly_chart(scat)
    with tab2:
        hist = px.histogram(df ,x = x_cols)
        st.plotly_chart(hist)