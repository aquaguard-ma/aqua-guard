import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="AQUA-GUARD", page_icon="🐟")
st.title("🐟 AQUA-GUARD - Agadir")
st.write("Surveillance intelligente des bassins de Tilapia")

bassin = st.selectbox("Choisir le bassin:", ["Bassin 1", "Bassin 2", "Bassin 3"])
espece = st.selectbox("Choisir l'espece du poisson", ["Tilapia", "Truite","Daurate","Bar","Carpe"])
if espece == "Tilapia":
    temp_min = 25
    temp_max = 30
    oxy_min = 5
    ph_min = 6.5
    ph_max = 9.0
elif espece == "Truite":
    temp_min = 12
    temp_max = 18
    oxy_min = 6
    ph_min = 6.5
    ph_max = 8.0
elif espece == "Daurade":
    temp_min = 18
    temp_max = 24
    oxy_min = 5.5
    ph_min = 7.0
    ph_max = 8.5
else:
    temp_min = 16
    temp_max = 22
    oxy_min = 5
    ph_min = 6.5
    ph_max = 8.5
oxygene = st.slider("Oxygene dans l'eau (mg/L)", 0.0, 10.0, 7.2)
temperature = st.slider("Temperature de l'eau (C)", 10.0, 40.0, 25.0)
pH = st.slider("pH de l'eau", 0.0, 14.0, 7.0)
if oxygene >= oxy_min:
    st.success("Eau 100% Saine")
else:
    st.error("DANGER! Manque d'oxygene")
if temperature < temp_min or temperature > temp_max:
    st.error("DANGER! Eau trop chaude")
else:
    st.success("Temperatue ideale")
if pH < ph_min or pH > ph_max:
    st.error("DANGER! pH non adapte")
else:
    st.success("pH ideal")
st.divider()
st.subheader("🐟🛂 Passeport du Poisson - Pour l'Export")

col_p1, col_p2 = st.columns([1, 1])

with col_p1:
    st.markdown(f"""
    **Bassin:** {bassin}


    **Espece:** {espece}


    **Ferme:** Agadir, Maroc


    **Qualite de l'eau:** {"100% Saine" if oxygene >= 5 else "DANGER"}


    **Oxygene moyen:** {oxygene} mg/L


    Temperature:{temperature} C

    pH:{pH} 


    **Nourriture:** Naturelle, sans antibiotiques


    **Certifie par:** AQUA-GUARD
    """)
    st.success("✅ Pret pour l'Export vers l'Europe")
    if st.button("📄 Generer le Passeport QR"):
        st.balloons()
        st.write("Passeport genere!")

with col_p2:
    data_qr = f"AQUA-GUARD | {bassin} | Tilapia | Agadir-Maroc | Eau: {oxygene} mg/L Oxygene | Qualite: 100% Saine"
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(data_qr)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img_qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=220)



    