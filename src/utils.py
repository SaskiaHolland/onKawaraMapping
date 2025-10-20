from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
LOCATION_FILE = DATA_DIR / "location.json"
CSV_FILE = DATA_DIR / "on_kawara_data.csv"

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"
MISSING_FILE = OUTPUT_DIR / "cities_without_coordinates.txt"
OUTPUT_FILE = OUTPUT_DIR / "kawaraMap.html"


# open csv
def open_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, encoding="utf-8")
