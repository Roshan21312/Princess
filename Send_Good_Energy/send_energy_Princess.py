import streamlit as st

st.title("My Dear Princess Sanmati !!")
st.write(
    "I know you were angry and now you are in No mood",
    "Here is some good energy, Sending you lots of energy and love"
)

col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider

with col2:
    st.image(r"Send_Good_Energy/baby-bear-brown.gif") 

Anddddd, Here's a good motivating energetic song for you
st.audio(r"Send_Good_Energy/Hall_Of_Fame.mp3")
