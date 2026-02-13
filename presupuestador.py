import streamlit as st

# Tarifas actualizadas según audio de Gustavo
TARIFA_TRASLADO_KM = 55.0  # Para mudanzas/mercaderías
TARIFA_EMBARCACION_KM = 80.0 # Para lanchas/cruceros

st.title("🚛 Conexión Logística Sur")

# 1. CAMBIO CLAVE: Primero elegimos la categoría global
categoria = st.sidebar.selectbox(
    "Seleccione el rubro:",
    ["Traslados Generales", "Embarcaciones"]
)

# 2. Lógica dinámica según la categoría elegida
if categoria == "Traslados Generales":
    # Aquí aparecen las opciones que te faltaban
    tipo_objeto = st.selectbox(
        "Tipo de traslado:",
        ["Mudanza Completa", "Mercadería / Pallets", "Objeto Particular"]
    )
    distancia = st.number_input("Distancia a recorrer (km):", min_value=1)
    total = distancia * TARIFA_TRASLADO_KM
    st.info(f"Tarifa aplicada: ${TARIFA_TRASLADO_KM} por kilómetro")

else:
    # Esta es la parte que ya tenías funcionando
    tipo_lancha = st.selectbox(
        "Tamaño de Embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande"]
    )
    distancia = st.number_input("Distancia a recorrer (km):", min_value=1)
    total = distancia * TARIFA_EMBARCACION_KM
    st.info(f"Tarifa aplicada: ${TARIFA_EMBARCACION_KM} por kilómetro")

# 3. Mostrar el resultado final
st.metric("COSTO ESTIMADO", f"${total:,.2f} UYU")

# Tu firma profesional obligatoria
st.sidebar.markdown("---")
st.sidebar.write("**Desarrollador:** Leonardo Olivera")
st.sidebar.caption("Estudiante de Agronomía | Especialista en IA")
