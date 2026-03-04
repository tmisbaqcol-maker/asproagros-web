# ✅ PEGAR TODO ESTE BLOQUE EN TU ARCHIVO PRINCIPAL (asproagros-web.py)
# Incluye: rutas correctas para Streamlit Cloud, debug en sidebar, carga robusta de imágenes
# usando NOMBRES ORIGINALES, y descargas de PDFs con rutas seguras.

import streamlit as st
from pathlib import Path

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="ASPROAGROS", page_icon="🌱", layout="wide")

BASE_DIR = Path(__file__).parent                # carpeta donde está asproagros-web.py
IMG_DIR  = BASE_DIR / "images"                 # debe existir en el repo
DATA_DIR = BASE_DIR / "data"                   # debe existir en el repo

# ---------------- DEBUG (Sidebar) ---------------- #
st.sidebar.markdown("## 🔧 Diagnóstico")
st.sidebar.write("📄 Script:", str(BASE_DIR))
st.sidebar.write("🖼️ images/:", str(IMG_DIR))
st.sidebar.write("📦 data/:", str(DATA_DIR))

if IMG_DIR.exists():
    img_files = sorted([p.name for p in IMG_DIR.iterdir() if p.is_file()])
    st.sidebar.success(f"✅ images/ existe ({len(img_files)} archivos)")
    st.sidebar.write(img_files)
else:
    st.sidebar.error("❌ No existe la carpeta images/ en el repo (debe estar commiteada).")

if DATA_DIR.exists():
    data_files = sorted([p.name for p in DATA_DIR.iterdir() if p.is_file()])
    st.sidebar.success(f"✅ data/ existe ({len(data_files)} archivos)")
    st.sidebar.write(data_files)
else:
    st.sidebar.error("❌ No existe la carpeta data/ en el repo (debe estar commiteada).")

# ---------------- HELPERS ---------------- #
def show_image(original_name: str, caption: str | None = None):
    """Carga imagen por nombre original desde images/ con error claro si falta."""
    path = IMG_DIR / original_name
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.error(f"❌ No se encontró la imagen: `{original_name}`")
        st.info(f"Ruta buscada: `{path}`")
        if IMG_DIR.exists():
            disponibles = sorted([p.name for p in IMG_DIR.iterdir() if p.is_file()])
            st.info("📌 Imágenes disponibles en `images/`:")
            st.write(disponibles)
        else:
            st.warning("📌 Crea la carpeta `images/` en el repo y súbela a GitHub.")

def download_pdf(original_name: str, label: str):
    """Botón de descarga de PDF desde data/ con rutas seguras."""
    path = DATA_DIR / original_name
    if path.exists():
        with open(path, "rb") as f:
            st.download_button(label=label, data=f, file_name=original_name, mime="application/pdf")
    else:
        st.error(f"❌ No se encontró el PDF: `{original_name}`")
        st.info(f"Ruta buscada: `{path}`")
        if DATA_DIR.exists():
            disponibles = sorted([p.name for p in DATA_DIR.iterdir() if p.is_file()])
            st.info("📌 Archivos disponibles en `data/`:")
            st.write(disponibles)
        else:
            st.warning("📌 Crea la carpeta `data/` en el repo y súbela a GitHub.")

# ---------------- UI ---------------- #
st.title("🌱 Asociación de Productores Agrícolas de Santa Cruz")
st.subheader("ASPROAGROS")

st.markdown("""
**NIT:** 901.117.531-1  
**Ubicación:** Santa Cruz - Luruaco, Atlántico, Colombia  
**Contacto:** +57 3205822216  
""")

menu = st.sidebar.selectbox(
    "Menú",
    ["Inicio", "Producción", "Avicultura", "Comunidad", "Documentos"]
)

# ---------------- PÁGINAS ---------------- #
if menu == "Inicio":
    col1, col2 = st.columns(2)
    with col1:
        show_image("WhatsApp Image 2026-02-20 at 10.33.46 AM.jpeg", "Encuentro comunitario")
    with col2:
        st.markdown("""
### Bienvenidos a ASPROAGROS
Asociación de productores agrícolas del corregimiento **Santa Cruz – Luruaco**.

**Líneas productivas:**
- Plátano
- Ñame
- Mango
- Limón
- Yuca
- Ají
""")

elif menu == "Producción":
    st.header("🌾 Producción Agrícola")
    show_image("WhatsApp Image 2026-02-23 at 1.09.39 PM.jpeg", "Producción agrícola")
    st.markdown("""
Fortalecemos la seguridad alimentaria con cultivos como:
- Plátano, ñame, yuca, mango, limón y ají.
""")

elif menu == "Avicultura":
    st.header("🐔 Producción Avícola")
    c1, c2 = st.columns(2)
    with c1:
        show_image("WhatsApp Image 2026-02-23 at 1.09.41 PM (1).jpeg", "Galpón avícola")
    with c2:
        show_image("WhatsApp Image 2026-02-23 at 1.09.41 PM (2).jpeg", "Manejo avícola")
    show_image("WhatsApp Image 2026-02-23 at 1.09.41 PM.jpeg", "Producción avícola")

elif menu == "Comunidad":
    st.header("🤝 Trabajo Comunitario")
    show_image("WhatsApp Image 2026-02-23 at 1.09.40 PM.jpeg", "Reunión / organización")
    show_image("WhatsApp Image 2026-02-23 at 1.09.40 PM (1).jpeg", "Gestión comunitaria")
    st.markdown("""
La asociación desarrolla reuniones, organización campesina y actividades de fortalecimiento comunitario.
""")

elif menu == "Documentos":
    st.header("📄 Documentos Institucionales")

    download_pdf("ACTIVIDADES DE INFORME DE GESTIÓN.pdf", "⬇️ Descargar Informe de Gestión (PDF)")
    download_pdf(
        "RESOLUCION DE INCLUSION-1106-ASOCIACION DE PRODUCTORES AGRICOLAS DE SANTA CRUZ SIGLA.pdf",
        "⬇️ Descargar Resolución ANT (PDF)"
    )
    download_pdf("balance, estado de resultados y rut ASPROAGROS.pdf", "⬇️ Descargar Estados Financieros + RUT (PDF)")
    download_pdf("CERTIFICACION ASPROAGROS.pdf", "⬇️ Descargar Certificación Contador (PDF)")

# ---------------- NOTA IMPORTANTE ---------------- #
st.caption("✅ Si alguna imagen/PDF no aparece, revisa el sidebar (Diagnóstico) para ver qué archivos detectó Streamlit Cloud.")
