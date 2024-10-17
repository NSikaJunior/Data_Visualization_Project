import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fr-en-reussite-au-baccalaureat-origine-sociale.csv", encoding="utf-8", delimiter=';')

st.sidebar.title("Sommaire")

pages = ["Contexte du projet", "Exploration des données", "Analyse de données", "Modélisation"]

page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0] :

    # Streamlit app
    st.title("Réussite au baccalauréat selon l’origine sociale")

    # Choix des colonnes
    colonne_x = st.selectbox("Axe X", df.columns, index=1)
    colonne_y = st.selectbox("Axe Y", df.columns, index=3)
    colonne_ventilation = st.selectbox("Ventiler les séries", df.columns, index=2)

    df = df.sort_values(by=[colonne_x, colonne_y])

    # Créer le graphique
    fig = px.line(df,
                  x=colonne_x, y=colonne_y, color=colonne_ventilation, width=1000, markers=True)

    # Afficher le graphique
    st.plotly_chart(fig)
