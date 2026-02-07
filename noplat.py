import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Makluman Kenderaan Asrama")

st.title("🚗 Makluman Kenderaan Murid Asrama")

nama = st.text_input("Nama Murid")
plat = st.text_input("No Plat Kenderaan")

if st.button("Hantar"):
    if nama and plat:
        masa = datetime.now().strftime("%d/%m/%Y %H:%M")
        data = pd.DataFrame([[nama, plat, masa]],
                            columns=["Nama Murid", "No Plat", "Masa"])

        if os.path.exists("data.csv"):
            data.to_csv("data.csv", mode="a", header=False, index=False)
        else:
            data.to_csv("data.csv", index=False)

        st.success("Maklumat berjaya dihantar ✅")
    else:
        st.warning("Sila isi semua maklumat")

st.divider()

st.subheader("👮 Paparan Guard")
if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
    carian = st.text_input("Cari No Plat")
    if carian:
        st.dataframe(df[df["No Plat"].str.contains(carian, case=False)])
    else:
        st.dataframe(df)
