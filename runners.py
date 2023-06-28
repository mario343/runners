import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    layout='wide',
    page_title="Main Page",
    page_icon="🏁")


def add_bg_from_url():
    st.sidebar.markdown(
        f"""
         <style>
         .css-cxvtz3 {{
            background-image: url("https://upload.wikimedia.org/wikipedia/commons/d/d2/Men_100m_final_1960_Olympics.jpg");
            background-attachment: fixed;
            background-size: cover;
           background-position: calc(1790px) calc(50%);
         }}
         .css-cxvtz3::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.1);
            pointer-events: none;
        }}
        .css-1oe5cao {{
            background-color: rgba(255, 255, 255, 0.6);


        }}
        .css-e3xfei {{
            background-color: rgba(255, 255, 255, 0.6);


        }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

# Main content
st.markdown("# Strona główna 🏁")
st.sidebar.markdown("# Strona główna ")
st.markdown(
    "Projekt z przedmiotu wizualizacja danych analizujący wyniki profesjonalnych biegaczy.")
st.markdown(
    "[Kliknij tutaj](http://www.alltime-athletics.com/index.html) aby odwiedzić stronę, z której pobrano dane.")
st.markdown(
    "Dane zawierają wszystkie oficjalne czasy (z zawodów aprobowanych przez IAAF), które są powyżej średniego czasu minimum olimpijskiego na dany dystans. ")

st.markdown("## Narzędzia użyte do projektu:")
st.markdown("""
- .streamlit
- .numpy
- .pandas
- .plotly
- .beautifulSoup
- .matplotlib
""")

rain(
    emoji="🏃‍♂️",
    font_size=34,
    falling_speed=8,
    animation_length="infinite",
)

footer = """<style>
.footer {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
}
</style>
<div class="footer">
    <p>Projekt stworzony przez: Mariusza Wilka, Jakuba Żuchowicza, Julie Zezule.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
