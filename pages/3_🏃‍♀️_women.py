import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout='wide',
    page_title="Biegaczki",
    page_icon="🏃‍♀️"

)


def add_bg_from_url():
    st.sidebar.markdown(
        """
        <style>
        .css-cxvtz3 {
            background-image: url("https://i.guim.co.uk/img/media/c723050bc6abfe76f3774bfd3f1e058274e5b4dc/0_87_4000_2401/master/4000.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=f0e75c2dbf730c752e5b39f9c5a96779");
            background-attachment: fixed;
            background-size: 55%;
            background-position: calc(250px) calc(40% + 0px);
        }
        .css-cxvtz3::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.1);
            pointer-events: none;
        }
        .css-1oe5cao {
            background-color: rgba(255, 255, 255, 0.6);
        }
        .css-e3xfei {
            background-color: rgba(255, 255, 255, 0.6);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


add_bg_from_url()


def open_html(distance, name, height):
    file_path = f"./women/{distance}/{name}.html"
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    return components.html(source_code, height=height)


st.markdown("# Wyniki kobiet 🏃‍♀️")
st.sidebar.markdown("# Kobiety 🏃‍♀️")
tab100,  tab800, tab10000, tab_half_marathon,  tab_marathon = st.tabs(
    ["100m", "800m", "10000m", "pół_maraton", "maraton"])
with tab100:
    st.header("100m")
    with st.expander(label="Najlepszy czas w danym roku", expanded=False):
        open_html("100", "best_of_every_season", 800)
    with st.expander(label="Wiatr a czas", expanded=False):
        open_html("100", "wind", 800)
    with st.expander(label="Kraje a liczba rekordów", expanded=False):
        open_html("100", "country_bubbles", 800)
    with st.expander(label="PB a wiek", expanded=False):
        open_html("100", "personal_best_graph", 800)
with tab800:
    st.header("800m")
    with st.expander(label="Top 10 - liczba najlepszych wyników na 800m według kraju", expanded=False):
        open_html("800", "top_10_countries", 800)
    with st.expander(label="Progresja rekordów świata", expanded=False):
        open_html("800", "WR_progression", 800)
with tab10000:
    st.header("10000m")
    with st.expander(label="Top 10 - liczba najlepszych wyników na 10000m według kraju", expanded=False):
        open_html("10000", "top_10_countries", 800)
    with st.expander(label="Progresja rekordów świata", expanded=False):
        open_html("10000", "WR_progression", 800)
with tab_half_marathon:
    st.header("Półmaraton")
with tab_marathon:
    st.header("Maraton")
    with st.expander(label="Najlepszy czas w danym roku", expanded=False):
        open_html("marathon", "best_of_every_season", 800)
    with st.expander(label="Progresja rekordów świata", expanded=False):
        open_html("marathon", "WR_progression", 800)
    with st.expander(label="Liczba biegaczy a kraje", expanded=False):
        open_html("marathon", "Runners_per_country", 800)
    with st.expander(label="PB a wiek", expanded=False):
        open_html("marathon", "personal_best_graph", 800)
