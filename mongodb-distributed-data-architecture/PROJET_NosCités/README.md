# NosCités – Infrastructure MongoDB Distribuée

## Présentation

Ce projet a pour objectif de concevoir et déployer une infrastructure de base de données distribuée avec MongoDB.  
L’enjeu principal est de garantir la haute disponibilité, la tolérance aux pannes et la scalabilité horizontale.

Les données utilisées proviennent d’annonces immobilières issues de deux villes : Paris et Lyon.

Ce projet s’inscrit dans une logique d’architecture Data Engineering proche d’un environnement de production.

---

## Objectifs

- Importer des fichiers CSV dans MongoDB
- Structurer les collections de manière cohérente
- Mettre en place un Replica Set
- Implémenter un cluster shardé
- Tester la réplication des données
- Vérifier la distribution et l’intégrité des données

---

## Architecture du projet

### 1. Importation des données

Les fichiers CSV ont été :

- Nettoyés et préparés
- Transformés si nécessaire
- Injectés dans MongoDB via un script Python

Collections principales :

- listings_paris
- listings_lyon

Des vérifications ont été effectuées pour contrôler :
- Le nombre total de documents
- La cohérence des champs
- Les types de données

---

### 2. Mise en place du Replica Set

Un Replica Set a été configuré afin d’assurer la haute disponibilité de la base de données.

Configuration :

- 1 nœud Primary
- 1 nœud Secondary
- 1 Arbiter

Fonctionnement :

- Le Primary reçoit les opérations d’écriture
- Les Secondary répliquent automatiquement les données
- L’Arbiter participe au quorum en cas de défaillance

Objectif :

- Garantir la continuité de service
- Protéger les données contre les pannes matérielles

---

### 3. Mise en place du Sharding

Un cluster shardé a été configuré afin de distribuer les données sur plusieurs serveurs.

Objectifs :

- Améliorer les performances
- Répartir la charge
- Permettre une montée en charge horizontale

Stratégie adoptée :

- Répartition des données selon la ville

Le sharding permet d’éviter la saturation d’un seul serveur et d’optimiser les requêtes.

---

## Technologies utilisées

- MongoDB
- MongoDB Compass
- Python
- Pandas
- Docker
- Ligne de commande MongoDB

---

## Vérifications réalisées

- Vérification du statut du Replica Set
- Test de réplication entre les nœuds
- Vérification de la distribution des shards
- Contrôle du nombre de documents par collection

---

## Résultats

- Infrastructure distribuée opérationnelle
- Données correctement répliquées
- Sharding fonctionnel
- Architecture scalable et tolérante aux pannes

---

## Perspectives d’amélioration

- Déploiement sur MongoDB Atlas
- Mise en place d’un monitoring
- Renforcement de la sécurité (authentification et rôles)
- Intégration avec un outil de Business Intelligence