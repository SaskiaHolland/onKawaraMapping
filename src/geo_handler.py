import json
import logging
from pathlib import Path

import pandas as pd
from geopy.geocoders import Nominatim

from src import utils
from src.utils import CSV_FILE, LOCATION_FILE

geolocator = Nominatim(user_agent="kawara_project")

logger = logging.getLogger(__name__)


def get_location() -> dict:
    table: pd.DataFrame = utils.open_csv(CSV_FILE)

    if not _check_location(table):
        _create_location_json(table)

    with open(LOCATION_FILE, encoding="utf-8") as fh:
        coordinates: dict = json.load(fh)
        fh.close()
    return coordinates


def _create_location_json(table: pd.DataFrame) -> None:
    cities = table['location/_type="creation Location"'].dropna().tolist()
    coordinates = {}  # besser als json speichern -> abfrage json ja sonst dic erweiterm -> json überschreiben

    for city in cities:
        if city in cities:
            continue
        try:
            location = geolocator.geocode(city)
            if location:
                coordinates[city] = [location.latitude, location.longitude]
            else:
                coordinates[city] = []
        except Exception as e:
            logger.warning(f"Could not geocode {city}: {e}")
            coordinates[city] = []

    _save_locations(coordinates)


def _check_location(table: pd.DataFrame) -> bool:
    with open("data/location.json", encoding="utf-8") as fh:
        json_file: dict = json.load(fh)

    cities = table['location/_type="creation Location"'].dropna().tolist()

    return all(city in json_file for city in cities)


def _save_locations(coordinates: dict, file_path: Path = LOCATION_FILE) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(coordinates, f, ensure_ascii=False, indent=4)
    logger.info(f"Saved {len(coordinates)} locations to {LOCATION_FILE}")
