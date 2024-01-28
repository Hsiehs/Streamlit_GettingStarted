import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Hobbies", page_icon="🏂")

st.markdown("# Hobbies 🏂")
st.sidebar.header("Hobbies 🏂")
st.markdown(
    """
    In my free time I enjoy many different hobbies.
    ### Summer:
    - Riding my motorcycle
    - Anything outside to enjoy the sun
    ### Winter:
    - Snowboarding
    ### Year Round
    - Hanging out with friends
    - Playing video games
    - going to the gym
    """
)


status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)



