# Analyse des facteurs influençant la souscription à une offre bancaire
## Campagne de téléprospection

---

## 1. Contexte du projet

Dans le cadre d’une campagne de téléprospection, une institution bancaire souhaite analyser les données issues de ses appels afin de comprendre quels profils de clients sont les plus susceptibles de souscrire à une offre bancaire après un contact téléphonique.

Ce projet s’inscrit dans une démarche d’analyse de données visant à améliorer l’efficacité des campagnes marketing, optimiser le ciblage des clients et réduire les coûts de prospection.

---

## 2. Problématique

Quels sont les profils de clients les plus susceptibles de souscrire à une offre bancaire à la suite d’un appel téléphonique ?

---

## 3. Objectifs de l’étude

- Explorer et comprendre la structure du jeu de données
- Identifier les variables influençant la souscription à une offre bancaire
- Comparer les profils des clients souscripteurs et non-souscripteurs
- Mettre en évidence des leviers d’optimisation des campagnes marketing
- Préparer les bases d’une future modélisation prédictive

---

## 4. Présentation des données

Le jeu de données est composé de **45 211 observations** et de **18 variables**.

### 4.1 Variables socio-démographiques
- `age` : âge du client  
- `job` : profession  
- `marital` : situation matrimoniale  
- `education` : niveau d’éducation  

### 4.2 Variables bancaires
- `balance` : solde du compte bancaire  
- `housing` : crédit immobilier  
- `loan` : prêt personnel  

### 4.3 Variables liées à la campagne
- `duration` : durée de l’appel (en secondes)  
- `campaign` : nombre de contacts durant la campagne en cours  
- `previous` : nombre de contacts lors de campagnes précédentes  
- `pdays` : nombre de jours depuis le dernier contact  

### 4.4 Variable cible
- `y` : souscription à l’offre bancaire (`yes` / `no`)

---

## 5. Méthodologie

### 5.1 Préparation des données
- Filtrage des clients majeurs (âge ≥ 18 ans)
- Traitement des valeurs manquantes
- Suppression des variables jugées non pertinentes (`month`, `day`)
- Création de variables dérivées (tranches d’âge)

### 5.2 Analyse exploratoire des données
- Analyse univariée des variables quantitatives et qualitatives
- Analyse bivariée entre les variables explicatives et la variable cible
- Étude des corrélations entre variables numériques
- Comparaison des profils souscripteurs et non-souscripteurs

### 5.3 Visualisation
- Histogrammes
- Boxplots
- Courbes de densité
- Heatmap de corrélations

---

## 6. Résultats principaux

### 6.1 Durée de l’appel
La durée de l’appel est le facteur le plus déterminant de la souscription.
Les clients ayant souscrit présentent des appels significativement plus longs.
Les appels courts aboutissent rarement à une souscription.

### 6.2 Niveau d’éducation
Les clients ayant un niveau d’éducation tertiaire sont proportionnellement plus enclins à souscrire.
Les niveaux primary et unknown présentent les taux de souscription les plus faibles.

### 6.3 Historique de contact
Les clients ayant déjà été contactés lors de campagnes précédentes sont plus réceptifs à l’offre.
Une corrélation positive modérée est observée entre `previous` et `pdays`.

### 6.4 Âge
La majorité des souscripteurs se situe dans la tranche 25–50 ans.
Cependant, aucune relation linéaire forte n’est observée entre l’âge et la souscription.

### 6.5 Solde bancaire
Le solde bancaire présente une distribution fortement asymétrique.
Aucune relation significative directe n’est observée avec la souscription.

---

## 7. Profil type du client le plus susceptible de souscrire

Client adulte âgé de 25 à 50 ans, disposant d’un niveau d’éducation tertiaire,
ayant déjà été contacté lors de campagnes précédentes,
et engagé dans un appel téléphonique de durée relativement longue.

---

## 8. Implications métier

- Prioriser les clients à niveau d’éducation élevé
- Optimiser les scripts pour favoriser des appels plus longs et qualitatifs
- Réactiver les clients déjà contactés
- Exploiter les variables comportementales comme leviers principaux de ciblage

---

## 9. Conclusion

Cette analyse met en évidence que la souscription à une offre bancaire dépend principalement
de la qualité de l’interaction lors de l’appel téléphonique, plutôt que de critères
socio-démographiques bruts.

Les résultats obtenus constituent une base solide pour optimiser les campagnes marketing
et développer un futur modèle prédictif de souscription.

---

## 10. Structure du projet

projet_banque/
│
├── analyse_banque.ipynb
├── donnees_marketing_banque.csv
├── donnees_marketing_banque.xlsx
├── README.md
└── requirements.txt
