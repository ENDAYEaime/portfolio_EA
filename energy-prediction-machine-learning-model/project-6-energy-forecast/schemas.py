from pydantic import BaseModel, Field, ConfigDict


class EnergyFeatures(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    Electricity_kBtu: float = Field(..., alias="Electricity(kBtu)", ge=0)
    SteamUse_kBtu: float = Field(..., alias="SteamUse(kBtu)", ge=0)
    Log_PropertyGFATotal: float = Field(..., ge=0)
    LargestPropertyUseTypeGFA: float = Field(..., ge=0)
    GFA_per_Floor: float = Field(..., ge=0)
    NaturalGas_kBtu: float = Field(..., alias="NaturalGas(kBtu)", ge=0)
    BuildingAge: float = Field(..., ge=0)


