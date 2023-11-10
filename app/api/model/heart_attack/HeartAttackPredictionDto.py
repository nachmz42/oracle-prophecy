from pydantic import BaseModel

class HeartAttackPredictionDto(BaseModel):
    prediction: int
