import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ASPROAGROS",
    page_icon="🌱",
    layout="wide"
)

# TITULO
st.title("🌱 Asociación de Productores Agrícolas de Santa Cruz")
st.subheader("ASPROAGROS")

st.markdown("""
**NIT:** 901.117.531-1  
**Ubicación:** Santa Cruz - Luruaco, Atlántico, Colombia  
**Contacto:** +57 3205822216  
""")

# MENU
menu = st.sidebar.selectbox(
    "Menú",
    [
        "Inicio",
        "Sobre Nosotros",
        "Producción Agrícola",
        "Avicultura",
        "Documentos",
        "Planeación Estratégica",
        "Contacto"
    ]
)

# ---------------- INICIO ---------------- #

if menu == "Inicio":

    col1, col2 = st.columns(2)

    with col1:
        st.image("images/platano.jpg")

    with col2:
        st.markdown("""
### Bienvenidos a ASPROAGROS

Somos una **asociación de productores agrícolas** ubicada en Santa Cruz – Luruaco.

Trabajamos para fortalecer la **seguridad alimentaria, la producción agrícola sostenible y el desarrollo económico rural**.

Nuestros productores cultivan:

- Ñame
- Plátano
- Mango
- Limón
- Yuca
- Ají
        """)

# ---------------- SOBRE NOSOTROS ---------------- #

if menu == "Sobre Nosotros":

    st.header("Sobre la Asociación")

    st.markdown("""
La **Asociación de Productores Agrícolas de Santa Cruz – ASPROAGROS** fue creada el **25 de septiembre de 2017** con el objetivo de organizar y fortalecer la producción agrícola local.  
""")

    st.subheader("Misión")

    st.write("""
Promover la producción agrícola sostenible, la comercialización de productos agrícolas
y el desarrollo económico de los productores asociados.
""")

    st.subheader("Visión")

    st.write("""
Ser una asociación líder en seguridad alimentaria a nivel regional y nacional.
""")

    st.subheader("Valores")

    st.write("""
- Transparencia
- Honestidad
- Responsabilidad
- Innovación
""")

# ---------------- PRODUCCIÓN ---------------- #

if menu == "Producción Agrícola":

    st.header("Producción Agrícola")

    st.image("images/platano.jpg")

    st.markdown("""
Nuestros productores desarrollan cultivos como:

- 🌱 Plátano
- 🌱 Ñame
- 🌱 Mango
- 🌱 Limón
- 🌱 Yuca
- 🌱 Ají

Estos cultivos contribuyen a la **seguridad alimentaria regional**.
""")

# ---------------- AVICULTURA ---------------- #

if menu == "Avicultura":

    st.header("Producción Avícola")

    st.image("images/gallinas1.jpg")

    st.markdown("""
La asociación también desarrolla proyectos de **producción avícola** para fortalecer los ingresos de los productores rurales.
""")

    st.image("images/gallinas2.jpg")

# ---------------- DOCUMENTOS ---------------- #

if menu == "Documentos":

    st.header("Documentos Oficiales")

    st.markdown("""
Documentos institucionales de ASPROAGROS
""")

    st.download_button(
        "Informe de Gestión",
        open("data/informe_gestion.pdf","rb"),
        file_name="informe_gestion.pdf"
    )

    st.download_button(
        "Resolución Agencia Nacional de Tierras",
        open("data/resolucion_ant.pdf","rb"),
        file_name="resolucion_ant.pdf"
    )

    st.download_button(
        "Balance Financiero",
        open("data/balance_financiero.pdf","rb"),
        file_name="balance.pdf"
    )

# ---------------- PLANEACIÓN ---------------- #

if menu == "Planeación Estratégica":

    st.header("Planeación Estratégica")

    st.markdown("""
Ejes estratégicos de desarrollo:

1️⃣ Fortalecimiento organizacional  
2️⃣ Desarrollo productivo  
3️⃣ Comercialización  
4️⃣ Sostenibilidad ambiental  
5️⃣ Gestión de proyectos
""")

# ---------------- CONTACTO ---------------- #

if menu == "Contacto":

    st.header("Contacto")

    st.markdown("""
📍 Santa Cruz – Luruaco, Atlántico  
📞 +57 3205822216  
📧 etovarvergara@gmail.com
""")
