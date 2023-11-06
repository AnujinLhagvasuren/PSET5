from PIL import Image
import streamlit as st

st.title('How do you feel today')

feeling = st.slider('How are you today?', 1, 10, 5)

if feeling >= 6:
    mood = "great"
elif feeling == 5:
    mood = "ok"
else:
    mood = "bad"




