from app.api.model.heart_attack.HeartAttackPatientDto import HeartAttackPatientDto

class HeartAttackPatient():
    def __init__(self, patient_data: HeartAttackPatientDto):
        self.sex = patient_data.sex
        self.diet = patient_data.diet
        self.age = patient_data.age
        self.cholesterol = patient_data.cholesterol
        self.heart_rate = patient_data.heart_rate
        self.alcohol_consumption = patient_data.alcohol_consumption
        self.exercise_hours_per_week = patient_data.exercise_hours_per_week
        self.stress_level = patient_data.stress_level
        self.sedentary_hours_per_day = patient_data.sedentary_hours_per_day
        self.bmi = patient_data.bmi
        self.triglycerides = patient_data.triglycerides
        self.physical_activity_days_per_week = patient_data.physical_activity_days_per_week
        self.sleep_hours_per_day = patient_data.sleep_hours_per_day
