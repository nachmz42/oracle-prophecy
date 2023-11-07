import os
from dotenv import load_dotenv

load_dotenv()

# Database
SERVER = os.environ.get("SERVER")
DATABASE = os.environ.get("DATABASE")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
PORT = os.environ.get("PORT")

# MLOPS Paths
LOCAL_MLOPS_DIRECTORY = os.getenv("LOCAL_MLOPS_DIRECTORY") or ".mlops"
PIPELINE_DIRECTORY_HEART_ATTACK = os.path.join(LOCAL_MLOPS_DIRECTORY,"training_outputs","pipelines", "heart-attack")

### HEART ATTACK
HEART_ATTACK_COLUMNS_TO_DROP = ['Income', 'Country', 'Continent', 'Hemisphere', 'BloodPressure', 'ID']
HEART_ATTACK_DIET_VALUES = ['Unhealthy','Average','Healthy']
HEART_ATTACK_CAT_COLUMNS = ['Sex']
HEART_ATTACK_ORD_COLUMNS = ['Diet']
HEART_ATTACK_NUM_COLUMNS = ['Age','Cholesterol','HeartRate','AlcoholConsumption','ExerciseHoursPerWeek','StressLevel','SedentaryHoursPerDay','BMI','Triglycerides','PhysicalActivityDaysPerWeek','SleepHoursPerDay']

HEART_ATTACK_COLUMNS = ['Sex','Diet','Age','Cholesterol','HeartRate','AlcoholConsumption','ExerciseHoursPerWeek','StressLevel','SedentaryHoursPerDay','BMI','Triglycerides','PhysicalActivityDaysPerWeek','SleepHoursPerDay']
