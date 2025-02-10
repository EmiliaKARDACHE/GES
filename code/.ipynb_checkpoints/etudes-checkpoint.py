
import streamlit as st
import os

def afficher_page_etudes():
    st.title("Nos Études 📚")  
   
    
    images = [
        
        ("Le graphique ci-dessous montre les émissions de gaz à effet de serre par kilomètre et par personne selon le mode de transport. Ce qui ressort                     clairement, c'est que le train génère beaucoup moins d'émissions par rapport à des modes de transport plus courants comme la voiture ou le bus.",                "..\images\image1.png"),
        
        ("Le graphique montre que les 2RM émettent le plus de CO, tandis que les autocars, bus et poids lourds ont les émissions de NOx les plus élevées,                    probablement en raison de l’usage du diesel. Les voitures et VUL ont des émissions plus modérées, mais leur grand nombre contribue fortement à la                pollution globale. Les bus et autocars, bien que plus polluants par véhicule, restent plus efficaces par passager transporté.",                                  "..\images\image2.png"),
        
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





