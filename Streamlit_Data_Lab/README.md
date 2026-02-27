# DataScope – Interactive Data Explorer with Streamlit

## Description

DataScope est une application web interactive développée avec Streamlit permettant d’explorer, manipuler et visualiser des données en temps réel.

Ce projet démontre la conception d’une application data complète intégrant des widgets interactifs, le chargement de fichiers CSV, la manipulation dynamique de DataFrames et la création de visualisations avec Matplotlib et Plotly.

Il s’inscrit dans une démarche de développement d’applications data orientées utilisateur et de démonstration de compétences en data analysis et data engineering.

---

## Objectifs

- Comprendre l’architecture et le modèle d’exécution de Streamlit  
- Développer une application interactive de data exploration  
- Implémenter des widgets dynamiques pour le filtrage des données  
- Intégrer des visualisations statiques et interactives  
- Structurer une application multi-sections via une sidebar  
- Manipuler des DataFrames en temps réel  

---

## Fonctionnalités

### Interface utilisateur

- Navigation via sidebar (Accueil, Exploration des données, Visualisation, À propos)
- Organisation modulaire du contenu

### Exploration de données

- Upload de fichiers CSV
- Lecture et affichage automatique des DataFrames
- Filtrage dynamique via sliders et widgets

### Widgets interactifs

- Button
- Slider
- Checkbox
- Selectbox
- Text input
- Text area
- Date input
- Time input

### Visualisations

- Histogramme dynamique avec Matplotlib
- Graphique interactif avec Plotly
- Filtrage conditionnel par année

---

## Stack technique

- Python 3.x
- Streamlit
- Streamlit Jupyter
- Pandas
- NumPy
- Matplotlib
- Plotly
- Pillow

---

## Installation

```bash
pip install streamlit==1.22.0
pip install streamlit_jupyter
pip install pandas numpy matplotlib plotly pillow