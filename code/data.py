import pandas as pd
import os

current_dir = os.path.dirname(__file__)

def load_emission_sncf_avion():
    filepath = os.path.join(current_dir, "../datasets/emission-co2-perimetre-complet.csv")

    df = pd.read_csv(filepath, sep=";")

    df["Train"] = df['Train - Empreinte carbone (kgCO2e)'] / df["Distance entre les gares"]
    df["Bus"] = df['Autocar longue distance - Empreinte carbone (kgCO2e)'] / df['Distance entre les gares']
    df["Voiture thermique"] = df['Voiture thermique (2,2 pers.) - Empreinte carbone (kgCO2e)'] / df['Distance entre les gares']
    df["Voiture electrique"] = df['Voiture électrique (2,2 pers.) - Empreinte carbone (kgCO2e)'] / df['Distance entre les gares']
    df["Avion"] = df['Avion - Empreinte carbone (kgCO2e)'] / df["Distance entre les gares"]

    df["Trajet"] = df["Origine"] + " - " + df["Destination"]   

    return df


def liste_gares_tgv():
    df = load_emission_sncf_avion()
    df_tgv = df[df['Transporteur'] == 'TGV']
    
    gares_origine = df_tgv['Origine'].unique()
    gares_destination = df_tgv['Destination'].unique()
    
    liste_gares = set(set(gares_origine) | set(gares_destination))

    liste_gares = list(liste_gares)
    
    return liste_gares

def liste_gares_intercites():
    df = load_emission_sncf_avion()
    df_intercités = df[df['Transporteur'] == 'Intercités']
    
    gares_origine = df_intercités['Origine'].unique()
    gares_destination = df_intercités['Destination'].unique()
    
    liste_gares = set(set(gares_origine) | set(gares_destination))

    liste_gares = list(liste_gares)
    
    return liste_gares

def liste_avions():
    df = load_emission_sncf_avion()
    df_avion = df[df['Avion - Empreinte carbone (kgCO2e)'].notna()]

    gares_origine = df_avion['Origine'].unique()
    gares_destination = df_avion['Destination'].unique() 
    
    liste_gares = set(set(gares_origine) | set(gares_destination))
    
    liste_gares = list(liste_gares)
    
    return liste_gares
def load_emissions_region():
    filepath = os.path.join(current_dir, "../datasets/Figure1_region.csv")

    df = pd.read_csv(filepath, sep=";")
    return df

def load_emissions_voitures_moto():
    filepath = os.path.join(current_dir, "../datasets/etude-facteurs-d'emissions-des-differents-modes-de-transport-routier.csv")

    df = pd.read_csv(filepath, sep=";")
    return df

def load_villes():
    filepath = os.path.join(current_dir, "../datasets/cities.csv")

    df = pd.read_csv(filepath, sep=",")
    return df

def load_gare():
    filepath = os.path.join(current_dir, "../datasets/liste-des-gares.csv")

    df = pd.read_csv(filepath, sep=";")
    return df

def liste_gares_ter():
    gares = load_gare()
    liste_gares = gares.iloc[:, 1].tolist()
    return liste_gares