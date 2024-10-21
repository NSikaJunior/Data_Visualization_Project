import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

df = pd.read_csv("fr-en-reussite-au-baccalaureat-origine-sociale.csv", encoding="utf-8", delimiter=';')
df_prediction2 = pd.read_csv("fr-en-reussite-bac-plus-prevision-2025-to-2030.csv")

st.sidebar.title("Sommaire")

pages = ["Introduction", "Présentation du dataset", "Tendances et idées à mettre en avant", "Exploration et analyse "
                                                                                            "des données I",
         "Exploration et analyse des données II",
         "Prédiction 2024-2030", "Conclusion"]
page = st.sidebar.radio("Aller vers la page :", pages)


def plot_evolution(dataframe: pd.DataFrame, num_figure: int, paragraphs, interpretation=True) -> None:
    df_dropped = dataframe.drop(columns=["num_ligne"])
    colonne_x = "Année"
    colonne_y = st.selectbox(f"Axe Y (Figure {num_figure})", df_dropped.columns, index=2)
    colonne_ventilation = "Origine sociale"

    df_dropped = df_dropped.sort_values(by=[colonne_x, colonne_y])
    fig = px.line(df_dropped, x=colonne_x, y=colonne_y, color=colonne_ventilation, width=1000, markers=True,
                  title=f"Figure {num_figure} : Evolution des réussites au baccalaureat dans le temps")

    # Afficher le graphique
    st.plotly_chart(fig)

    if interpretation:
        if st.checkbox(f"Interprétation figure {num_figure}"):
            for key, val in paragraphs.items():
                if df_dropped.columns.tolist().index(colonne_y) == key:
                    for paragraph in paragraphs[key]:
                        st.write(f"""{paragraph}""")


if page == pages[0]:

    st.title("Réussite au baccalauréat selon l’origine sociale")

    st.write("""## Introduction""")

    # open method used to open different extension image file
    intro_im = Image.open(r"./img/dataviz.jpg")
    st.image(intro_im)

    st.write("Ce projet s'intéresse à l'influence de l'origine sociale sur la réussite"
             " au baccalauréat en France. J'utilise le dataset \"Réussite au baccalauréat selon l’origine sociale\" "
             "que j'ai trouvé sur le site data.education.gouv.fr. J'ai choisi ce dataset car il permet d'analyser "
             "l'impact des inégalités sociales sur la performance scolaire, un sujet crucial "
             "dans le contexte de l'éducation et de l'équité sociale. Les données couvrent p"
             "lusieurs années et trois types de baccalauréats : général, technologique"
             " et professionnel. L'objectif est de voir comment les élèves issus de différentes"
             " classes sociales réussissent ces examens, et d'observer les tendances au fil du temps.")


if page == pages[1]:
    st.title("Présentation du dataset")

    st.write("324 lignes et 11 colonnes")

    st.dataframe(df.head())

if page == pages[2]:
    st.title("Tendances et idées à mettre en avant")

    st.write("""
        À travers ce projet, je cherche à mettre en lumière les questions suivantes :
        
        1. Les élèves issus de classes sociales favorisées ont-ils de meilleurs taux de réussite que ceux issus de milieux défavorisés ?
        2. Quelle est l'évolution de la réussite au baccalauréat pour les différentes classes sociales sur plusieurs années ?
        3. Existe-t-il des différences marquées entre les types de baccalauréats en fonction de l'origine sociale ?"""
             )

