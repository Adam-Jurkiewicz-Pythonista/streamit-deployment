import streamlit as st

from streamlit_gsheets import GSheetsConnection

def reload_datas():
    conn = st.connection("gsheets", type=GSheetsConnection)
    dane_pkw = conn.read()
    edited_df = st.data_editor(dane_pkw, num_rows="dynamic")

try:
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    dane_pkw = conn.read()

    edited_df = st.data_editor(dane_pkw, num_rows="dynamic")
except Exception as e:
    st.header('Błąd wczytywania')
    st.subheader(f"{e=}")

st.button("RELOAD", on_click="reload_datas")