import os
from dotenv import load_dotenv
from pymongo import MongoClient
import polars as pl

# =====================================================
# Chargement des variables d'environnement
# =====================================================

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# =====================================================
# Connexion à MongoDB
# =====================================================

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# =====================================================
# Extraction des données MongoDB vers Polars
# =====================================================

data = list(collection.find({}, {"_id": 0}))
df = pl.DataFrame(data)

# =====================================================
# Préparation des variables analytiques
# =====================================================

# Calcul du taux de réservation annuel
df = df.with_columns(
    ((365 - pl.col("availability_365")) / 365)
    .alias("booking_rate")
)

# Extraction du mois à partir de la date du dernier avis
df = df.with_columns(
    pl.col("last_review")
      .str.strptime(pl.Date, strict=False)
      .dt.month()
      .alias("month")
)

# =====================================================
# 1. Taux de réservation moyen par mois et type de logement
# =====================================================

booking_rate_by_month_and_type = (
    df.filter(
        pl.col("month").is_not_null() &
        pl.col("room_type").is_not_null()
    )
    .group_by(["month", "room_type"])
    .agg(
        pl.col("booking_rate").mean().alias("average_booking_rate")
    )
    .sort(["month", "average_booking_rate"], descending=[False, True])
)

# =====================================================
# 2. Médiane du nombre d’avis pour l’ensemble des logements
# =====================================================

median_reviews_all = df.select(
    pl.col("number_of_reviews").median().alias("median_number_of_reviews")
)

# =====================================================
# 3. Médiane du nombre d’avis par catégorie d’hôte
# =====================================================

median_reviews_by_host_category = (
    df.group_by("host_is_superhost")
      .agg(
          pl.col("number_of_reviews").median()
          .alias("median_number_of_reviews")
      )
)

# =====================================================
# 4. Densité de logements par quartier de Paris
# =====================================================

housing_density_by_neighbourhood = (
    df.filter(pl.col("neighbourhood").is_not_null())
      .group_by("neighbourhood")
      .agg(
          pl.count().alias("number_of_listings")
      )
      .sort("number_of_listings", descending=True)
)

# =====================================================
# 5. Quartiers avec le plus fort taux de réservation par mois
# =====================================================

top_neighbourhoods_by_booking_rate = (
    df.filter(
        pl.col("month").is_not_null() &
        pl.col("neighbourhood").is_not_null()
    )
    .group_by(["month", "neighbourhood"])
    .agg(
        pl.col("booking_rate").mean().alias("average_booking_rate")
    )
    .sort(["month", "average_booking_rate"], descending=[False, True])
    .group_by("month")
    .head(3)
)

# =====================================================
# Affichage des résultats (contrôle)
# =====================================================

print("\nTaux de réservation moyen par mois et type de logement")
print(booking_rate_by_month_and_type)

print("\nMédiane du nombre d’avis (tous logements)")
print(median_reviews_all)

print("\nMédiane du nombre d’avis par catégorie d’hôte")
print(median_reviews_by_host_category)

print("\nDensité de logements par quartier")
print(housing_density_by_neighbourhood.head(10))

print("\nQuartiers avec le plus fort taux de réservation par mois")
print(top_neighbourhoods_by_booking_rate)




