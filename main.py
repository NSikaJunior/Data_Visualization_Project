import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fr-en-reussite-au-baccalaureat-origine-sociale.csv", encoding="utf-8", delimiter=';')

st.sidebar.title("Sommaire")

pages = ["Contexte du projet", "Exploration des données", "Analyse de données", "Modélisation"]

page = st.sidebar.radio("Aller vers la page :", pages)


if page == pages[0]:

    # Streamlit app
    st.title("Réussite au baccalauréat selon l’origine sociale")

    # Choix des colonnes
    df_dropped = df.drop(columns=["num_ligne"])
    colonne_x = "Année"
    colonne_y = st.selectbox("Axe Y (Figure 1)", df_dropped.columns, index = 2)
    colonne_ventilation = "Origine sociale"

    df_dropped = df_dropped.sort_values(by=[colonne_x, colonne_y])
    fig = px.line(df_dropped, x=colonne_x, y=colonne_y, color=colonne_ventilation, width=1000, markers=True,
                  title="Figure 1 : Evolution des réussites au baccalaureat dans le temps")

    # Afficher le graphique
    st.plotly_chart(fig)

    if st.checkbox("Interprétation figure 1"):
        interpretation = None
        st.write("Interprétation figure 1")


elif page == pages[1]:

    st.title("Réussite au baccalauréat selon l’origine sociale")

    # Pourcentage moyen de réussite au baccalauréat pour chaque origine sociale
    colonne_x = "Origine sociale"
    colonne_y = "Pourcentage d'admis au baccalauréat"
    mean_success = df.groupby(colonne_x)[colonne_y].mean().reset_index()
    fig2 = px.bar(mean_success,
                  x=colonne_x, y=colonne_y, color=colonne_x, width=1000,
                  title="Figure 2 : Pourcentage moyen de réussite au baccalauréat pour chaque origine sociale")

    # Afficher le graphique
    st.plotly_chart(fig2)

    if st.checkbox("Interprétation figure 2"):
        st.write("Interprétation figure 2")
