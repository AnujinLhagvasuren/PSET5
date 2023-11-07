import streamlit as st
from PIL import Image
st.title('How do you feel today')

feeling = st.slider('How are you today?', 1, 10, 5)

if feeling >= 6:
    mood = "great"
elif feeling == 5:
    mood = "ok"
else:
    mood = "bad"

st.write("I feel", mood)
image_path = f"images/{mood}.jpg"
st.image(Image.open(image_path))

if mood in mood_images:
    image_path = mood_images[mood]
    st.image(Image.open(image_path), caption=f'Your {mood} mood!')
else:
    st.error("Image not found for this mood")


if st.button("Refresh"):
    st.experimental_rerun()


if mood in mood_images:
    image_path = mood_images[mood]
    if os.path.exists(image_path):
        st.image(Image.open(image_path), caption=f'Your {mood} mood!')
    else:
        st.warning(f"Image not found for {mood} mood. Showing a placeholder image.")
        st.image("images/placeholder.jpg")
else:
    st.error("Image not found for this mood")

feeling = st.slider('How are you today?', 1, 10, 5, format="%d/10")

mood_descriptions = {
    "great": "Feeling fantastic today!",
    "ok": "Having an average day.",
    "bad": "Not feeling my best."
}

# ...

st.write("I feel", mood)
if mood in mood_descriptions:
    st.write(mood_descriptions[mood])
    
mood_images = {
    "great": "images/great.jpg",
    "ok": "images/ok.jpg",
    "bad": "images/bad.jpg",
    "awful": "images/awful.jpg",
    # Add more moods and corresponding image paths here
}

st.title('How do you feel today')
st.markdown("<p style='text-align: center;'>Use the slider to indicate your mood</p>", unsafe_allow_html=True)
st.sidebar.markdown("Welcome to the Mood Analyzer")
st.markdown("<style>body { background-color: #f2f2f2; }</style>", unsafe_allow_html=True)





