import streamlit as st
import pandas as pd
import numpy as np
import random

def weather(temp, wind, humidity):
  col1, col2, col3 = st.columns(3)
  tempString = str(temp) + " °F"
  windString = str(wind) + " MPH"
  humidityString = str(humidity) + " %"
  col1.metric("Temperature", tempString, "1.2 °F")
  col2.metric("Wind", windString, "-8%")
  col3.metric("Humidity", humidityString, "4%")


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to My Personal Homepage")

st.markdown(
    """
    My Name is Stanley Hsieh and I'm a Senior at The University of Washington, Bothell Campus, majoring in computer science and software enginneering.
    ### Want to learn more?
    - Check out the other pages on the sidebar
    """
)
temp = 70
wind = 9
humidity = 70
st.subheader("Today's Weather")
temp = random.randint(0, 90)
wind = random.randint(0, 25)
humidity = random.randint(25, 100)
weather(temp, wind, humidity)

st.button("Refresh")
  