if page == pages[3]:

    # Streamlit app
    st.title("Exploration et analyse des données")

    plot_evolution(df, 1, {2: ["Les enfants de cadres et de professions intellectuelles "
                               "supérieures sont, de manière générale, plus nombreux à "
                               "réussir le baccalauréat général. Leur courbe est la plus élevée et "
                               "suit une progression croissante régulière.",
                               "Les enfants d'ouvriers et d'employés, d'agriculteurs et autres professions "
                               "intermédiaires sont moins nombreux à réussir"
                               "le baccalauréat. Leurs courbes sont plus stables, avec une "
                               "progression moins marquée."
                               ],
                           3: ["Malgré cette tendance à la hausse, les écarts de réussite entre les différentes "
                               "catégories sociales persistent. Les enfants issus de milieux socio-économiques "
                               "favorisés (cadres, professions intellectuelles supérieures) ont toujours des taux de "
                               "réussite supérieurs à ceux des enfants d'ouvriers ou d'employés.",
                               "Si les écarts demeurent, on observe une tendance à leur réduction au fil des années. "
                               "Cette évolution suggère une amélioration de l'égalité des chances dans l'accès au "
                               "baccalauréat général."],
                           4: ["Ce graphique montre le nombre d'admis au baccalauréat technologique par origine "
                               "sociale. Les professions intermédiaires (instituteurs et assimilés), les cadres, "
                               "et les retraités sont les principales catégories étudiées.",
                               "On observe une baisse générale du nombre d'admis au fil des années (depuis les années "
                               "2000) dans presque toutes les catégories sociales, avec une légère remontée vers 2020.",
                               "Cela pourrait indiquer une réduction de l'attractivité ou de l'accès au baccalauréat "
                               "technologique, particulièrement pour certaines catégories professionnelles."],
                           5: ["Ce graphique présente le pourcentage d'admis au bac technologique, ce qui donne une "
                               "vision relative par rapport à l'ensemble des inscrits.",
                               "Contrairement au nombre absolu, le pourcentage de réussite au baccalauréat "
                               "technologique semble avoir globalement augmenté pour toutes les origines sociales "
                               "entre les années 2000 et 2020. Après une montée significative entre 2005 et 2015, "
                               "il y a une légère baisse vers 2020.",
                               "Cette tendance montre qu'en proportion, le baccalauréat technologique reste "
                               "accessible à une grande partie des catégories sociales, malgré la baisse du nombre "
                               "total d'admis."],
                           6: ["Le baccalauréat professionnel a été particulièrement populaire au début des années "
                               "2010, mais le nombre d'admis a diminué par la suite.",
                               "Les professions intermédiaires, les ouvriers, et les employés sont les catégories "
                               "sociales qui semblent le plus bénéficier de ce type de baccalauréat."],
                           7: ["Les taux de réussite au baccalauréat professionnel varient selon l'origine sociale. "
                               "Certaines catégories, comme les enfants d'agriculteurs exploitants, de cadres et de "
                               "professions intellectuelles. ",
                               "On observe aussi deux pics en 2008 et en 2020 pour toutes "
                               "les origines sociales. Ces pics marquent une forte augmentation du taux de réussite au "
                               "bac professionnel suivie d'une baisse toute aussi forte de ce taux. Le pic de 2020 "
                               "pourrait pet-être être expliqué par la COVID-19."
                               "supérieures, montrent des taux plus élevés"],
                           8: ["Le nombre total d'admis au baccalauréat a globalement augmenté au fil des ans. "
                               "Certaines catégories sociales montrent des "
                               "tendances à la hausse plus constantes, tandis que d'autres restent relativement "
                               "stables. Cela peut refléter des inégalités structurelles et l'accès différencié aux "
                               "ressources éducatives selon les origines sociales."],
                           9: ["Les taux de réussite au baccalauréat varient significativement selon l'origine "
                               "sociale des étudiants.",
                               " Les cadres et professions intellectuelles supérieures semblent "
                               "avoir des taux de réussite plus élevés, tandis que d'autres groupes, "
                               "comme les ouvriers et les employés, présentent des taux moins élevés. Cette disparité "
                               "souligne l'impact de l'origine sociale sur la réussite académique, indiquant "
                               "peut-être des inégalités structurelles dans l'accès à l'éducation et le soutien "
                               "scolaire."]}
                   )


elif page == pages[4]:

    st.title("Exploration et analyse des données")

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
        st.write("L'histogramme présente le pourcentage moyen de réussite au baccalauréat pour chaque origine sociale, "
                 "sur plus de 26 ans, toute période confindue.")
        st.write("L'axe vertical représente le pourcentage d'admis au baccalauréat, allant de 70% à 100%. L'axe "
                 "horizontal représente les différentes catégories d'origine sociale. ")
        st.write("Globalement, les taux de réussite sont élevés. Cpendant, les disparités dans les taux de réussite "
                 "reflètent peut-être des inégalités structurelles dans le"
                 "système éducatif, où certaines catégories sociales bénéficient de plus de ressources et de soutien "
                 "que d'autres. Ces résultats soulignent l'importance de politiques visant à réduire ces inégalités "
                 "pour garantir une égalité des chances pour tous les étudiants.")

elif page == pages[5]:

    # Prediction
    st.title("Prédiction 2024-2030")

    st.write("Modèle : Perceptron multicouche (Multi Layer Perceptron)")

    st.write("""
        ### Méthode d'entrainement
        - un modèle par origine sociale pour prédire les 8 valeurs (nombres et pourcentages de réussite sont les targets) pour cette origine à une date donnée (feature). Donc 12 modèles indépendants.
        - je tune chaque modèle séparément avec l'algorithme de Random Search. Les paramètres à optimiser sont :
            - le nombre de couches entre 1 et 5
            - le nombre de neurones pour chaque couche
            - le taux d'apprentissage entre 1e-4 et 1e-2""")

    plot_evolution(df_prediction2, 3, {}, interpretation=False)

elif page == pages[6]:

    st.title("Conclusion")

    st.write("Les visualisations réalisées à partir du dataset ont mis en lumière de manière claire et concise "
             "les inégalités persistantes dans l'accès au baccalauréat. Ces représentations graphiques ont permis "
             "d'identifier les tendances clés et de comprendre les mécanismes à l'œuvre. Cette approche quantitative, "
             "couplée à une analyse qualitative, offre une vision plus précise de la situation et permet d'orienter "
             "les politiques publiques de manière plus efficace. Pour réduire ces inégalités, il est nécessaire de "
             "mettre en place des mesures ciblées, telles que l'amélioration de l'accompagnement scolaire, "
             "la lutte contre les discriminations et la promotion de la diversité dans les établissements scolaires.")

