import streamlit as st
# We need to import the streamlit library as first

st.set_page_config(
    page_title="My application for DV4S",
    layout="wide",
    initial_sidebar_state="expanded" # So it is open the menu
)

# Title
st.title("🎈 My new app")

# Text and writer
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Data
value = st.slider("Select a specific value: ", 0, 100, 40)
# The values are in order the minimum, the maximum and the actual value of the slider

# To write the value of the slider (at screen)
st.write("You selected: ", value)