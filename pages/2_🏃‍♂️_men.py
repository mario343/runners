import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    layout='wide',
)


def add_bg_from_url():
    st.sidebar.markdown(
        """
        <style>
        .css-cxvtz3 {
            background-image: url("https://i2-prod.mirror.co.uk/incoming/article27267110.ece/ALTERNATES/s1200c/2_ATHLETICS-OLY-2016-RIO.jpg");
            background-attachment: fixed;
            background-size: 55%;
            background-position: calc(630px) calc(40% + 0px);
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


st.header("# Wyniki mężczyzn 🏃‍♂️")
st.sidebar.markdown("# Mężczyźni 🏃‍♂️")
tab100, tab200, tab400, tab800, tab1500, tab3000, tab5000, tab10000, tab_half_marathon, tab_marathon = st.tabs(
    ["100m", "200m", "400m", "800m", "1500m", "3000m", "5000m", "10000m", "half marathon", "marathon"])
with tab100:
    st.header("100m")
    with st.expander(label="Najlepszy czas w danym roku", expanded=False):
        best_time_yr = open(
            "./men/100/best_of_every_season.html", 'r', encoding='utf-8')
        source_code = best_time_yr.read()
        components.html(source_code, height=600)
    with st.expander(label="Progresja rekordów świata", expanded=False):
        wr = open("./men/100/WR_progression.html", 'r', encoding='utf-8')
        source_code = wr.read()
        components.html(source_code, height=600)
    with st.expander(label="Usain Bolt vs przeciętny człowiek", expanded=False):
        gif_file = "./men/100/animation.gif"
        st.image(gif_file, caption='GIF File', use_column_width=False)
    with st.expander(label="Wiatr a czas", expanded=False):
        Wind = open("./men/100/wind.html", 'r', encoding='utf-8')
        source_code = Wind.read()
        components.html(source_code, height=600)
    with st.expander(label="Kraje a liczba rekordów", expanded=False):
        bubbles = open("./men/100/country_bubbles.html", 'r', encoding='utf-8')
        source_code = bubbles.read()
        components.html(source_code, height=600)
    with st.expander(label="Liczba biegaczy a kraje", expanded=False):
        rnrs_per_country = open(
            "./men/100/Runners_per_country.html", 'r', encoding='utf-8')
        source_code = rnrs_per_country.read()
        components.html(source_code, height=800)
    with st.expander(label="PB a wiek", expanded=False):
        personal_best_graph = open(
            "./men/100/personal_best_graph.html", 'r', encoding='utf-8')
        source_code = personal_best_graph.read()
        components.html(source_code, height=600)
    with st.expander(label="Najlepsze wyniki sprinterów w zależności od wieku", expanded=False):
        heatmap = open("./men/100/heatmap.html", 'r', encoding='utf-8')
        source_code = heatmap.read()
        components.html(source_code, height=600)
with tab200:
    st.header("100m")

with tab400:
    st.header("100m")
with tab800:
    st.header("100m")
