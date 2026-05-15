import streamlit as st
import base64

st.set_page_config(layout="wide")

# VIDEO
with open("bg.mp4", "rb") as f:
    video_data = f.read()

video_base64 = base64.b64encode(video_data).decode()


with open("drink-water-have-a-drink.gif", "rb") as f:
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

    font-size: 30px;

    font-weight: 500;

    margin-top: 15px;

    text-shadow:
        2px 2px 15px rgba(0,0,0,0.9);
}}

</style>

<video autoplay muted loop playsinline id="bgvid">
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
""", unsafe_allow_html=True)


# CENTERED GIF
st.markdown(f"""
            
<style>
        .wrap{{
            margin-top:-100px;
        }}    
</style>

<div class='wrap'>
<div style="
display:flex;
justify-content:center;
align-items:center;
width:100%;
margin-top:0 px;
margin-bottom:0px;
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
        Stay Hydrated my Princess <br>
            (with a Crown & a Palace)
    </div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><br>",unsafe_allow_html=True)

with open("thirsty-shogo.gif", "rb") as f:
    gif_data2 = base64.b64encode(f.read()).decode()

st.markdown(f"""
<div style="
display:flex;
justify-content:center;
align-items:center;
width:100%;
margin-top:15px;
margin-bottom:10px;
">

<img
src="data:image/gif;base64,{gif_data2}"
style="
border-radius:20px;
display:block;
margin:auto;
">

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="center">
    <div class="big-text">
            Aise hi paani peete rehna itna saara... 😅(hehehe)
    </div>
</div>
""", unsafe_allow_html=True)

