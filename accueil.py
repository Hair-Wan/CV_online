import streamlit as st
from datetime import datetime
st.title("Bienvenue sur mon CV en ligne")
st.divider()
# ---------------------------------------------------------------------------------

st.write("Lien vers le reste de mon CV")
projet, skills, contact = st.columns(3)
with projet:
    st.page_link("projets.py")
with skills:
    st.page_link("skills.py")
with contact:
    st.page_link("contact.py")
    
st.divider()

st.write("Autres liens utiles")
# Charger l’image GitHub
st.image("image/icon_github.png")
path_icon_github = "image\icon_github.png"
st.markdown(f"""
    <a href="https://github.com/Hair-Wan" target="_blank">
        <img src="{path_icon_github}" width="50">
    </a>
""", unsafe_allow_html=True)
# ---------------------------------------------------------------------------------

st.markdown('---')
col1, col2, col3 = st.columns([1,1,1]) # colonne de la même taille
with col1:
    st.image("image/profil_picture.jpg", caption="Erwan Blanchet profil picture")
with col2:
    st.write("Erwan")
    st.write("Blanchet")
    current_date = datetime.now() # récupération de la data actuelle
    birth_date = datetime(2004, 10, 5)
    age = current_date.year - birth_date.year # calcul des années bruts

    # notre anniversaire n'est pas forcément passé donc nous enlevons un an si notre moi et jour n'est pas encore passé
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day): # si anniversaire pas encore passé
        age -= 1
    st.write(age)
with col3:
    with open("documents\CV_Blanchet-Erwan.pdf", "rb") as file:
        contenu_pdf = file.read()
    st.download_button(
        label="Télécharger mon cv",
        data=contenu_pdf,
        mime="application/pdf",
        file_name="CV_Erwan_Blanchet.pdf",
        icon=":material/download:",
    )

st.divider()
