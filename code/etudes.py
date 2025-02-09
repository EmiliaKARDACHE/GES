
import streamlit as st

def afficher_page_etudes():
    st.title("Nos Études 📚")  
    st.write("Bienvenue sur la page dédiée à nos études. Voici quelques informations utiles.")
    
    images = [
        ("ETUDE ALEX ......", "../images/image1.png"),
        ("ETUDE ERIC ......", "../images/image2.png"),
        ("ETUDE EMILIA .....", "../images/image3.png"),
        ("ETUDE EMILIA .....", "../images/image4.png"),
    ]
    
    for description, image in images:
        st.write(f"**{description}**")  # Texte en gras
        st.image(image, use_container_width=True)




