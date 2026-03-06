import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("➕ Ajouter des données")

# L'URL de ton API FastAPI est maintenant définie dans une variable d'environnement .env
# API_URL = "http://127.0.0.1:8000/donnees"

API_URL = os.getenv("API_URL", "http://localhost:8000")
# Utilise ensuite API_URL dans tes requêtes requests.get/post


with st.form("form_ajout"):
    nom = st.text_input("Nom de l'élément")

    # MODIFICATION ICI : On utilise number_input pour envoyer un nombre (float)
    valeur = st.number_input("Valeur numérique", value=0.0, step=0.1)

    submit = st.form_submit_button("Envoyer à l'API")

if submit:
    if nom:
        # On prépare les données pour l'API
        # 'valeur' est maintenant bien un nombre grâce à number_input
        payload = {"nom": nom, "valeur": valeur}

        # Envoi de la requête POST
        try:
            # response = requests.post(API_URL, json=payload)
            response = requests.post(f"{API_URL}/donnees", json=payload)
            if response.status_code == 200:
                st.success(f"✅ Succès ! L'élément '{nom}' a été ajouté.")
            else:
                # On affiche le message d'erreur de l'API pour debug
                st.error(f"❌ Erreur API : {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"❌ Impossible de contacter l'API : {e}")
    else:
        st.warning("Le nom est obligatoire !")
