import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- TARIFAS ACTUALIZADAS SEGÚN GUSTAVO ---
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0   

# --- LOGO Y TÍTULO CON ICONOS ---
# Usamos columnas para que los iconos queden a los lados del nombre
st.write("")
col_logo1, col_logo2, col_logo3 = st.columns([1, 4, 1])

with col_logo1:
    st.markdown("<h1 style='text-align: right;'>🚢</h1>", unsafe_allow_html=True) # Icono Barco

with col_logo2:
    st.markdown("<h1 style='text-align: center; color: #01579b; font-family: sans-serif;'>CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)

with col_logo3:
    st.markdown("<h1 style='text-align: left;'>🚛</h1>", unsafe_allow_html=True) # Icono Camión

st.markdown("<p style='text-align: center; color: gray;'>Servicios de Transporte Nacional e Internacional</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SELECCIÓN POR CÍRCULOS (RADIO BUTTONS) ---
st.markdown("### 🛠️ Seleccione el rubro del traslado:")
rubro = st.radio(
    "Elija una categoría para calcular su presupuesto:",
    ["📦 Mudanzas, Mercaderías u Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    index=0,
    horizontal=True
)

st.markdown("---")

# --- LÓGICA DE SERVICIOS ---
if "📦 Mudanzas" in rubro:
    st.subheader("📋 Detalle de Carga General")
    tipo_detalle = st.selectbox(
        "¿Qué tipo de objeto o mercadería traslada?",
        ["Mudanza Particular", "Mercadería Comercial", "Objetos de Valor", "Varios"]
    )
    distancia = st.number_input("Kilómetros totales del recorrido (km):", min_value=1.0, value=1.0, key="km_muda")
    
    # CÁLCULO A 55 PESOS EL KM
    total = distancia * TARIFA_MUDANZA_KM
    st.success(f"Tarifa autorizada: **${TARIFA_MUDANZA_KM} por km**")

else:
    st.subheader("📋 Detalle de Náutica")
    tipo_detalle = st.selectbox(
        "Categoría de la embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies / 10 Ton)"]
    )
    distancia = st.number_input("Kilómetros totales del recorrido (km):", min_value=1.0, value=1.0, key="km_lancha")
    
    # CÁLCULO A 80 PESOS EL KM
    total = distancia * TARIFA_BARCO_KM
    st.info(f"Tarifa Náutica: **${TARIFA_BARCO_KM} por km**")

# --- RESULTADO DEL PRESUPUESTO ---
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>Presupuesto Estimado:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Registro de foto (Visual)
st.subheader("📷 Registro Fotográfico")
st.file_uploader("Suba una imagen para validar dimensiones y peso", type=['png', 'jpg', 'jpeg'])

if st.button("📲 SOLICITAR COTIZACIÓN POR WHATSAPP"):
    st.balloons()
    st.success("Preparando datos para enviar a Leonardo Olivera...")

# --- FIRMA PROFESIONAL EN EL SIDEBAR ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")
st.sidebar.caption("Agro Data Litoral")
