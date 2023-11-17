import streamlit as st
import pandas as pd

dane_pkw = pd.read_excel("datas/wyniki_gl_na_listy_po_obwodach_proc_sejm_utf8.xlsx")

edited_df = st.data_editor(dane_pkw, num_rows="dynamic")