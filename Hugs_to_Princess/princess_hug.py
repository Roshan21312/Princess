import streamlit as st
import base64

st.set_page_config(layout="wide")

# VIDEO
with open("Hugs_to_Princess/bg.mp4", "rb") as f:
    video_data = f.read()

video_base64 = base64.b64encode(video_data).decode()


with open("Hugs_to_Princess/the-cats-love.gif", "rb") as f:
    gif_data = base64.b64encode(f.read()).decode()

# BACKGROUND
st.markdown(f"""
<style>

#bgvid {{
    position: fixed;
    top: 50%;
    left: 50%;

    min-width: 100%;
    min-height: 100%;

    width: auto;
    height: auto;

    transform: translate(-50%, -50%);

    object-fit: cover;

    z-index: -999;
}}

.stApp {{
    background: transparent;
}}

[data-testid="stAppViewContainer"] {{
    background: rgba(0,0,0,0.10);
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* Center content */

.center {{
    text-align: center;
}}

.big-text {{
    color: white;

    font-size: 35px;

    font-weight: 500;

    margin-top: 20px;

    text-shadow:
        2px 2px 15px rgba(0,0,0,0.9);
}}

</style>

<video autoplay muted loop playsinline id="bgvid">
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# SPACING
st.markdown("<br><br><br>", unsafe_allow_html=True)

# CENTERED GIF
st.markdown(f"""
<div style="
display:flex;
justify-content:center;
align-items:center;
width:100%;
margin-top:20px;
margin-bottom:10px;
">

<img
src="data:image/gif;base64,{gif_data}"
style="
border-radius:20px;
display:block;
margin:auto;
">

</div>
""", unsafe_allow_html=True)

# TEXT
st.markdown("""
<div class="center">
    <div class="big-text">
        A bigggg hug to you 💖
    </div>
</div>
""", unsafe_allow_html=True)
