import streamlit as st
st.slider

feeling = st.slider('How are you today?', 1, 10, 5)

if feeling >=6:
    mood = "great"
elif feeling <=4:
    mood = "bad"
elif feeling == 5:
    mood = "ok"
    
st.write("I feel",mood)

from PIL import Image

st.image(Image.open(f'images/{mood}.jpg'))


