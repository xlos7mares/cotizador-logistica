import streamlit as st

# --- TARIFAS ACTUALIZADAS SEGÚN AUDIO DE GUSTAVO ---
#
TARIFA_GENERAL_KM = 55.0  # Para mudanzas, mercaderías, objetos
TARIFA_BARCOS_KM = 80.0    # Para lanchas y cruceros

st.title("🚛 Conexión Logística Sur")

# 1. ESTO ES LO QUE TE FALTA: Un selector para cambiar el rubro
rubro = st.radio(
    "¿Qué tipo de carga desea cotizar?",
    ["📦 Mercadería / Mudanza / Objeto", "🚤 Embarcación"],
    horizontal=True
)

st.markdown("---")

# 2. Lógica para que aparezcan las opciones correctas
if rubro == "📦 Mercadería / Mudanza / Objeto":
    # Aquí es donde aparecen las opciones que no veías
    tipo_carga = st.selectbox(
        "Detalle de la carga:",
        ["Mudanza Residencial", "Mercadería Comercial", "Pallets / Bultos", "Objeto Especial"]
    )
    distancia = st.number_input("Kilómetros a recorrer (km):", min_value=1.0, step=1.0)
    total = distancia * TARIFA_GENERAL_KM
    st.info(f"Aplicando tarifa de Gustavo: **${TARIFA_GENERAL_KM} por km**")

else:
    # Esto es lo que te aparece ahora (Lanchas)
    tipo_lancha = st.selectbox(
        "Tipo de embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies / 10 Ton)"]
    )
    distancia = st.number_input("Kilómetros a recorrer (km):", min_value=1.0, step=1.0)
    total = distancia * TARIFA_BARCOS_KM
    st.info(f"Aplicando tarifa de Embarcación: **${TARIFA_BARCOS_KM} por km**")

# 3. Resultado Final Impactante
st.markdown("### COSTO TOTAL ESTIMADO")
st.markdown(f"<h1 style='color: #007BFF;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Firma profesional
st.sidebar.write(f"**Desarrollador:** Leonardo Olivera")
st.sidebar.caption("Software & IA - Estudiante de Agronomía")
