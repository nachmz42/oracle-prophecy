import pandas as pd
from app.api.model.heart_attack.HeartAttackPatientDto import HeartAttackPatientDto
from app.api.model.heart_attack.HeartAttackPatient import HeartAttackPatient
from app.api.model.heart_attack.HeartAttackPredictionDto import HeartAttackPredictionDto
import numpy as np

from app.environment.params import HEART_ATTACK_COLUMNS



def patentDtoToHeartAttackDataFrame(patientDto: HeartAttackPatientDto):
    '''Converts a HeartAttackPatientDto into a Data frame'''
    df = pd.DataFrame([list(HeartAttackPatient(patientDto).__dict__.values())],columns=HEART_ATTACK_COLUMNS)
    return df

def predictionDfToHeartAttackPredictionDto(prediction_array: np.ndarray) -> HeartAttackPredictionDto:
    '''Converts the prediction returned by the model into HeartAttackPredictionDto'''
    if prediction_array.size != 1 or (prediction_array != 0 and prediction_array != 1):
        raise ValueError("Array must have just 1 value 0 or 1.")

    prediction_value = int(prediction_array.item())
    return HeartAttackPredictionDto(prediction=prediction_value)
