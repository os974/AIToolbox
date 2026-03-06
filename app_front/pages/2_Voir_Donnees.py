import os

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("📋 Consulter les données")

# L'URL de ton API FastAPI est maintenant définie dans une variable d'environnement .env
# API_URL = "http://127.0.0.1:8000/donnees"

API_URL = os.getenv("API_URL", "http://localhost:8000")
# Utilise ensuite API_URL dans tes requêtes requests.get/post

try:
    # On récupère les données de l'API
    # response = requests.get(API_URL)
    response = requests.get(f"{API_URL}/donnees")

    if response.status_code == 200:
        data = response.json()

        if data:
            # On affiche les données dans un joli tableau
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("La base de données est vide pour le moment.")
    else:
        st.error("Erreur lors de la récupération des données.")

except Exception as e:
    st.error(f"❌ Impossible de contacter l'API : {e}")

if st.button("Actualiser"):
    st.rerun()
