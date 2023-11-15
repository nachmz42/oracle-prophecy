import os
from dotenv import load_dotenv

load_dotenv()
#Data origin
DATA_ORIGIN = os.environ.get("DATA_ORIGIN")

# Heart attack
HEART_ATTACK_CSV_NAME = os.getenv("HEART_ATTACK_CSV_NAME") or 'heart_attack_prediction_dataset.csv'
HEART_ATTACK_COLUMNS_TO_DROP = ['Income', 'Country', 'Continent', 'Hemisphere', 'BloodPressure', 'ID']
HEART_ATTACK_DIET_VALUES = ['Unhealthy','Average','Healthy']
HEART_ATTACK_CAT_COLUMNS = ['Sex']
HEART_ATTACK_ORD_COLUMNS = ['Diet']
HEART_ATTACK_NUM_COLUMNS = ['Age','Cholesterol','HeartRate','AlcoholConsumption','ExerciseHoursPerWeek','StressLevel','SedentaryHoursPerDay','BMI','Triglycerides','PhysicalActivityDaysPerWeek','SleepHoursPerDay']
HEART_ATTACK_COLUMNS = ['Sex','Diet','Age','Cholesterol','HeartRate','AlcoholConsumption','ExerciseHoursPerWeek','StressLevel','SedentaryHoursPerDay','BMI','Triglycerides','PhysicalActivityDaysPerWeek','SleepHoursPerDay']
HEART_ATTACK_COLUMNS_CSV = column_names = [
    "PatientID",
    "Age",
    "Sex",
    "Cholesterol",
    "BloodPressure",
    "HeartRate",
    "Diabetes",
    "FamilyHistory",
    "Smoking",
    "Obesity",
    "AlcoholConsumption",
    "ExerciseHoursPerWeek",
    "Diet",
    "PreviousHeartProblems",
    "MedicationUse",
    "StressLevel",
    "SedentaryHoursPerDay",
    "Income",
    "BMI",
    "Triglycerides",
    "PhysicalActivityDaysPerWeek",
    "SleepHoursPerDay",
    "Country",
    "Continent",
    "Hemisphere",
    "HeartAttackRisk"
]


# Database
SERVER = os.environ.get("SERVER")
DATABASE = os.environ.get("DATABASE")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
PORT = os.environ.get("PORT")

# MLOPS Paths
LOCAL_MLOPS_DIRECTORY = os.getenv("LOCAL_MLOPS_DIRECTORY") or ".mlops"
PIPELINE_DIRECTORY_HEART_ATTACK = os.path.join(LOCAL_MLOPS_DIRECTORY,"training_outputs","pipelines", "heart-attack")
DATA_DIRECTORY_HEART_ATTACK = os.path.join(LOCAL_MLOPS_DIRECTORY,"data","heart-attack",HEART_ATTACK_CSV_NAME)
