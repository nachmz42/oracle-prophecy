from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from app.environment.params import HEART_ATTACK_DIET_VALUES, HEART_ATTACK_ORD_COLUMNS, HEART_ATTACK_CAT_COLUMNS, HEART_ATTACK_NUM_COLUMNS
from sklearn.pipeline import make_pipeline
from sklearn.compose import  ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

def create_pipeline():
    ordinal_enc = OrdinalEncoder(categories=[HEART_ATTACK_DIET_VALUES],
              handle_unknown='use_encoded_value',
              unknown_value=-1)
    scaler= StandardScaler()
    ohe = OneHotEncoder(drop='if_binary', sparse=False, handle_unknown='ignore')
    preprocessing_pipeline = ColumnTransformer(
    transformers=[
        ('numerical',scaler,HEART_ATTACK_NUM_COLUMNS),
        ('ordinal', ordinal_enc, HEART_ATTACK_ORD_COLUMNS),
        ('onehot', ohe, HEART_ATTACK_CAT_COLUMNS)
    ])

    clf = RandomForestClassifier(n_estimators=500, max_depth=20)

    pipeline = make_pipeline(preprocessing_pipeline,clf)

    return pipeline
