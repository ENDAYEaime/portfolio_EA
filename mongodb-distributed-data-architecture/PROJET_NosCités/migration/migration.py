import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient


# ==========================
# Chargement de l'environnement
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
DATA_FILE_PATH = os.getenv("DATA_FILE_PATH")
CITY = os.getenv("CITY")

print("DEBUG ENV_PATH =", ENV_PATH)
print("DEBUG DATA_FILE_PATH =", DATA_FILE_PATH)
print("DEBUG CITY =", CITY)


# =====================
# TEST AVANT MIGRATION
# =====================

def test_data_integrity(df):
    """
    Tests d'intégrité automatiques sur le CSV (avant migration).
    """
    print("Tests d'intégrité AVANT migration (CSV)...")

    required_columns = [
        "id",
        "host_id",
        "neighbourhood_cleansed",
        "room_type",
        "price",
        "latitude",
        "longitude",
    ]

    # Colonnes obligatoires
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Colonnes manquantes : {missing_cols}")

    # id et host_id : tolérance zéro
    if df[["id", "host_id"]].isnull().any().any():
        raise ValueError("Valeurs manquantes dans les identifiants critiques (id / host_id)")

    # price : autorisé mais signalé
    missing_price = df["price"].isnull().sum()
    if missing_price > 0:
        print(f"Attention : {missing_price} annonces sans prix renseigné")

    # Doublons d'annonces
    if df.duplicated(subset=["id"]).any():
        raise ValueError("Doublons détectés sur l'identifiant d'annonce")

    print("Tests CSV réussis")


# =================
# Transformation des données
# =================

def transform_data(df, city):
    """
    Transforme les données CSV en documents MongoDB.
    Ajoute le champ `city` pour la gestion multi-sites.
    """
    # Remplacer les NaN par None (MongoDB compatible)
    df = df.where(pd.notna(df), None)

    # Conversion simple du prix
    if "price" in df.columns:
        df["price"] = (
            df["price"]
            .astype(str)
            .str.replace(r"[^0-9.]", "", regex=True)
        )
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Ajout de la ville
    df["city"] = city

    return df.to_dict(orient="records")


# =================
# Migration vers MongoDB
# =================

def migrate_to_mongodb(data, mongo_uri, db_name, collection_name):
    """
    Migration incrémentale vers MongoDB (sans suppression).
    """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    result = collection.insert_many(data, ordered=False)
    print(f"Inserted {len(result.inserted_ids)} documents into '{collection_name}' collection.")


# =================
# Test après migration
# =================

def test_migration(mongo_uri, db_name, collection_name, expected_count):
    """
    Vérifie que le nombre total de documents est cohérent
    après import incrémental.
    """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    actual_count = collection.count_documents({})
    print(f"Nombre total de documents dans MongoDB : {actual_count}")

    if actual_count < expected_count:
        raise ValueError(
            "Le nombre de documents après migration est inférieur au nombre importé."
        )

    print("Test de migration réussi.")


# =================
# main
# =================

if __name__ == "__main__":
    print("Lancement du script de migration multi-sites")

    if CITY is None:
        raise ValueError("La variable CITY doit être définie dans le fichier .env")

    # Chargement des données
    df = pd.read_csv(DATA_FILE_PATH)

    # Tests avant migration
    test_data_integrity(df)

    # Transformation des données
    transformed_data = transform_data(df, CITY)

    # Migration vers MongoDB (AJOUT)
    migrate_to_mongodb(
        transformed_data,
        MONGO_URI,
        DB_NAME,
        COLLECTION_NAME
    )

    # Tests après migration
    test_migration(
        MONGO_URI,
        DB_NAME,
        COLLECTION_NAME,
        len(transformed_data)
    )

    print("Migration terminée avec succès")




  

