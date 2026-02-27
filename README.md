# Portfolio Data Science

Ce portfolio est un site web statique conçu pour présenter mes projets de data science, data analyse et data engineering à des recruteurs.  
Il a pour objectif de mettre en avant ma capacité à comprendre une problématique, analyser des données, produire des visualisations pertinentes et présenter des résultats exploitables.

Le site est développé en HTML et CSS et peut être déployé facilement via GitHub Pages.

---

## Objectifs du portfolio
- Présenter des projets concrets et structurés
- Mettre en avant les compétences techniques et analytiques
- Fournir une navigation claire et professionnelle
- Faciliter l’évaluation rapide de mon profil par un recruteur

---

## Structure du projet

.
├── index.html # Page d’accueil du portfolio
├── styles/ # Feuilles de style CSS
│ ├── main.css # Styles globaux du site
│ └── projet.css # Styles spécifiques aux pages de projets
├── projets/ # Pages dédiées aux projets
│ └── projet1.html # Modèle de page projet
└── images/ # Images et captures d’écran

yaml
Copier le code

---

## Ajouter un nouveau projet

1. Créer une nouvelle page HTML dans le dossier `projets/` en dupliquant le fichier `projet1.html`
2. Modifier le contenu pour décrire le projet :
   - Contexte
   - Problématique
   - Données utilisées
   - Méthodes et outils
   - Résultats et conclusions
3. Ajouter les captures d’écran ou visuels dans le dossier `images/`
4. Mettre à jour la section projets de `index.html` pour inclure un lien vers la nouvelle page

---

## Déploiement sur GitHub Pages

1. Créer un nouveau dépôt sur GitHub
2. Initialiser Git dans le dossier du projet :
```bash
git init
git add .
git commit -m "Initial commit"
Lier le dépôt local au dépôt GitHub :

bash
Copier le code
git remote add origin https://github.com/votre-username/votre-repo.git
git branch -M main
git push -u origin main
Accéder aux paramètres du dépôt GitHub

Dans la section « Pages », sélectionner la branche main comme source

Le site sera accessible à l’adresse suivante :

arduino
Copier le code
https://votre-username.github.io/votre-repo/
Personnalisation du portfolio
Modifier les couleurs, typographies et styles globaux dans styles/main.css

Adapter les styles spécifiques aux projets dans styles/projet.css

Mettre à jour les informations personnelles et de contact dans index.html

Ajouter ou remplacer les images dans le dossier images/

Ajuster la structure des pages projet selon les besoins

Bonnes pratiques pour un portfolio efficace
Présenter des projets clairs, concrets et bien structurés

Mettre en avant la problématique et la valeur ajoutée de chaque projet

Décrire les choix techniques et méthodologiques

Inclure des visualisations lisibles et pertinentes

Ajouter des liens vers le code source et, si possible, des démonstrations en ligne

Maintenir le contenu à jour

Optimiser les images pour le web afin d’améliorer les performances

Tester le site sur différents navigateurs et tailles d’écran

