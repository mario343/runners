import streamlit as st

st.set_page_config(
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


st.markdown("# Wyniki kobiet 🏃‍♀️")
st.sidebar.markdown("# Kobiety 🏃‍♀️")
