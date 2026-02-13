import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Presupuestador Oficial", page_icon="🚛")

# --- TARIFAS ACTUALIZADAS SEGÚN GUSTAVO ---
#
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0   

# --- TU FIRMA PROFESIONAL ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")

st.markdown("<h1 style='text-align: center; color: #01579b;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- SELECCIÓN POR CÍRCULOS (RADIO) ---
st.markdown("### 1. ¿Qué tipo de traslado necesita cotizar?")
rubro = st.radio(
    "Seleccione una categoría:",
    ["📦 Mudanzas, Mercaderías u Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    index=0,
    horizontal=True
)

st.markdown("---")

if "📦 Mudanzas" in rubro:
    st.subheader("Configuración de Carga General")
    tipo_detalle = st.selectbox(
        "Detalle del objeto:",
        ["Mudanza", "Mercadería", "Objetos de Valor", "Maquinaria Liviana"]
    )
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0, key="km_muda")
    
    # CÁLCULO A 55 PESOS EL KM
    total = distancia * TARIFA_MUDANZA_KM
    st.success(f"Tarifa autorizada: **${TARIFA_MUDANZA_KM} por km**")

else:
    st.subheader("Configuración de Náutica")
    tipo_detalle = st.selectbox(
        "Categoría de embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies)"]
    )
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0, key="km_lancha")
    
    total = distancia * TARIFA_BARCO_KM
    st.info(f"Tarifa Náutica: **${TARIFA_BARCO_KM} por km**")

# --- RESULTADO FINAL ---
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>Presupuesto Estimado:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Registro de foto
st.subheader("📷 Foto del objeto")
st.file_uploader("Suba una imagen para validar dimensiones", type=['png', 'jpg', 'jpeg'])

if st.button("📲 SOLICITAR POR WHATSAPP"):
    st.balloons()
