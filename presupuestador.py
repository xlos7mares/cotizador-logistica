import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Conexión Logística Sur", page_icon="🚛")

# --- TARIFAS OFICIALES SEGÚN GUSTAVO ---
#
PRECIO_MUDANZA_OBJETO_KM = 55.0
PRECIO_EMBARCACION_KM = 80.0

# --- FIRMA DE LEONARDO OLIVERA ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA - Estudiante de Agronomía")
st.sidebar.caption("Agro Data Litoral")

# --- INTERFAZ PRINCIPAL ---
st.markdown("<h1 style='text-align: center;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("---")

# CAMBIO PARA QUE APAREZCA SÍ O SÍ: 
# Usamos un selectbox principal para definir el rubro
rubro_principal = st.selectbox(
    "¿Qué servicio desea cotizar hoy?",
    ["📦 Traslados (Mudanza, Mercadería u Objetos)", "🚤 Embarcaciones (Lanchas, Cruceros)"]
)

if "📦 Traslados" in rubro_principal:
    # OPCIONES QUE PIDIÓ GUSTAVO
    st.subheader("Configuración de Mudanza / Mercadería")
    opcion_detalle = st.selectbox(
        "Detalle del objeto de valor:",
        ["Mudanza Completa", "Mercadería / Bultos", "Objeto de Valor Particular", "Maquinaria Liviana"]
    )
    
    distancia = st.number_input("Ingrese los Kilómetros de viaje (km):", min_value=1.0, value=1.0, key="dist_mudanza")
    
    # CÁLCULO A 55 PESOS EL KM
    total = distancia * PRECIO_MUDANZA_OBJETO_KM
    
    st.warning(f"Tarifa para Mudanzas/Objetos: ${PRECIO_MUDANZA_OBJETO_KM} por kilómetro")

else:
    # OPCIONES DE EMBARCACIONES
    st.subheader("Configuración de Embarcación")
    opcion_detalle = st.selectbox(
        "Tipo de embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies / 10 Ton)"]
    )
    
    distancia = st.number_input("Ingrese los Kilómetros de viaje (km):", min_value=1.0, value=1.0, key="dist_lancha")
    
    # CÁLCULO A 80 PESOS EL KM
    total = distancia * PRECIO_EMBARCACION_KM
    
    st.info(f"Tarifa para Embarcaciones: ${PRECIO_EMBARCACION_KM} por kilómetro")

# --- RESULTADO FINAL ---
st.markdown("---")
st.markdown(f"### COSTO ESTIMADO PARA: {opcion_detalle}")
st.markdown(f"<h1 style='color: #2E7D32; text-align: center;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# --- BOTÓN DE WHATSAPP ---
if st.button("📲 SOLICITAR ESTE TRASLADO"):
    st.balloons()
    st.success("Conectando con el centro de logística...")
