# Pandas Data Lab

Ce projet regroupe une série d’exercices pratiques visant à maîtriser la manipulation et le nettoyage de données avec la bibliothèque Pandas.

Le notebook couvre les opérations fondamentales utilisées en Data Analysis et Data Engineering.

---

## Objectif

Renforcer les compétences sur :

- Lecture de fichiers CSV
- Exploration de DataFrame
- Sélection de colonnes et de lignes
- Filtrage conditionnel
- Gestion des index
- Nettoyage des valeurs manquantes
- Transformation de colonnes
- Agrégation et groupby
- Analyse descriptive
- Tri et extraction des valeurs extrêmes

---

## Contenu du notebook

### 1. Import des librairies

- pandas
- matplotlib (visualisation)

### 2. Lecture et exploration des données

- read_csv()
- head()
- tail()
- describe()
- value_counts()

### 3. Manipulation du DataFrame

- Sélection de colonnes
- Sélection de lignes avec loc
- Filtrage avec conditions multiples
- Création de nouvelles colonnes
- Modification d’index
- Reset d’index

### 4. Nettoyage des données

- Détection des valeurs nulles
- fillna()
- dropna()
- Remplacement de valeurs
- Conversion de types (astype)

### 5. Agrégation et analyse

- groupby()
- sum()
- value_counts()
- nlargest()

### 6. Mini cas pratique

Nettoyage et analyse d’un dataset sur les centrales électriques européennes :

- Analyse des capacités installées
- Répartition par type d’énergie
- Identification des plus grandes centrales
- Analyse descriptive des variables numériques

---

## Technologies utilisées

- Python 3.x
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Installation

```bash
pip install pandas matplotlib jupyter