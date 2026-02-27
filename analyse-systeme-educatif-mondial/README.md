# Analyse des données éducatives mondiales  
## Identification des pays à fort potentiel pour une expansion internationale

## Contexte

Dans un contexte d’expansion internationale d’une entreprise du secteur éducatif (EdTech), il est essentiel d’identifier les pays présentant le plus fort potentiel de développement.

Ce projet s’appuie sur les données de la Banque mondiale (World Education Statistics) afin d’analyser différents indicateurs éducatifs, économiques et démographiques pour orienter une stratégie d’implantation.

---

## Problématique

Comment les données éducatives issues de la Banque mondiale peuvent-elles aider à identifier les pays présentant le plus fort potentiel pour une expansion internationale ?

---

## Données utilisées

Source : Banque mondiale – World Development Indicators / Education Statistics

Principaux fichiers exploités :
- EdStatsData.csv
- EdStatsCountry.csv
- EdStatsSeries.csv
- EdStatsFootNote.csv

Les données couvrent plus de 200 pays et plusieurs décennies d’indicateurs.

---

## Méthodologie

### 1. Exploration et compréhension des données
- Analyse de la structure des DataFrames
- Vérification des types et des valeurs manquantes
- Nettoyage des colonnes inutiles
- Renommage et harmonisation des variables

### 2. Sélection des indicateurs stratégiques

Indicateurs étudiés :
- PIB et PIB par habitant
- Accès à Internet (utilisateurs pour 100 habitants)
- Durée de scolarité obligatoire
- Taux de chômage
- Participation féminine au marché du travail
- Croissance démographique
- Population totale et population active

### 3. Analyse statistique

- Matrices de corrélation (Pearson et Spearman)
- Analyse des relations entre développement économique, connectivité et indicateurs éducatifs
- Identification des tendances temporelles
- Analyse comparative entre pays

### 4. Visualisations

- Heatmaps de corrélation
- Graphiques comparatifs par pays
- Classements (ex : top pays selon chômage)
- Sélection structurée des pays à fort potentiel

---

## Résultats clés

Les analyses montrent que les pays présentant un fort potentiel combinent :

- PIB élevé ou en forte croissance
- Forte connectivité numérique
- Système éducatif structuré et long
- Population jeune ou marché important
- Stabilité économique relative

Pays identifiés comme stratégiques (exemples) :
- Allemagne
- Finlande
- Suède
- Danemark
- France
- Japon
- Chine
- Inde
- Brésil
- Nigeria

Ces pays présentent un équilibre entre développement économique, infrastructure éducative et potentiel de marché.

---

## Compétences mobilisées

- Nettoyage et transformation de données avec Pandas
- Manipulation de jeux de données multi-sources
- Analyse statistique et corrélations
- Visualisation avec Matplotlib et Seaborn
- Interprétation orientée décision stratégique

---

## Stack technique

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Structure du projet

analyse-systeme-educatif-mondial/
│
├── README.md
├── analyse_systeme_educatif_mondial.ipynb
└── data/

---

## Perspectives d'amélioration

- Construction d’un score composite de potentiel pays
- Modélisation prédictive (clustering des pays)
- Intégration d’indicateurs macroéconomiques supplémentaires
- Automatisation du pipeline d’analyse

---

## Conclusion

Ce projet démontre la capacité à transformer des données publiques complexes en recommandations stratégiques exploitables pour une décision d’expansion internationale.

Il illustre une approche data-driven combinant analyse statistique, visualisation et interprétation métier.