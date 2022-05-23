import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Site_with_Artur",
    page_icon="Envelope"
)

nav = option_menu(
    menu_title=None,
    options=["Home", "Hakob", "Artur"],
    icons = [None, None, None],
    default_index=0,
    orientation="horizontal"
)

heading = st.container()
text = st.container()

if nav == "Home":
    with heading:
        st.snow()
        st.title("Welcome")

if nav == "Hakob":
    with text:
        st.write("Hakob is gay!")

if nav == "Artur":
    st.balloons()
    with text:
        st.write("Artur is like deadpool.")
