from app.ml_logic.heart_attack.data import load_data_from_sql
from app.environment.params import HEART_ATTACK_COLUMNS_TO_DROP, HEART_ATTACK_NUM_COLUMNS
import pandas as pd
from sklearn.model_selection import train_test_split
from app.ml_logic.heart_attack.pipeline import create_pipeline
from app.ml_logic.heart_attack.registry import save_pipeline, load_pipeline
from colorama import Fore, Style

def preprocess(data: pd.DataFrame):
    columns_to_drop = HEART_ATTACK_COLUMNS_TO_DROP
    columns_to_drop = [col for col in columns_to_drop if col in data.columns]

    if columns_to_drop:
        data.drop(columns=columns_to_drop, inplace=True)

    return data

def train():
    print(Fore.MAGENTA + "\n ⭐️ Use case: preprocess and train the Heart Attack model" + Style.RESET_ALL)
    data = load_data_from_sql()
    data = preprocess(data)

    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)
    # Balance data
    df_0 = data[data['HeartAttackRisk'] == 0] # The group with spam value 0
    df_1 = data[data['HeartAttackRisk'] == 1] # The group with spam value 1

    # Find the number of rows in the smaller group
    n = min(len(df_0), len(df_1))

    # Sample n rows from the larger group without replacement
    df_0_balanced = df_0.sample(n, replace=False, random_state=42)

    # Concatenate the balanced group with the smaller group
    data = pd.concat([df_0_balanced, df_1])

    X = data.drop(columns=['HeartAttackRisk'],axis=1)
    y= data[['HeartAttackRisk']]
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = create_pipeline()

    # Fit pipeline
    pipeline.fit(X_train, y_train)
    print(Fore.GREEN + "\n ✅ Model trained" + Style.RESET_ALL)
    # Save pipeline
    save_pipeline(pipeline=pipeline)

def evaluate():
    print(Fore.MAGENTA + "\n ⭐️ Use case: evaluate the Heart Attack model" + Style.RESET_ALL)
    data = load_data_from_sql()
    data = preprocess(data)

    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)
    # Balance data
    df_0 = data[data['HeartAttackRisk'] == 0] # The group with spam value 0
    df_1 = data[data['HeartAttackRisk'] == 1] # The group with spam value 1

    # Find the number of rows in the smaller group
    n = min(len(df_0), len(df_1))

    # Sample n rows from the larger group without replacement
    df_0_balanced = df_0.sample(n, replace=False, random_state=42)

    # Concatenate the balanced group with the smaller group
    data = pd.concat([df_0_balanced, df_1])
    X = data.drop(columns=['HeartAttackRisk'],axis=1)
    y= data[['HeartAttackRisk']]
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = load_pipeline()
    accuracy = pipeline.score(X_test, y_test)
    print(f"✅ Model acurracy: {accuracy}")

def predict(X_pred: pd.DataFrame | None = None):

    print(Fore.MAGENTA + "\n ⭐️ Use case: pred" + Style.RESET_ALL)
    pipeline = load_pipeline()
    X_pred = preprocess(X_pred)
    return pipeline.predict(X_pred)
