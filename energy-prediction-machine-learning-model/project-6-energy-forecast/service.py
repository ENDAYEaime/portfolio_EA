import bentoml
import pandas as pd

from schemas import EnergyFeatures


model_ref = bentoml.models.get("seattle_energy_model:latest")
model = model_ref.load_model()

FEATURE_NAMES = model.feature_names_in_.tolist()


@bentoml.service
class SeattleEnergyService:

    @bentoml.api
    def predict(self, features: EnergyFeatures) -> dict:
        df = pd.DataFrame([features.model_dump(by_alias=True)])
        df = df[FEATURE_NAMES]

        prediction = float(model.predict(df)[0])

        return {
            "site_energy_use_kbtu": prediction,
            "site_energy_use_kwh": prediction * 0.293071,
        }


















