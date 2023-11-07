from pydantic import BaseModel

class HeartAttackPatientDto(BaseModel):
    sex: str
    diet:str
    age: int
    cholesterol:float
    heart_rate:int
    alcohol_consumption:float
    exercise_hours_per_week: float
    stress_level: int
    sedentary_hours_per_day: float
    bmi: float
    triglycerides:float
    physical_activity_days_per_week:float
    sleep_hours_per_day: float
