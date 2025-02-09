
import streamlit as st

def afficher_page_etudes():
    st.title("Nos Études 📚")  
    st.write("Bienvenue sur la page dédiée à nos études. Voici quelques informations utiles.")
    
    images = [
    ("ETUDE ALEX ......", "Final/images/image1.png"),
    ("ETUDE ERIC ......", "Final/images/image2.png"),
    ("ETUDE EMILIA .....", "Final/images/image3.png"),
    ("ETUDE EMILIA .....", "Final/images/image4.png"),
]
    
    for description, image in images:
        st.write(f"**{description}**")  # Texte en gras
        st.image(image, use_container_width=True)




