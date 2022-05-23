import streamlit as st
import streamlit_option_menu

st.set_page_config(
    page_title="Site_with_Artur",
    page_icon="Envelope"
)

nav = option_menu(
    menu_title=None,
    options=["Home", "Project", "Contacts"],
    icons=["house", "calculator-fill", "envelope"],
    default_index=0,
    orientation="horizontal"
)

heading = st.container()
text = st.container()

with heading:
    st.snow()
    st.title("Welcome")

with text:
    st.write("Hakob is gay!")
