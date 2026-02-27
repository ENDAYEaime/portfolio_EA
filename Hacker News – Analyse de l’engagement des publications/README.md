# Hacker News – Analyse de l’engagement des publications

## Contexte
Hacker News est une plateforme communautaire utilisée par des développeurs, entrepreneurs et passionnés de technologie pour partager des articles, poser des questions et présenter des projets.  
Ce projet vise à analyser les publications afin de comprendre quels types de posts génèrent le plus d’engagement et à quels moments ils sont les plus susceptibles de recevoir des commentaires.

---

## Objectifs
- Comparer l’engagement entre les publications de type *Ask HN* et *Show HN*
- Mesurer l’impact de l’heure de publication sur le nombre moyen de commentaires
- Identifier les créneaux horaires optimaux pour maximiser l’engagement

---

## Données
- Source : Hacker News (fichier CSV)
- Données analysées :
  - Titre des publications
  - Type de post (Ask HN, Show HN, autres)
  - Date et heure de publication
  - Nombre de commentaires

---

## Technologies utilisées
- Python
- Jupyter Notebook
- Bibliothèque `datetime`
- Structures de données natives (listes, dictionnaires)

---

## Analyse réalisée
- Nettoyage et structuration des données
- Séparation des publications par type
- Calcul du nombre moyen de commentaires par type de post
- Analyse temporelle de l’engagement par heure de publication
- Classement des heures générant le plus d’interactions

---

## Résultats principaux
- Les publications *Ask HN* génèrent en moyenne plus de commentaires que les *Show HN*
- L’engagement varie fortement selon l’heure de publication
- Le créneau le plus performant se situe autour de **15h (heure EST)**

---

## Conclusion
Cette analyse montre que le type de publication et le moment de diffusion ont un impact significatif sur l’engagement des utilisateurs.  
Pour maximiser le nombre de commentaires, il est recommandé de privilégier les posts de type *Ask HN* et de publier en milieu d’après-midi (heure EST).

---

## Limites et perspectives
- Les publications sans commentaires ont été exclues de l’analyse
- L’analyse pourrait être approfondie avec :
  - Une visualisation graphique des résultats
  - Une prise en compte des jours de la semaine
  - Une analyse basée sur le score ou le nombre de vues
