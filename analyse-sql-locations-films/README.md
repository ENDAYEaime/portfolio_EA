# Analyse SQL d'une base de locations de films (SQLite)

## Présentation

Ce projet consiste à construire une base de données SQLite à partir de fichiers CSV, puis à réaliser une analyse exploratoire et métier via des requêtes SQL exécutées depuis un notebook Jupyter.

L'objectif est double :
- pratiquer la création et l'alimentation d'une base relationnelle (SQLite) depuis des fichiers plats ;
- répondre à des questions d'analyse (popularité des films, dépenses clients, performance des magasins, etc.) à l'aide de jointures et d'agrégations.

## Données

Les données sont fournies sous forme de plusieurs fichiers CSV représentant différentes tables d'une base relationnelle de location de films (structure proche de Sakila), par exemple :
- film, actor, category
- film_actor, film_category
- customer, rental, payment
- store, staff
- address, city, country, language, inventory

## Contenu du notebook

### 1. Installation et imports
- installation et utilisation de `ipython-sql`
- imports Python : `pandas`, `numpy`, `sqlalchemy`

### 2. Création de la base SQLite
- création d'un fichier SQLite (ex: `data/database.db`)
- chargement automatique des CSV dans des tables SQL via SQLAlchemy

### 3. Compréhension du modèle relationnel
- visualisation des relations entre tables (diagramme)
- vérifications rapides : `SELECT ... LIMIT ...`, exploration des colonnes (`PRAGMA table_info(...)`)

### 4. Nettoyage / contrôles
- contrôle des types et de la cohérence des tables
- vérification des liaisons clés (jointures attendues) et des volumes

### 5. Analyses SQL
Exemples de questions traitées :
- films les plus populaires par genre (CTE + window function : `ROW_NUMBER() OVER(PARTITION BY ...)`)
- dépense moyenne par client (agrégation sur `payment`)
- nombre moyen de locations par client (agrégation sur `rental`)
- performance des magasins (transactions, revenu total, revenu moyen par location)

## Stack technique

- Python (Jupyter Notebook)
- SQLite
- SQLAlchemy
- ipython-sql
- Pandas / NumPy

## Arborescence recommandée

.
├── README.md
├── notebooks/
│   └── analyse_sql_locations_films.ipynb
├── data/
│   ├── raw/                  # CSV d'origine
│   └── database.db           # base SQLite générée
├── requirements.txt
└── .gitignore

## Installation

1) Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate