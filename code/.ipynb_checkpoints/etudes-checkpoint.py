import streamlit as st
import os

def afficher_page_etudes():
    st.title("Nos Études 📚")  
    st.write("Bienvenue sur la page dédiée à nos études. Voici quelques informations utiles.")
    
    # Dossier où se trouvent les images
    image_path = os.path.join("Final", "images")     

    # Liste des images et des descriptions
    images = [
        ("ETUDE ALEX ......", os.path.join(image_path, "image1.png")),
        ("ETUDE ERIC ......", os.path.join(image_path, "image2.png")),
        ("ETUDE EMILIA .....", os.path.join(image_path, "image3.png")),
        ("ETUDE EMILIA .....", os.path.join(image_path, "image4.png")),
    ]
    
    # Affichage des images
    for description, image in images:
        st.write(f"**{description}**")  # Texte en gras
        st.image(image, use_container_width=True) 





