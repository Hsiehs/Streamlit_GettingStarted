import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Education", page_icon="🏫")

st.markdown("# Education 🏫")
st.sidebar.header("Education 🏫")
st.markdown(
    """
    My Education was not the normal one, It took me a while to figure out what I wanted to do.
    Once I did, I didnt get accepted to the school I wanted to transfer to, so I stayed at BC to purse their CS Degree.
    After a year I reapplied to UWB and got in, which meant I need to retake a years worth of CS courses.
    ### Bellevue College
    - Associates in Arts and Science
    - 2017-2022
    ### University of Washington, Bothell Campus
    - Bachelors of Science - Computer Science and Software Engineering
    - 2022-2024
    """
)


status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)



