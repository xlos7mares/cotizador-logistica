import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛")

# --- TARIFAS (AUDIO GUSTAVO) ---
PRECIO_MUDANZA_KM = 55.0  
PRECIO_BARCOS_KM = 80.0   

# --- FIRMA PROFESIONAL ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")

st.markdown("<h1 style='text-align: center; color: #01579b;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- CAMBIO A BOTONES CIRCULARES (FORZA LA ACTUALIZACIÓN) ---
st.markdown("### 1. Seleccione el rubro del servicio:")
rubro = st.radio(
    "Elija una categoría:",
    ["📦 Mudanzas, Mercaderías u Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    index=0,
    horizontal=True
)

st.markdown("---")

if "📦 Mudanzas" in rubro:
    st.subheader("Configuración de Carga General")
    tipo_detalle = st.selectbox(
        "Detalle del traslado:",
        ["Mudanza", "Mercadería", "Objetos de Valor", "Maquinaria Liviana"]
    )
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0, key="km_muda")
    total = distancia * PRECIO_MUDANZA_KM
    st.success(f"Tarifa autorizada: **${PRECIO_MUDANZA_KM} por km**")

else:
    st.subheader("Configuración de Náutica")
    tipo_detalle = st.selectbox(
        "Categoría:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies)"]
    )
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0, key="km_lancha")
    total = distancia * PRECIO_BARCOS_KM
    st.info(f"Tarifa Náutica: **${PRECIO_BARCOS_KM} por km**")

# --- RESULTADO ---
st.markdown("---")
st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>Total: $ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Registro de foto (Como en tu diseño original)
st.subheader("📷 Foto del objeto")
st.file_uploader("Suba una imagen para validar dimensiones", type=['png', 'jpg', 'jpeg'])

if st.button("📲 SOLICITAR POR WHATSAPP"):
    st.balloons()
