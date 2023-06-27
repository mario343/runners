import streamlit as st

st.set_page_config(
    page_title="Biegacze",
    page_icon="🏃‍♂️"

)

tab100, tab200, tab400, tab800, tab1500, tab3000, tab5000, tab10000, tab_half_marathon, tab_marathon = st.tabs(
    ["100m", "200m", "400m", "800m", "1500m", "3000m", "5000m", "10000m", "half marathon", "marathon"])


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

with tab100:
    st.header("100m")
with tab200:
    st.header("100m")
with tab400:
    st.header("100m")
with tab800:
    st.header("100m")
