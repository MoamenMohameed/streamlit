import streamlit as st

st.set_page_config(
    page_title="Shape Calculation",
    page_icon="📐",
    layout="wide"
)

st.header("Shapes Calculations")


shape = st.selectbox("choose from menu" , ["","Rectangle", "Circle"])


if shape == "Circle" :
    radius = st.number_input("Radius" , min_value=0.0, max_value=100.0 , step=0.01)
    area = radius * radius * 3.14
    perimeter = 2 * 3.14 * radius

if shape == "Rectangle" :
    width = st.number_input('Width' , 0.0 , step=0.1)
    height = st.number_input('Height' , 0.0 , step=0.1)
    area = width * height
    perimeter = 2 * (width + height)

btn = st.button("Calc") 
if(btn):
    with st.spinner("calculating...."):
        st.write("Area is = :",area)
        st.write("perimeter is = :",perimeter)
