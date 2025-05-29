# Football Data Pipeline - Projet Data Engineering sur GCP

## Description

Ce projet personnel a pour objectif de construire un pipeline de données complet autour des données footballistiques, en utilisant les services Google Cloud Platform (GCP).  
Il récupère les données via une API football, stocke les fichiers dans Google Cloud Storage (Data Lake), les traite avec Dataflow et BigQuery (Data Warehouse), et génère des reportings via Looker. L’ensemble est orchestré avec Cloud Composer (Apache Airflow).

---

## Architecture

- **Google Cloud Storage** : stockage brut des données récupérées (JSON, CSV, etc.)
- **Dataflow** : traitement et transformation des données en pipeline ETL/ELT
- **BigQuery** : stockage structuré et analyse SQL
- **Looker** : tableaux de bord et reporting interactif
- **Cloud Composer** : orchestration et automatisation du pipeline

---

## Fonctionnalités

- Récupération des données football via API (ex : API-Football)
- Stockage des données brutes dans un bucket GCS
- Traitement et nettoyage des données
- Chargement dans BigQuery pour analyse
- Visualisation via Looker
- Automatisation via DAGs Cloud Composer

---

## Installation & utilisation

1. Cloner le dépôt :

```bash
git clone https://github.com/mouyassirm/gcp-sports-etl-project.git
cd gcp-sports-etl-project
