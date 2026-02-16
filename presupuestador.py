import streamlit as st

# --- CONFIGURACIÓN PROFESIONAL ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="wide")

# --- TARIFAS ACTUALIZADAS (AUDIO GUSTAVO 10/02) ---
TARIFA_MUDANZA_KM = 55.0  # 
TARIFA_BARCO_KM = 80.0    # 

# --- TU FIRMA PROFESIONAL ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")
st.sidebar.markdown("---")

# --- SELECTOR DE RUBRO (FORZA LA ACTUALIZACIÓN) ---
st.sidebar.header("Configuración del Servicio")
rubro = st.sidebar.radio(
    "Seleccione el rubro:",
    ["📦 Mudanzas / Mercaderías / Objetos", "🚤 Embarcaciones"],
    index=0
)

st.markdown("<h1 style='text-align: center; color: #004d40;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("---")

if "📦 Mudanzas" in rubro:
    st.header("Cotizador de Carga General")
    st.info(f"Tarifa vigente para traslados: **${TARIFA_MUDANZA_KM} por kilómetro**") # 
    
    tipo_objeto = st.selectbox(
        "¿Qué desea trasladar?",
        ["Mudanza Particular", "Mercadería / Bultos", "Objeto de Valor", "Maquinaria Liviana"]
    )
    distancia = st.number_input("Kilómetros totales de ruta (km):", min_value=1.0, value=1.0, step=1.0)
    
    # CÁLCULO A 55 PESOS EL KM 
    total = distancia * TARIFA_MUDANZA_KM

else:
    st.header("Cotizador de Náutica")
    st.info(f"Tarifa vigente para embarcaciones: **${TARIFA_BARCO_KM} por kilómetro**") # 
    
    tipo_lancha = st.selectbox(
        "Categoría de la embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies / 10 Ton)"]
    )
    distancia = st.number_input("Kilómetros totales de ruta (km):", min_value=1.0, value=1.0, step=1.0)
    
    # CÁLCULO A 80 PESOS EL KM 
    total = distancia * TARIFA_BARCO_KM

# --- RESULTADO DE IMPACTO ---
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Resumen de Cotización")
    st.write(f"**Servicio:** {rubro}")
    st.write(f"**Distancia:** {distancia} km")

with col2:
    st.markdown(f"<h2 style='text-align: center;'>COSTO TOTAL</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# --- REGISTRO FOTOGRÁFICO ---
st.markdown("---")
st.subheader("📷 Subir foto para verificación de medidas (Obligatorio)")
st.file_uploader("Drag and drop file here", type=['png', 'jpg', 'jpeg'])

if st.button("📲 ENVIAR PRESUPUESTO A WHATSAPP"):
    st.balloons()
    st.success("Enviando datos a Leonardo Olivera...")
