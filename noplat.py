import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Sistem Kenderaan Asrama", layout="centered")

FILE = "data_kenderaan.csv"

# Jika fail belum wujud, cipta
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Nama Murid", "No Plat", "Tarikh"])
    df.to_csv(FILE, index=False)

# =========================
# BORANG IBU BAPA
# =========================
st.title("🚗 Makluman Kenderaan Murid Asrama")

with st.form("borang_kenderaan"):
    nama = st.text_input("Nama Murid")
    plat = st.text_input("No Plat Kenderaan")
    hantar = st.form_submit_button("Hantar")

    if hantar:
        if nama and plat:
            tarikh = datetime.now().strftime("%d/%m/%Y")  # TARIKH SAHAJA

            data_baru = pd.DataFrame(
                [[nama, plat.upper(), tarikh]],
                columns=["Nama Murid", "No Plat", "Tarikh"]
            )

            data_baru.to_csv(FILE, mode="a", header=False, index=False)
            st.success("Maklumat berjaya dihantar. Terima kasih.")
        else:
            st.warning("Sila lengkapkan semua maklumat.")

st.divider()

# =========================
# PAPARAN GUARD
# =========================
st.header("👮‍♂️ Paparan Guard")

df = pd.read_csv(FILE)

carian = st.text_input("Cari No Plat")

if carian:
    paparan = df[df["No Plat"].str.contains(carian.upper(), na=False)]
else:
    paparan = df

st.dataframe(paparan, use_container_width=True)
