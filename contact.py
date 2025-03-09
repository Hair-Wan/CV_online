import streamlit as st
st.title("Contact")



with st.container(border=True):
    st.header("Mes coodonées :", divider="gray")
    st.write("📞 07 86 57 06 93")
    st.write("📧 blanchet.erwan@hotmail.com")


with st.expander("📍 Voir les coordonnées"):
    st.write("📌 **Adresse :** 123, Rue de la Tech, Paris, France")
    st.write("📞 **Téléphone :** +33 1 23 45 67 89")
    st.write("✉️ **Email :** contact@exemple.com")
st.divider()