import streamlit as st

from streamlit_gsheets import GSheetsConnection

try:
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    dane_pkw = conn.read()

    edited_df = st.data_editor(dane_pkw, num_rows="dynamic")
except Exception as e:
    st.header('Błąd wczytywania')
    st.subheader(f"{e=}")

def reload_datas():
    try:
        dane_pkw = conn.read()
        st.data_editor(dane_pkw, num_rows="dynamic")
    except Exception as e:
        st.header('Błąd reload')
        st.subheader(f"{e=}")

st.button("RELOAD", on_click="reload_datas")