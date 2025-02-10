
import streamlit as st
import os

def afficher_page_etudes():
    st.title("Nos Études 📚")  
    st.write("Bienvenue sur la page dédiée à nos études. Voici quelques informations utiles.")
    
    images = [
        ("ETUDE ALEX ......", "image1.png"),
        ("ETUDE ERIC ......", "image2.png"),
        ("ETUDE EMILIA .....", "image3.png"),
        ("ETUDE EMILIA .....", "image4.png"),   
    ]

    for description, image in images:
        chemin_absolu = os.path.abspath(image)  # Convertir en chemin absolu
        
        if os.path.exists(chemin_absolu):  # Vérifier si l'image existe
            st.write(f"**{description}**")  # Texte en gras
            st.image(chemin_absolu, use_container_width=True)
        else:
            st.warning(f"⚠️ Image introuvable : {chemin_absolu}") 





