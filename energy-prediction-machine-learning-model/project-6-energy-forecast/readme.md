# Seattle Energy Forecast  
**Déploiement en production d’un modèle de machine learning**

---

## Présentation générale du projet

Ce projet s’inscrit dans une démarche complète et réaliste de **data science appliquée**, allant de l’analyse des données jusqu’au **déploiement en production d’un modèle de machine learning** accessible via une **API REST hébergée sur le cloud**.

L’objectif principal est de **prédire la consommation énergétique annuelle normalisée d’un bâtiment** à partir de ses caractéristiques structurelles et de certaines composantes énergétiques mesurées, puis de rendre cette prédiction exploitable par des utilisateurs ou des systèmes externes.

Le projet met l’accent sur :
- la rigueur méthodologique en data science,
- la qualité du feature engineering,
- la robustesse des modèles,
- la reproductibilité,
- et les bonnes pratiques de mise en production (MLOps).

---

## Objectifs du projet

- Construire un modèle de prédiction de la consommation énergétique des bâtiments
- Comparer plusieurs modèles supervisés
- Sélectionner un modèle performant et cohérent métier
- Packager le modèle de manière reproductible
- Exposer le modèle via une API REST
- Déployer le service sur une infrastructure cloud
- Tester le service en conditions réelles

---

## Jeu de données

Le projet repose sur le dataset **Seattle Building Energy Benchmark**, qui contient des informations énergétiques et structurelles sur des bâtiments tertiaires et publics de la ville de Seattle.

### Types de données disponibles
- caractéristiques physiques des bâtiments (surface, âge, nombre d’étages)
- consommations énergétiques par source (électricité, gaz naturel, vapeur)
- indicateurs de performance énergétique
- indicateurs environnementaux (émissions de GES)

Les données couvrent plusieurs centaines de bâtiments et permettent une approche réaliste de modélisation énergétique à l’échelle urbaine.

---

## Démarche de Data Science

L’ensemble du travail de data science est réalisé dans un **notebook Jupyter structuré et documenté**, suivant une démarche progressive et justifiée.

---

### Analyse exploratoire des données

L’analyse exploratoire vise à comprendre la structure et les caractéristiques du dataset avant toute modélisation.

Elle inclut notamment :
- l’étude de la structure globale des données
- l’analyse des distributions des variables
- l’identification des valeurs manquantes et aberrantes
- l’analyse des corrélations entre variables numériques
- la compréhension métier des indicateurs énergétiques

Cette étape permet d’identifier les variables pertinentes et les risques potentiels (redondance, corrélation excessive, fuite de données).

---

### Feature engineering et sélection des variables

La sélection des variables repose sur plusieurs critères :
- cohérence métier
- variance suffisante
- contribution au modèle
- limitation des redondances
- prévention du *data leakage*

Les analyses de corrélation et d’importance des variables ont conduit à retenir un **sous-ensemble volontairement restreint et cohérent** de variables explicatives.

Certaines variables fortement corrélées ou dérivées ont été supprimées, tandis que d’autres, bien que fortement liées à la consommation énergétique, ont été conservées car elles représentent des **composantes réelles et mesurées de l’énergie consommée**.

---

## Variable cible (target)

```text
SiteEnergyUseWN(kBtu)
