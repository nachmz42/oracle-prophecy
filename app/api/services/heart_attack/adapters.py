import pandas as pd
from app.api.model.heart_attack.HeartAttackPatientDto import HeartAttackPatientDto
from app.api.model.heart_attack.HeartAttackPatient import HeartAttackPatient
from app.environment.params import HEART_ATTACK_COLUMNS



def patentDtoToHeartAttackDataFrame(patientDto: HeartAttackPatientDto):
    '''Converts a HeartAttackPatientDto into a Data frame'''
    df = pd.DataFrame([list(HeartAttackPatient(patientDto).__dict__.values())],columns=HEART_ATTACK_COLUMNS)
    return df
