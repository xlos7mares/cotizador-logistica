import streamlit as st

# --- CONFIGURACIÓN DE TÍTULOS ---
st.set_page_config(page_title="Conexión Logística Sur", page_icon="🚛")

# --- TU FIRMA PROFESIONAL ---
st.sidebar.markdown(f"**Desarrollador:** Leonardo Olivera")
st.sidebar.caption("Software Developer & Estudiante de Agronomía")
st.sidebar.caption("IA Avanzada - Agro Data Litoral")

# --- TARIFAS (AUDIO GUSTAVO 10/02/2026) ---
TARIFA_TRASLADOS_KM = 55.0  #
TARIFA_EMBARCACIONES_KM = 80.0 #

st.markdown("# 🚛 CONEXIÓN LOGÍSTICA SUR")

# --- EL CAMBIO QUE FALTA EN TU APP ---
# Primero definimos el GRAN RUBRO para que aparezcan las opciones de Gustavo
rubro = st.selectbox(
    "Seleccione el rubro del servicio:",
    ["Traslados Generales (Mudanza/Mercadería)", "Embarcaciones (Lanchas/Cruceros)"]
)

if rubro == "Traslados Generales (Mudanza/Mercadería)":
    # OPCIONES PARA MUDANZAS
    tipo_detalle = st.selectbox(
        "Detalle del objeto:",
        ["Mudanza", "Mercadería", "Objeto pesado", "Otros"]
    )
    distancia = st.number_input("Distancia estimada (km):", min_value=1)
    # Cálculo a 55 pesos el km según Gustavo
    costo_final = distancia * TARIFA_TRASLADOS_KM
    st.info(f"Tarifa aplicada para {tipo_detalle}: **${TARIFA_TRASLADOS_KM} / km**")

else:
    # OPCIONES PARA EMBARCACIONES (Lo que ya tenías en las capturas)
    tipo_detalle = st.selectbox(
        "Tamaño de Embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies)"]
    )
    distancia = st.number_input("Distancia estimada (km):", min_value=1)
    # Cálculo a 80 y pico según Gustavo
    costo_final = distancia * TARIFA_EMBARCACIONES_KM
    st.info(f"Tarifa aplicada para Embarcaciones: **${TARIFA_EMBARCACIONES_KM} / km**")

# --- RESULTADO FINAL ---
st.markdown("---")
st.metric(label="COSTO TOTAL ESTIMADO", value=f"${costo_final:,.2f} UYU")

# --- SUBIDA DE FOTO (Obligatorio como en tu imagen) ---
st.subheader("📷 Subir foto para verificación de medidas (Obligatorio)")
st.file_uploader("Drag and drop file here", type=['png', 'jpg', 'jpeg'])

if st.button("📲 ENVIAR A MI WHATSAPP (LEONARDO)"):
    st.success("Generando cotización...")
