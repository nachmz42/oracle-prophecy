from colorama import Fore, Style
import glob
import pickle
import time
import os

from app.environment.params import PIPELINE_DIRECTORY_HEART_ATTACK
from sklearn.pipeline import Pipeline



def save_pipeline(pipeline: Pipeline) -> None:
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # e.g. 20210824-154952

    # Save pipeline locally
    pipeline_path = os.path.join(PIPELINE_DIRECTORY_HEART_ATTACK ,f"{timestamp}.pkl")
    pickle.dump(pipeline, open(pipeline_path, 'wb'))

    print("✅ Pipeline saved locally")

    return None

def load_pipeline() -> Pipeline:
    #load pipeline locally
    local_pipeline_paths = glob.glob(f"{PIPELINE_DIRECTORY_HEART_ATTACK}/*")
    if not local_pipeline_paths:
        print(Fore.YELLOW +
                f"⚠️ No pipeline found in {PIPELINE_DIRECTORY_HEART_ATTACK}"
                + Style.RESET_ALL)
        raise FileNotFoundError

    most_recent_pipeline_path_on_disk = sorted(
        local_pipeline_paths)[-1]

    print(f"✅ Pipeline found at {most_recent_pipeline_path_on_disk}")
    print(Fore.BLUE + f"\nLoad latest pipeline from disk..." + Style.RESET_ALL)

    latest_pipeline = pickle.load(
        open(most_recent_pipeline_path_on_disk, "rb"))

    print("✅ Pipeline loaded from local disk")

    return latest_pipeline
