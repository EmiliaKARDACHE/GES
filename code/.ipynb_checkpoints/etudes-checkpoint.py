
import streamlit as st
import os

def afficher_page_etudes():
    st.title("Nos Études 📚")  
    st.write("Bienvenue sur la page dédiée à nos études. Voici quelques informations utiles.")
    
    images = [
        
        ("Alex .....", os.path.join("..", "images", "image1.png")),
        
        ("ETUDE ERIC ......", "..\images\image2.png"),
        
        ("Cette carte montre les émissions de GES des trajets domicile-travail par département en France. On remarque que certains départements comme l'Eure-et-            Loir (28), l'Eure (27), et l'Oise (60) ont des émissions plus élevées, indiquées par des couleurs foncées. À l'inverse, l'Île-de-France, notamment               Paris et ses environs, affiche des niveaux d'émissions plus faibles, probablement grâce à une meilleure utilisation des transports en commun. Cette              carte met  en évidence les différences d'empreinte carbone selon les régions, influencées par la mobilité et l'accessibilité.",                                  "..\images\image3.png"), 
        
          ("Lorsque l'on multiplie les émissions de GES par la population de chaque région, les résultats changent significativement. Les régions à forte                   population, comme l'Île-de-France, Auvergne-Rhône-Alpes, Hauts-de-France, et Nouvelle-Aquitaine, voient leurs émissions augmenter, car elles comptent            une grande densité de population ce qui est assez logique. Ainsi, même si ces régions avaient des émissions faibles par habitant, leur grande                    population entraîne des émissions totales plus élevées.", "..\images\image4.png"),   
    ]

    for description, image in images:
        chemin_absolu = os.path.abspath(image)  # Convertir en chemin absolu
        
        if os.path.exists(chemin_absolu):  # Vérifier si l'image existe
            st.write(f"**{description}**")  # Texte en gras
            st.image(chemin_absolu, use_container_width=True)
        else:
            st.warning(f"⚠️ Image introuvable : {chemin_absolu}")  





