from data import *
from distance import *
import streamlit as st
import pandas as pd
import os
from etudes import afficher_page_etudes 


os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = '' 
os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''

    

villes = make_listes_villes()
villes = [""] + villes 
trains_avions = load_emission_sncf_avion()
    
trajets_allers_tgv = trains_avions.loc[trains_avions['Transporteur'] == 'TGV', 'Origine'].to_list
trajets_retours_tgv = trains_avions.loc[trains_avions['Transporteur'] == 'TGV', 'Destination'].to_list
    
trajets_allers_intercites = trains_avions.loc[trains_avions['Transporteur'] == 'Intercités', 'Origine'].to_list
trajets_retours_intercites = trains_avions.loc[trains_avions['Transporteur'] == 'Intercités', 'Destination'].to_list
    
trajets_allers_avion = origines_avion = trains_avions.loc[trains_avions['Avion - Empreinte carbone (kgCO2e)'].notna(), 'Origine'].tolist()
trajets_retours_avion = origines_avion = trains_avions.loc[trains_avions['Avion - Empreinte carbone (kgCO2e)'].notna(), 'Destination'].tolist()
    
gares_ter = liste_gares_ter()
gares_ter = [""] + gares_ter
    
gares_tgv = liste_gares_tgv()
gares_tgv = [""] + gares_tgv
    
gares_intercites = liste_gares_intercites()
gares_intercites = [""] + gares_intercites
    
gares_intercites = liste_gares_intercites()
gares_intercites = [""] + gares_intercites
    
avions = liste_avions()
avions = [""] + avions
    
trains = load_emission_sncf_avion()
    
ter_trains = trains[(trains['Transporteur'] == 'TGV')]
emission_tgv = ter_trains['Train'].mean()
    
intercités_trains = trains[(trains['Transporteur'] == 'Intercités')]
emission_intercite = ter_trains['Train'].mean()

st.title("Formulaire de Transport")
st.text("Merci de mettre chaque étape du trajet en cas de correspondance.")
st.markdown("""
    <style>
        body {
            background-color: #003366; 
            color: yellow;
            margin: 0;                  /* Supprimer les marges par défaut */
            padding: 0;                 /* Supprimer les padding par défaut */
            height: 100vh;              /* Assurer que le body occupe toute la hauteur de la fenêtre */
            width: 100vw;               /* Assurer que le body occupe toute la largeur de la fenêtre */
            display: flex;
            flex-direction: column;     /* Flexbox pour aligner verticalement les éléments */
            justify-content: flex-start; /* Placer les éléments du haut vers le bas */
        }

        .column-style {
            margin-right: 20px;
        }
        
        .line-spacing {
            margin-bottom: 30px;
        }
        
        .title-text {
            color: #003366; /* Bleu foncé pour le texte */
        }

        .bottom-text {
            color: yellow; /* Jaune pour le texte en bas */
        }

        h1, h2, h3, h4, h5, h6 {
            color: yellow;  /* Assurez-vous que tous les titres sont en jaune */
        }

        input, select {
            background-color: #00509E;  /* Fond bleu clair pour les champs */
            color: yellow;              /* Texte des champs jaune */
        }

        .center-text {
            text-align: center;
        }
            
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 {
            max-width: 90rem
        }

    </style>
""", unsafe_allow_html=True)


if "rows" not in st.session_state:
    st.session_state.rows = [{"mode_transport": "", "type_vehicule": "", "ville_depart": "", "ville_arrivee": ""}]

def add_row():
    st.session_state.rows.append({"mode_transport": "", "type_vehicule": "", "ville_depart": "", "ville_arrivee": ""})

if st.button("Ajouter une ligne"):
    add_row()

