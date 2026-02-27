# Analyse et visualisation des centrales électriques en Europe

## Contexte
La transition énergétique est un enjeu majeur en Europe. Comprendre la répartition des centrales électriques, leurs sources d’énergie et leurs capacités permet de mieux appréhender les choix énergétiques des différents pays.

Ce projet s’inscrit dans une démarche d’analyse exploratoire et de visualisation de données appliquée à un jeu de données réel sur les centrales électriques européennes.

---

## Objectifs
L’objectif principal de ce projet est de :
- analyser la répartition des centrales électriques en Europe,
- comparer les sources d’énergie utilisées selon les pays,
- étudier les capacités de production par source et par technologie,
- mettre en évidence certaines spécificités nationales, notamment le cas de la France.

---

## Données
Le jeu de données utilisé recense des centrales électriques européennes et contient notamment :
- le pays,
- la localisation géographique (latitude, longitude),
- la source d’énergie,
- la capacité de production,
- la technologie utilisée.

Format : CSV  
Fichier : `powerplants-eu.csv`

---

## Méthodologie
Le projet suit les étapes suivantes :
1. Chargement et exploration des données
2. Nettoyage et préparation des variables
3. Analyse exploratoire globale
4. Comparaisons par pays
5. Analyse par source d’énergie
6. Focus spécifique sur la France
7. Comparaison de différentes librairies de visualisation

---

## Visualisations réalisées
- Diagrammes en barres (simples et empilées)
- Diagrammes en barres horizontales
- Boxplots
- Scatter plots
- Diagrammes circulaires (donut)
- Visualisations avec :
  - Matplotlib
  - Seaborn
  - Bokeh

---

## Outils et technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Bokeh
- Jupyter Notebook

---

## Résultats principaux
L’analyse met en évidence :
- une forte dominance de l’hydroélectricité en nombre de centrales,
- des capacités de production très concentrées sur certaines sources comme le nucléaire et le gaz,
- de fortes disparités entre les pays européens,
- une spécificité marquée de la France avec une capacité nucléaire largement dominante.

---

## Limites
- Les données ne tiennent pas compte de l’évolution temporelle.
- Certaines sources d’énergie sont regroupées ou peu détaillées.
- Les capacités installées ne reflètent pas nécessairement la production réelle.

---

## Conclusion
Ce projet illustre une démarche complète d’analyse exploratoire et de visualisation de données à partir d’un jeu de données réel. Il met en pratique des compétences clés en data analysis, notamment la manipulation de données, la visualisation et l’interprétation des résultats.

---

## Auteur
**Endaye Aimé**  
Projet réalisé dans le cadre de la construction d’un portfolio en analyse et ingénierie des données.
