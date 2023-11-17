import streamlit as st
import pandas as pd

try:
    dane_pkw = pd.read_excel("wyniki.xlsx")
    edited_df = st.data_editor(dane_pkw, num_rows="dynamic")
except Exception as e:
    st.header('Błąd wczytywania')
    st.subheader(f"{e=}")