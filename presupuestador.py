import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Presupuestador Oficial", page_icon="🚛")

# --- TARIFAS ACTUALIZADAS (PEDIDO GUSTAVO) ---
PRECIO_MUDANZA_KM = 55.0  
PRECIO_BARCOS_KM = 80.0   

# --- FIRMA DE LEONARDO ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")

st.markdown("<h1 style='text-align: center; color: #01579b;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- ESTA ES LA OPCIÓN DE CÍRCULOS (RADIO) ---
st.markdown("### 1. Seleccione el rubro del servicio:")
rubro = st.radio(
    "Elija una categoría:",
    ["📦 Mudanzas / Mercaderías / Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    index=0,
    horizontal=True
)

st.markdown("---")

if "📦 Mudanzas" in rubro:
    st.subheader("Configuración de Carga General")
    tipo_detalle = st.selectbox(
        "Detalle del traslado:",
        ["Mudanza", "Mercadería Comercial", "Objetos de Valor", "Varios"]
    )
    distancia = st.number_input("Distancia en Kilómetros (km):", min_value=1.0, value=1.0, key="km_muda")
    
    # EL COSTO DE GUSTAVO: $55 el km
    total = distancia * PRECIO_MUDANZA_KM
    st.success(f"Tarifa: **${PRECIO_MUDANZA_KM} por km**")

else:
    st.subheader("Configuración de Náutica")
    tipo_detalle = st.selectbox(
        "Categoría:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande"]
    )
    distancia = st.number_input("Distancia en Kilómetros (km):", min_value=1.0, value=1.0, key="km_lancha")
    
    total = distancia * PRECIO_BARCOS_KM
    st.info(f"Tarifa: **${PRECIO_BARCOS_KM} por km**")

# --- RESULTADO ---
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>Presupuesto Estimado:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Registro de foto
st.subheader("📷 Foto del objeto")
st.file_uploader("Suba una imagen para validar el presupuesto", type=['png', 'jpg', 'jpeg'])

if st.button("📲 SOLICITAR POR WHATSAPP"):
    st.balloons()
