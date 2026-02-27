# Jupyter Fundamentals – Data Workflow

## Présentation du projet

Ce projet a pour objectif de présenter les bases d’utilisation de Jupyter Notebook dans un contexte d’analyse de données avec Python.

Il couvre les notions essentielles suivantes :

- Exécution et gestion des cellules
- Compréhension de l’état (state) du notebook
- Ordre d’exécution et reproductibilité
- Définition et utilisation de fonctions
- Lecture et manipulation de fichiers CSV
- Rédaction de documentation avec Markdown

Ce projet constitue une base technique pour des travaux d’analyse de données plus avancés.

---

## Objectifs pédagogiques

- Comprendre le fonctionnement interne de Jupyter Notebook
- Apprendre à structurer un notebook de manière claire et reproductible
- Manipuler des données issues d’un fichier CSV
- Documenter un travail d’analyse avec Markdown

---

## Technologies utilisées

- Python 3
- Jupyter Notebook (environnement VS Code)
- Module csv
- Markdown

---

## Structure du projet

jupyter-fundamentals-data-workflow/
│
├── Apprendre_et_installer_Jupyter_Notebook.ipynb
├── AppleStore.csv
├── README.md
└── requirements.txt

---

## Concepts clés abordés

### 1. Exécution des cellules

Chaque cellule possède un ordre d’exécution.  
L’ordre dans lequel les cellules sont exécutées peut influencer le résultat final.

### 2. Gestion de l’état (State)

Les variables définies dans une cellule restent en mémoire tant que le kernel est actif.

### 3. État caché (Hidden State)

L’utilisation de la commande `%history` permet d’identifier les instructions exécutées précédemment, même si elles ne sont plus visibles.

### 4. Lecture d’un fichier CSV

Le projet montre comment :
- Ouvrir un fichier CSV
- Lire son contenu
- Transformer les données en liste exploitable
- Afficher les premières lignes du jeu de données

---

## Reproductibilité

Pour garantir des résultats cohérents :

1. Redémarrer le kernel
2. Exécuter toutes les cellules dans l’ordre

Cela permet d’éviter les erreurs liées à un état mémoire incohérent.

---

## Améliorations possibles

- Utilisation de la bibliothèque pandas pour une manipulation plus avancée des données
- Ajout d’une analyse exploratoire (EDA)
- Visualisations avec Matplotlib ou Seaborn
- Nettoyage et préparation des données

---

## Auteur

Aimé Endaye  
Étudiant en Data Engineering et Analyse de Données