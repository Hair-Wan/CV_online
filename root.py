import streamlit as st
print()
print('Debug -------------')
pages = {
    "CV": [
        st.Page("accueil.py", title="👨‍💻 Accueil"),
        st.Page("projets.py", title="🖥️ Mes projets"),
        st.Page("skills.py", title="🛠️ Mes skills"),
        st.Page("contact.py", title="📬 Me contacter")
    ],
    "Automatisation": [
        st.Page("automation.py", title="🚀 Automatise tes processsus"),
    ],
}

pg = st.navigation(pages)
pg.run()