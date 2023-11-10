from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.interface.heart_attack.main import predict
from app.api.model.heart_attack.HeartAttackPatientDto import HeartAttackPatientDto
from app.api.services.heart_attack.adapters import patentDtoToHeartAttackDataFrame
from app.api.services.heart_attack.adapters import predictionDfToHeartAttackPredictionDto

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def index() -> dict:
    return {'ok': True}

@app.post('/heart-attack/predict')
def heart_attack_predict(patientDto: HeartAttackPatientDto):
    X_pred = patentDtoToHeartAttackDataFrame(patientDto)
    pred = predictionDfToHeartAttackPredictionDto(predict(X_pred))
    return pred
