import streamlit as st

# --- CONFIGURACIÓN DE TARIFAS (AUDIO GUSTAVO 10/02/2026) ---
# Traslados de mercadería/mudanza: $55/kg
# Traslados de embarcaciones (Tráiler propio o de la empresa): ~$80/km
TARIFA_MUDANZA_KG = 55.0
TARIFA_EMBARCACION_KM = 80.0 

def calcular_cotizacion(tipo, valor_unidad, distancia=1):
    if tipo == "Mercadería / Mudanza":
        return valor_unidad * TARIFA_MUDANZA_KG
    else:
        # Para embarcaciones el cálculo suele ser por kilómetro
        return distancia * TARIFA_EMBARCACION_KM

# --- INTERFAZ DE CONEXIÓN LOGÍSTICA SUR ---
st.markdown("<h1 style='text-align: center;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Actualización de Tarifas v2026.02</p>", unsafe_allow_html=True)

st.sidebar.header("⚙️ Parámetros de Cotización")
tipo_servicio = st.sidebar.selectbox("Tipo de Traslado:", ["Mercadería / Mudanza", "Embarcación"])

if tipo_servicio == "Mercadería / Mudanza":
    peso = st.sidebar.number_input("Peso total (kg):", min_value=1.0, value=100.0)
    total = calcular_cotizacion(tipo_servicio, peso)
    st.info(f"Tarifa aplicada para Mudanza/Mercadería: **${TARIFA_MUDANZA_KG} por kg**")
else:
    distancia = st.sidebar.number_input("Distancia del trayecto (km):", min_value=1.0, value=10.0)
    total = calcular_cotizacion(tipo_servicio, 0, distancia)
    st.info(f"Tarifa aplicada para Embarcaciones: **${TARIFA_EMBARCACION_KM} por km**")

# --- RESULTADO DEL COTIZADOR ---
st.markdown("---")
c1, c2 = st.columns(2)
c1.metric("VALOR ESTIMADO", f"${total:,.2f} UYU")
c2.metric("SERVICIO", tipo_servicio)

st.success("✅ Cálculo basado en los parámetros de logística regional vigentes.")

# --- TU FIRMA PROFESIONAL ---
st.markdown("---")
st.caption("Desarrollado por: Leonardo Olivera | Estudiante de Agronomía & Desarrollador IA")
