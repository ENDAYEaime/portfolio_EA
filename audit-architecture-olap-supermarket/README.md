# Audit d’architecture de données OLAP – SuperSmartMarket

## Contexte

Dans le cadre de ce projet, j’ai été missionné pour auditer l’environnement de données d’une entreprise fictive (SuperSmartMarket), spécialisée dans la grande distribution.

L’entreprise constatait des incohérences dans son chiffre d’affaires historisé au sein de son entrepôt de données OLAP utilisé par Power BI.

Objectif : analyser l’architecture existante, comprendre les flux de données, identifier les anomalies et formuler des recommandations techniques.

---

## Objectifs du projet

- Analyser l’architecture de données existante
- Concevoir un schéma relationnel à partir d’un fichier à plat
- Créer un prototype de base de données
- Vérifier les indicateurs métiers via des requêtes SQL
- Analyser les logs de la base de données
- Identifier les causes d’incohérences du chiffre d’affaires
- Rédiger un rapport d’audit
- Formuler des recommandations techniques

---

## Démarche

### 1. Analyse de l’architecture

- Étude de l’environnement Microsoft (OLAP, Power BI)
- Compréhension des flux de données
- Identification des points sensibles

### 2. Modélisation des données

- Création d’un schéma relationnel
- Séparation table de faits / dimensions
- Mise en place des clés primaires et étrangères

### 3. Prototype SQL

- Création de la base de données
- Implémentation des tables
- Rédaction des requêtes d’analyse :
  - Chiffre d’affaires total
  - Top 10 clients
  - Chiffre d’affaires par employé

### 4. Analyse des logs

- Étude des logs de la base
- Identification d’opérations modifiant les données historiques
- Détection de mises à jour impactant le chiffre d’affaires

### 5. Recommandations

- Mise en place de contraintes d’intégrité
- Sécurisation des mises à jour
- Amélioration du suivi des modifications
- Application des principes ACID
- Utilisation de triggers ou procédures stockées
- Bonnes pratiques de gouvernance des données

---

## Résultats

- Confirmation du chiffre d’affaires réel
- Identification de la cause des variations historiques
- Proposition d’améliorations structurelles
- Documentation complète via :
  - Dictionnaire des données
  - Schéma relationnel
  - Rapport d’audit
  - Support de présentation

---

## Compétences mobilisées

- SQL avancé
- Modélisation relationnelle
- Architecture OLAP
- Audit de base de données
- Analyse de logs
- Qualité et gouvernance des données
- Documentation technique

---

## Technologies

- SQL
- SGBD relationnel (SQLite / PostgreSQL / MySQL selon implémentation)
- Power BI (contexte métier)

---

## Conclusion

Ce projet m’a permis de travailler sur un cas concret d’audit d’architecture de données, en combinant modélisation, analyse SQL et compréhension des enjeux métiers liés à la qualité des données.

Il met en évidence l’importance des bonnes pratiques d’intégrité, de traçabilité et de gouvernance dans un environnement décisionnel.