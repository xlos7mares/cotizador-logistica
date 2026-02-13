import streamlit as st

# --- CONFIGURACIÓN CRÍTICA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛")

# --- TARIFAS ACTUALIZADAS (AUDIO GUSTAVO) ---
TAR_MUDANZA = 55.0  # El precio que pidió Gustavo por km
TAR_BARCO = 80.0

# --- FIRMA PROFESIONAL ---
st.sidebar.write("### 👨‍💻 Desarrollador")
st.sidebar.info("Leonardo Olivera\n\nDesarrollador IA & Software")

st.markdown("<h1 style='text-align: center;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)

# --- FORZAR VISIBILIDAD DE MUDANZAS ---
# Usamos radio buttons porque son más difíciles de ignorar por la caché
servicio = st.radio(
    "ELIJA EL TIPO DE TRASLADO:",
    ["MUDANZAS / MERCADERÍAS / OBJETOS", "EMBARCACIONES"],
    index=0  # Esto fuerza a que Mudanza sea lo primero que se ve
)

st.markdown("---")

if servicio == "MUDANZAS / MERCADERÍAS / OBJETOS":
    st.subheader("📦 Cotización de Carga General")
    detalle = st.text_input("¿Qué objeto de valor desea trasladar?", "Mudanza / Mercadería")
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0)
    
    # CÁLCULO EXACTO SOLICITADO
    total = distancia * TAR_MUDANZA
    
    st.success(f"Tarifa Especial: ${TAR_MUDANZA} por kilómetro")

else:
    st.subheader("🚤 Cotización de Embarcaciones")
    lancha = st.selectbox("Tamaño:", ["Lancha chica", "Crucero mediano", "Embarcación Grande"])
    distancia = st.number_input("Kilómetros totales (km):", min_value=1.0, value=1.0)
    
    total = distancia * TAR_BARCO
    st.info(f"Tarifa Embarcación: ${TAR_BARCO} por kilómetro")

# --- RESULTADO ---
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>Costo Estimado:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #1565C0;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

if st.button("📲 ENVIAR COTIZACIÓN A GUSTAVO"):
    st.balloons()
