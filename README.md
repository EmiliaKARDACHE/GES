# 🌍 CO2 Travel Emissions Calculator 🌍

Bienvenue dans le projet **CO2 Travel Emissions Calculator** ! Ce projet permet de calculer les émissions de CO2 générées par un trajet en fonction de plusieurs critères : mode de transport, type de véhicule, et les villes de départ et d'arrivée. 🚗✈️🚉

### 🚀 Technologies utilisées
![Python](https://img.shields.io/badge/Python-3.9-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-1.7.0-orange) 
![Geopy](https://img.shields.io/badge/Geopy-2.3.0-green) 
![Pandas](https://img.shields.io/badge/Pandas-1.3.0-blueviolet)

- **Python** : Langage utilisé pour la logique du projet.
- **Streamlit** : Framework pour créer l'interface web.
- **Geopy** : Pour le calcul de la distance entre les villes.
- **Pandas** : Pour le traitement des données.

### 📦 Installation

Si tu souhaites tester ce projet localement, voici les étapes à suivre :

1. Clone ce dépôt :

   ```bash
   git clone https://github.com/tonutilisateur/CO2-Travel-Emissions-Calculator.git

2. Installe les dépendances nécessaires avec pip :

    ```bash
    pip install -r requirements.txt

  Où requirements.txt contient :
    
    streamlit
    geopy
    pandas


### ⚙️ Lancer le projet
Une fois les dépendances installées, tu peux lancer l'application avec la commande suivante :

    ```bash
    streamlit run app.py

Cela ouvrira l'application dans ton navigateur.

### 🌐 Accès en ligne
Tu peux également accéder à l'application en ligne via Streamlit Cloud : 

[Calculer mon empreinte GES](https://emiliakardache-ges-codeapp-jmjgoe.streamlit.app/) 

### 🛠️ Fonctionnement
Mode de transport : Choisis entre Route, Train ou Avion.
Type de véhicule (pour la route) : Sélectionne le type de véhicule, par exemple Véhicule utilitaire, Voiture, Bus, etc.
Ville de départ et arrivée : Indique les villes de départ et d'arrivée.
Calcul des émissions : Le projet calcule les émissions de CO2 en fonction de la distance entre les villes, du mode de transport et du type de véhicule.


### 🔧 Exemple d'utilisation
Ouvre l'application Streamlit.
Sélectionne un mode de transport (exemple : Route).
Choisis un type de véhicule (par exemple, Voiture).
Entrez Paris comme ville de départ et Lyon comme ville d'arrivée.
Clique sur Calculer pour afficher les émissions de CO2 estimées.

### 📊 Calcul des émissions
Les émissions de CO2 sont calculées à partir de la distance entre les villes, ajustées selon le mode de transport et le type de véhicule. Les valeurs sont basées sur des moyennes de consommation et des émissions standard par mode de transport.

### 📄 Contributeurs
- Emilia KARDACHE
- Alexandre GUEYDAN
- Eric COSTEROUSSE 
