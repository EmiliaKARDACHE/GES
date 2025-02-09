from data import load_villes
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd

villes_df = load_villes()

def make_listes_villes():

    villes_df['zip_code'] = villes_df['zip_code'].fillna(0).astype(int)
    villes_df['ville dep'] = villes_df['name'].astype(str) + ' - ' + villes_df['zip_code'].astype(str)
    villes = villes_df.iloc[:, 4].tolist()
    departements = villes_df.iloc[:, 3].tolist()

    liste_villes = []
    for i in range(len(villes)):
        liste_villes.append(villes[i] + " - " + str(departements[i]))

    return liste_villes

def get_coordinates(ville):
    city_data = villes_df[villes_df['ville dep'] == ville]
    
    latitude = city_data['gps_lat'].values[0]
    longitude = city_data['gps_lng'].values[0]
    return latitude, longitude

def calculer_distance(ville1, ville2):
    coord_ville1 = get_coordinates(ville1)
    coord_ville2 = get_coordinates(ville2)
    
    distance = geodesic(coord_ville1, coord_ville2).kilometers
    return distance
    
make_listes_villes()
#print(get_coordinates("Paradou - 13520"))
