import pandas as pd
import json
# geo
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='kawara_project')

# open csv
def openCSV(csv):
    return pd.read_csv(csv, encoding='utf-8')

# get location with folium and save as json
def createLocationJson(table):
    cities = table['location/_type="creation Location"'].tolist()
    coordinates = {} #besser als json speichern -> abfrage json ja sonst dic erweiterm -> json überschreiben
    for city in cities:
        try: 
            location = geolocator.geocode(city)
            coordinates[city] = [location.latitude, location.longitude]
        except AttributeError:
            coordinates[city] = []

    # convert to json and save
    with open('data/location.json', 'w', encoding='utf-8') as fp:
        json.dump(coordinates, fp, ensure_ascii=False,  indent=4)
    
    return None

# check if city is already in json
def checkLocation(table):
    with open('data/location.json', encoding='utf-8') as fh:
        json_file = json.load(fh)

    cities = table['location/_type="creation Location"'].tolist()

    for city in cities:
        if not city in json_file.keys():
            return False
    return True

# save location as dict or update json
def getLocation():
    table = openCSV('./data/on_kawara_data.csv')
    check_cities = checkLocation(table)
    if not check_cities:
        createLocationJson(table)
    with open('data/location.json', encoding='utf-8') as fh:
        coordinates = json.load(fh) # dictionary
        fh.close()
    return coordinates

