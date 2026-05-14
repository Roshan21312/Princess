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



# LOAD AUDIO
import streamlit.components.v1 as components

# LOAD AUDIO
with open("Hugs_to_Princess/phir_kabhi.mp3", "rb") as f:
    audio_data = f.read()

audio_base64 = base64.b64encode(audio_data).decode()

components.html(
    f"""
    <style>

    body {{
        margin: 0;
        overflow: hidden;
    }}

    @keyframes pulse {{

         0% {{
             box-shadow: 0 0 12px rgba(255,105,180,0.5);
         }}

         50% {{
             box-shadow: 0 0 40px rgba(255,182,193,1);
         }}

         100% {{
             box-shadow: 0 0 12px rgba(255,105,180,0.45);
         }}
     }}

    @keyframes spin{{
        from {{
            rotate: 0deg;
        }}
        to {{
            rotate: 360deg;
        }}
    }}

    .rotate{{
        animation:
            spin 5s linear infinite,
            pulse 2s ease-in-out infinite;
    }}

    


    .music-container {{

        position: absolute;

        left: 50%;

        transform: translateX(-50%);

        margin-top: 15px;
    }}

    #music-btn {{

        width: 65px;
        height: 65px;

        border-radius: 50%;

        border: none;

        background: rgba(255,105,180,0.88);

        color: white;

        font-size: 28px;

        cursor: pointer;

        z-index: 999999;

        animation: pulse 2s infinite;

        box-shadow:
            0 0 20px rgba(255,105,180,0.6);

        transition: 0.3s ease;
    }}

    #music-btn:hover {{
        scale: 1.08;
    }}

    </style>

    <div class="music-container">
        <button id="music-btn">🎵</button>
    </div>

    <audio id="bg-audio" loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>

    <script>

    const btn = document.getElementById("music-btn");
    const audio = document.getElementById("bg-audio");

    let playing = false;

    btn.addEventListener("click", () => {{

        if (!playing) {{

            
            audio.volume = 0.5;
            audio.play();

            playing = true;

            btn.style.animation=
            "spin 5s linear infinite, pulse 2s ease-in-out infinite";


        }} else {{

            audio.pause();

            playing = false;

            btn.style.animation = "pulse 2s infinite";
        }}

    }});

    </script>
    """,
    height=100,
)
