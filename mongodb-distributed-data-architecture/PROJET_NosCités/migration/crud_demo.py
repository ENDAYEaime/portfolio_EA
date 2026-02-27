import os
from dotenv import load_dotenv
from pymongo import MongoClient

# ==========================
# Chargement des variables d'environnement
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# ==========================
# Connexion MongoDB
# ==========================

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

print(" Connexion MongoDB établie")

# ==========================
# CREATE
# ==========================

def create_listing():
    listing = {
        "id": 999999999,
        "name": "Demo Listing - NosCités",
        "host_id": 123456,
        "neighbourhood_cleansed": "Paris Centre",
        "room_type": "Entire home/apt",
        "price": 150,
        "latitude": 48.8566,
        "longitude": 2.3522,
        "demo": True
    }

    result = collection.insert_one(listing)
    print(f" CREATE → Document inséré avec _id = {result.inserted_id}")

# ==========================
# READ
# ==========================

def read_listing():
    listing = collection.find_one({"demo": True})
    print(" READ → Document trouvé :")
    print(listing)

# ==========================
# UPDATE
# ==========================

def update_listing():
    result = collection.update_one(
        {"demo": True},
        {"$set": {"price": 180}}
    )
    print(f" UPDATE → Documents modifiés : {result.modified_count}")

# ==========================
# DELETE
# ==========================

def delete_listing():
    result = collection.delete_one({"demo": True})
    print(f"DELETE → Documents supprimés : {result.deleted_count}")

# ==========================
# MAIN
# ==========================

if __name__ == "__main__":
    print("🚀 Démonstration CRUD MongoDB")

    create_listing()
    read_listing()
    update_listing()
    read_listing()
    delete_listing()

    print(" Démonstration CRUD terminée")
