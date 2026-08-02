
import pandas as pd
from .config import DATASETS
import os

def load_dataset(name, data_folder):
    if name not in DATASETS:
        raise ValueError(f"Unknown dataset: {name}")

    path = os.path.join(data_folder, DATASETS[name])
    return pd.read_csv(path)