for i, row in enumerate(st.session_state.rows):
    col1, col2, col3, col4 = st.columns([10, 10, 14, 14])

    with col1:
        row["mode_transport"] = st.selectbox("Mode de transport", ["Route", "Train", "Avion"], index=["Route", "Train", "Avion"].index(row["mode_transport"]) if row["mode_transport"] else 0, key=f"mode_transport_{i}")

    with col2:
        if row["mode_transport"] == "Route":
            row["type_vehicule"] = st.selectbox(
                "Type de véhicule", 
                ["2 Roues Motrices", "Bus", "Poids lourd", "Véhicule utilitaire", "Voiture"],
                key=f"type_vehicule_route_{i}"
            )
        elif row["mode_transport"] == "Train":
            row["type_vehicule"] = st.selectbox(
                "Type de train", 
                ["TER", "TGV", "Intercités"],
                key=f"type_vehicule_train_{i}"
            )
        elif row["mode_transport"] == "Avion":
            row["type_vehicule"] = st.selectbox(
                "Type avion", 
                [],
                key=f"type_vehicule_avion_{i}"
            )
    with col3:
        if row["mode_transport"] == "Route":
            row["ville_depart"] = st.selectbox('Ville de départ', villes, key=f"selectbox_depart{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TER':
            row["ville_depart"] = st.selectbox('Gare de départ', villes, key=f"selectbox_depart{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TGV':
            row["ville_depart"] = st.selectbox('Gare de départ', gares_tgv, key=f"selectbox_depart{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'Intercités':
            row["ville_depart"] = st.selectbox('Gare de départ', gares_intercites, key=f"selectbox_depart{i}")
        elif row["mode_transport"] == "Avion":
            row["ville_depart"] = st.selectbox('Aéroport de départ', avions, key=f"selectbox_depart{i}")

    with col4:
        if row["mode_transport"] == "Route":
            row["ville_arrivee"] = st.selectbox("Ville d'arrivée", villes, key=f"selectbox_arrivee{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TER':
            row["ville_arrivee"] = st.selectbox("Gare d'arrivée", villes, key=f"selectbox_arrivee{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TGV':
            row["ville_arrivee"] = st.selectbox("Gare d'arrivée", gares_tgv, key=f"selectbox_arrivee{i}")
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'Intercités':
            row["ville_arrivee"] = st.selectbox("Gare d'arrivée", gares_intercites, key=f"selectbox_arrivee{i}")
        elif row["mode_transport"] == "Avion":
            row["ville_arrivee"] = st.selectbox("Aéroport d'arrivée", avions, key=f"selectbox_arrivee{i}")
    
    st.markdown("<div class='line-spacing'></div>", unsafe_allow_html=True)

total_empreinte = 0
messages_erreur = []

for row in st.session_state.rows:
    if row["ville_depart"] and row["ville_arrivee"]:
        if row["mode_transport"] == "Route":
            # Calculate distance between the two cities
            distance = calculer_distance(row["ville_depart"], row["ville_arrivee"])

            # Apply the appropriate coefficient based on the vehicle type
            if row["type_vehicule"] == "2 Roues Motrices":
                coeff_2rm =  1.594333 
                empreinte_route = distance * coeff_2rm
                total_empreinte += empreinte_route

            elif row["type_vehicule"] == "Autocar":
                coeff_autocar = 0.803152/30  
                empreinte_route = distance * coeff_autocar
                total_empreinte += empreinte_route

            elif row["type_vehicule"] == "Bus":
                coeff_bus = 1.063000/30  
                empreinte_route = distance * coeff_bus
                total_empreinte += empreinte_route

            elif row["type_vehicule"] == "Poids lourd":
                coeff_pl = 0.523545  
                empreinte_route = distance * coeff_pl
                total_empreinte += empreinte_route

            elif row["type_vehicule"] == "Véhicule utilitaire":
                coeff_vul = 0.252545
                empreinte_route = distance * coeff_vul
                total_empreinte += empreinte_route

            elif row["type_vehicule"] == "Voiture":
                coeff_voiture = 0.938192/2.2  
                empreinte_route = distance * coeff_voiture
                total_empreinte += empreinte_route

        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TER':
            empreinte_ter = calculer_distance(row['ville_depart'], row['ville_arrivee']) * trains[trains['Transporteur'] == row["type_vehicule"]]['Train'].mean()
            total_empreinte += empreinte_ter
        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'TGV':
            filtre_tgv = trains_avions[
                ((trains_avions['Origine'] == row['ville_depart']) & (trains_avions['Destination'] == row['ville_arrivee'])) |
                ((trains_avions['Origine'] == row['ville_arrivee']) & (trains_avions['Destination'] == row['ville_depart']))
            ]
            filtre_tgv = filtre_tgv[filtre_tgv['Transporteur'] == 'TGV']

            if not filtre_tgv.empty:
                empreinte_tgv = round(filtre_tgv["Train - Empreinte carbone (kgCO2e)"].iloc[0],3)
                total_empreinte += empreinte_tgv
            else:
                messages_erreur.append(f"Il n'y a pas de trajet en TGV enregistré pour l'itinéraire {row['ville_depart']} -> {row['ville_arrivee']}.")

        elif row["mode_transport"] == "Train" and row["type_vehicule"] == 'Intercités':
            filtre_intercites = trains_avions[
                ((trains_avions['Origine'] == row['ville_depart']) & (trains_avions['Destination'] == row['ville_arrivee'])) |
                ((trains_avions['Origine'] == row['ville_arrivee']) & (trains_avions['Destination'] == row['ville_depart']))
            ]
            filtre_intercites = filtre_intercites[filtre_intercites['Transporteur'] == 'Intercités']

            if not filtre_intercites.empty:
                empreinte_intercites = round(filtre_intercites["Train - Empreinte carbone (kgCO2e)"].iloc[0],3)
                total_empreinte += empreinte_intercites
            else:
                messages_erreur.append(f"Il n'y a pas de trajet en Intercités enregistré pour l'itinéraire {row['ville_depart']} -> {row['ville_arrivee']}.")

        elif row["mode_transport"] == "Avion":
            filtre_avion = trains_avions[
                ((trains_avions['Origine'] == row['ville_depart']) & (trains_avions['Destination'] == row['ville_arrivee'])) |
                ((trains_avions['Origine'] == row['ville_arrivee']) & (trains_avions['Destination'] == row['ville_depart']))
            ]

            if not filtre_avion.empty:
                empreinte_avion = round(filtre_avion["Avion - Empreinte carbone (kgCO2e)"].iloc[0],3)
                total_empreinte += empreinte_avion
            else:
                messages_erreur.append(f"Il n'y a pas de trajet en avion enregistré pour l'itinéraire {row['ville_depart']} -> {row['ville_arrivee']}.")

st.markdown(f"<h3 class='title-text' style='text-align: center; font-size:45px'>{round(total_empreinte), 3} kg de CO2</h3>", unsafe_allow_html=True)

if messages_erreur:
    st.markdown("<h3 class='title-text' style='text-align: center; color: red;'>Messages d'erreur</h3>", unsafe_allow_html=True)
    for message in messages_erreur:
        st.markdown(f"<p style='color: red; text-align: center; font-size: 18px'>{message}</p>", unsafe_allow_html=True)

# Initialiser la navigation
def navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Sélectionnez une page", ["Formulaire de Transport", "Mes Études"])

    if page == "Mes Études":
        afficher_page_etudes()

# Appel de la fonction de navigation
if __name__ == "__main__":  
    navigation()  