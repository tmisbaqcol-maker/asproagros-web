import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="ASPROAGROS",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Asociación de Productores Agrícolas de Santa Cruz")
st.subheader("ASPROAGROS")

st.markdown("""
**NIT:** 901.117.531-1  
**Ubicación:** Santa Cruz - Luruaco, Atlántico  
**Contacto:** +57 3205822216  
""")

menu = st.sidebar.selectbox(
    "Menú",
    [
        "Inicio",
        "Producción",
        "Avicultura",
        "Comunidad",
        "Documentos"
    ]
)

# Carpeta de imágenes
img = Path("images")

# -------- INICIO -------- #

if menu == "Inicio":

    col1, col2 = st.columns(2)

    with col1:
        st.image(img / "WhatsApp Image 2026-02-20 at 10.33.46 AM.jpeg")

    with col2:
        st.markdown("""
### ASPROAGROS

Asociación de productores agrícolas del corregimiento **Santa Cruz – Luruaco**.

Cultivamos:

- Plátano
- Ñame
- Mango
- Limón
- Ají
- Yuca
        """)

# -------- PRODUCCIÓN -------- #

if menu == "Producción":

    st.header("Producción Agrícola")

    st.image(img / "WhatsApp Image 2026-02-23 at 1.09.39 PM.jpeg")

    st.markdown("""
Los productores de la asociación trabajan principalmente en cultivos de:

- Plátano
- Ñame
- Yuca
- Mango
- Limón
""")

# -------- AVICULTURA -------- #

if menu == "Avicultura":

    st.header("Producción Avícola")

    col1, col2 = st.columns(2)

    with col1:
        st.image(img / "WhatsApp Image 2026-02-23 at 1.09.41 PM (1).jpeg")

    with col2:
        st.image(img / "WhatsApp Image 2026-02-23 at 1.09.41 PM (2).jpeg")

    st.image(img / "WhatsApp Image 2026-02-23 at 1.09.41 PM.jpeg")

# -------- COMUNIDAD -------- #

if menu == "Comunidad":

    st.header("Trabajo Comunitario")

    st.image(img / "WhatsApp Image 2026-02-23 at 1.09.40 PM.jpeg")

    st.image(img / "WhatsApp Image 2026-02-23 at 1.09.40 PM (1).jpeg")

    st.markdown("""
La asociación también desarrolla procesos organizativos,
reuniones comunitarias y fortalecimiento del trabajo campesino.
""")

# -------- DOCUMENTOS -------- #

if menu == "Documentos":

    st.header("Documentos Institucionales")

    st.download_button(
        "Informe de Gestión",
        open("data/ACTIVIDADES DE INFORME DE GESTIÓN.pdf","rb"),
        file_name="informe_gestion.pdf"
    )

    st.download_button(
        "Resolución ANT",
        open("data/RESOLUCION DE INCLUSION-1106-ASOCIACION DE PRODUCTORES AGRICOLAS DE SANTA CRUZ SIGLA.pdf","rb"),
        file_name="resolucion_ant.pdf"
    )

    st.download_button(
        "Estados Financieros",
        open("data/balance, estado de resultados y rut ASPROAGROS.pdf","rb"),
        file_name="balance.pdf"
    )
