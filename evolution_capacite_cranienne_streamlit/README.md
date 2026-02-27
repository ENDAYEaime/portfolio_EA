# Évolution de la capacité crânienne humaine – Application Streamlit

## Présentation du projet
Ce projet consiste en une application interactive de data analyse et de data visualisation, développée avec Streamlit, visant à explorer l’évolution de la capacité crânienne humaine à travers le temps, l’espace géographique et différentes caractéristiques morphologiques.

L’objectif est de transformer un jeu de données paléo-anthropologique complexe en analyses compréhensibles, visualisations interactives et conclusions exploitables.

---

## Problématique
Quels sont les facteurs anatomiques, géographiques, environnementaux et temporels qui influencent l’évolution de la capacité crânienne chez les hominidés ?

---

## Données utilisées
- Fichier : `Evolution_DataSets_clean.csv`
- Données nettoyées et préparées en amont
- Variables principales :
  - Capacité crânienne (cm³)
  - Temporalité (millions d’années)
  - Pays et zones géographiques
  - Espèces ou groupes humains
  - Caractéristiques morphologiques et comportementales

---

## Structure de l’application
L’application est organisée en plusieurs pages thématiques.

### Accueil
- Présentation du contexte scientifique
- Objectifs du projet
- Indicateurs clés (nombre de spécimens, pays analysés, capacité crânienne moyenne)
- Introduction à l’analyse multi-facteurs

### Analyse statistique
- Analyse exploratoire des données
- Statistiques descriptives
- Analyse des variables numériques et catégorielles
- Filtres interactifs appliqués à l’ensemble des visualisations

### Visualisation des données
- Distributions (histogrammes, boxplots)
- Évolutions temporelles
- Analyses multivariées
- Visualisations interactives

### Analyse géographique
- Cartographie interactive des données
- Répartition spatiale par pays
- Analyse de la densité des observations
- Statistiques par zone géographique

### Résultats et conclusions
- Synthèse des principaux résultats
- Tendances évolutives majeures
- Corrélations anatomiques et environnementales
- Limites de l’étude et pistes d’amélioration

---

## Technologies utilisées
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Folium

---

## Structure du projet
evolution_capacite_cranienne_streamlit/
│
├── pages/
│ ├── 1_Analysis.py
│ ├── 2_Visualization.py
│ ├── 3_Geographic_Analysis.py
│ └── 3_Results.py
│
├── static/
│ └── style.css
│
├── models/
├── Home.py
├── router.py
├── config.py
├── Evolution_DataSets_clean.csv
├── requirements.txt
└── README.md