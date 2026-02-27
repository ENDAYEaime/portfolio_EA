# Analyse et modélisation d’une base de données du marché immobilier français

## Contexte

Ce projet consiste à concevoir et exploiter une base de données relationnelle à partir de données publiques du marché immobilier français.

L’objectif est de structurer plusieurs jeux de données (biens, ventes, communes, départements, régions, population) afin de permettre des analyses multi-niveaux du marché immobilier.

Ce projet met l’accent sur la modélisation relationnelle, les jointures SQL et l’analyse de données territoriales.

---

## Objectifs

- Concevoir un schéma relationnel cohérent
- Créer une base de données structurée
- Mettre en place les clés primaires et étrangères
- Exploiter les données via des requêtes SQL analytiques
- Extraire des indicateurs pertinents sur le marché immobilier

---

## Données utilisées

Sources publiques françaises :

- Données de transactions immobilières (ventes)
- Données géographiques : communes, départements, régions
- Données démographiques : population
- Informations sur les biens immobiliers

Les données sont structurées autour des entités suivantes :

- Biens immobiliers
- Ventes
- Communes
- Départements
- Régions
- Population

---

## Modélisation de la base

La base relationnelle repose sur :

- Tables normalisées
- Clés primaires
- Clés étrangères
- Relations hiérarchiques (Commune → Département → Région)
- Lien entre transactions et biens

Un schéma relationnel est disponible dans le dossier `assets/`.

---

## Analyses réalisées

Exemples d’analyses SQL :

- Prix moyen au m² par commune
- Comparaison des prix par département
- Évolution des transactions par région
- Corrélation entre population et volume de ventes
- Identification des zones à forte attractivité
- Classement des régions selon le dynamisme immobilier

---

## Compétences mobilisées

- Modélisation relationnelle
- Conception de schéma SQL
- Jointures multi-tables
- Agrégations (GROUP BY, HAVING)
- Fonctions analytiques
- Nettoyage et structuration de données
- Analyse territoriale

---

## Stack technique

- SQL
- SGBD relationnel (SQLite / MySQL / PostgreSQL selon implémentation)
- Python (si scripts d’import utilisés)

---

## Structure du projet

analyse-base-donnees-immobilier-france/
│
├── README.md
├── creation_base.sql
├── requetes_analyse.sql
├── data/
└── assets/

---

## Perspectives d’amélioration

- Indexation pour optimisation des performances
- Création de vues matérialisées
- Mise en place d’un pipeline d’ingestion automatisé
- Création d’un dashboard (Power BI / Streamlit)

---

## Conclusion

Ce projet démontre la capacité à concevoir et exploiter une base de données relationnelle complète à partir de données brutes.

Il met en avant des compétences clés en modélisation SQL et en analyse de données structurées, essentielles pour un poste en Data Engineering ou Data Analyst.