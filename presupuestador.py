import streamlit as st

# --- TARIFAS OFICIALES (ACTUALIZADAS 10/02/2026) ---
# Gustavo: "Para el cálculo en internet ponele 55 pesos el kilómetro"
TARIFA_TRASLADO_KM = 55.0  
TARIFA_EMBARCACION_KM = 80.0 

st.set_page_config(page_title="Conexión Logística Sur", page_icon="🚛")

st.markdown("<h1 style='text-align: center;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Cotizador Automático de Traslados</p>", unsafe_allow_html=True)

# --- PANEL LATERAL ---
st.sidebar.header("Configuración del Viaje")
tipo_servicio = st.sidebar.selectbox(
    "¿Qué desea trasladar?", 
    ["Mudanza / Mercadería / Objeto", "Embarcación (Lancha/Crucero)"]
)

distancia = st.sidebar.number_input("Distancia a recorrer (km):", min_value=1.0, value=1.0, step=1.0)

# --- LÓGICA DE CÁLCULO ---
if tipo_servicio == "Mudanza / Mercadería / Objeto":
    tarifa_aplicada = TARIFA_TRASLADO_KM
    descripcion = "Traslado General"
else:
    tarifa_aplicada = TARIFA_EMBARCACION_KM
    descripcion = "Traslado de Embarcación"

total_cotizacion = distancia * tarifa_aplicada

# --- MOSTRAR RESULTADOS ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Resumen del Servicio")
    st.write(f"**Tipo:** {descripcion}")
    st.write(f"**Distancia:** {distancia} km")
    st.write(f"**Tarifa:** ${tarifa_aplicada} por km")

with col2:
    st.subheader("Costo Total")
    st.markdown(f"<h2 style='color: #004d40;'>${total_cotizacion:,.2f} UYU</h2>", unsafe_allow_html=True)

# --- SECCIÓN DE FOTO (Como en tu captura de pantalla) ---
st.markdown("---")
st.subheader("📷 Registro del Objeto")
foto = st.file_uploader("Suba una foto del objeto o mercadería para finalizar el presupuesto", type=['png', 'jpg', 'jpeg'])

if st.button("📲 Enviar Cotización por WhatsApp"):
    # Aquí iría la lógica del enlace de WhatsApp
    st.success("Preparando mensaje para Leonardo Olivera...")

# --- TU FIRMA PROFESIONAL ---
st.markdown("---")
st.caption("Desarrollado por: Leonardo Olivera | IA & Software Developer")
