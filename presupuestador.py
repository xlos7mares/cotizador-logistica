import streamlit as st
import os
from PIL import Image

# 1. CONFIGURACIÓN DE PÁGINA Y ESTÉTICA DARK PROFESIONAL
st.set_page_config(page_title="Conexión Logística Sur", page_icon="🚚", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #121417; }
    [data-testid="stVerticalBlock"] > div {
        background-color: #1e2126;
        padding: 15px;
        border-radius: 15px;
    }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'Inter', sans-serif; }
    .stSelectbox div, .stNumberInput input {
        background-color: #2c3036 !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid #3e444c !important;
    }
    .stButton>button {
        background-color: #2ec4b6 !important;
        color: #121417 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        height: 55px !important;
        width: 100% !important;
        border: none !important;
    }
    .result-box {
        background-color: #2c3036;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #2ec4b6;
        margin-top: 20px;
    }
    .btn-whatsapp {
        background-color: #25d366;
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS DE URUGUAY
data_uruguay = {
    "Paysandú": ["Paysandú Ciudad", "Guichón", "Quebracho", "San Félix"],
    "Salto": ["Salto Ciudad", "Termas del Daymán", "Constitución"],
    "Montevideo": ["Montevideo Centro", "Puerto MVD", "Carrasco", "Paso de la Arena"],
    "Maldonado": ["Punta del Este", "Piriápolis", "Maldonado Ciudad", "San Carlos"],
    "Colonia": ["Colonia del Sacramento", "Carmelo", "Nueva Helvecia", "Rosario"],
    "Río Negro": ["Fray Bentos", "Young", "Nuevo Berlín"],
    "Artigas": ["Artigas Ciudad", "Bella Unión"],
    "Soriano": ["Mercedes", "Dolores", "Cardona"],
    "Canelones": ["Ciudad de la Costa", "Pando", "Las Piedras"]
}

# Distancias estimadas desde la base (Paysandú) para sugerir al cliente
distancias_base = {
    "Montevideo": 375, "Salto": 120, "Maldonado": 520, "Colonia": 350, 
    "Artigas": 210, "Río Negro": 100, "Soriano": 180, "Canelones": 360, "Paysandú": 20
}

# 3. LOGO
if os.path.exists("logo.png"):
    st.image(Image.open("logo.png"), width=280)
else:
    st.title("🚚 CONEXIÓN LOGÍSTICA SUR")

st.subheader("Cotizador Oficial Uruguay 2025")

# 4. ENTRADAS DE DATOS
col1, col2 = st.columns(2)
with col1:
    depto_origen = st.selectbox("Departamento Origen:", list(data_uruguay.keys()))
    ciudad_origen = st.selectbox("Pueblo/Ciudad Origen:", data_uruguay[depto_origen])

with col2:
    depto_destino = st.selectbox("Departamento Destino:", list(data_uruguay.keys()))
    ciudad_destino = st.selectbox("Pueblo/Ciudad Destino:", data_uruguay[depto_destino])

servicio = st.selectbox(
    "Tipo de Transporte:",
    ["Flete Estándar", "Mudanza Residencial", "Remolque de Embarcación", "Maquinaria de Peso Medio"]
)

# Sugerencia de distancia automática
dist_sugerida = distancias_base.get(depto_destino, 100)
distancia = st.number_input("Kilómetros totales del viaje:", min_value=1, value=dist_sugerida)

# 5. MOTOR DE COSTOS REALES (URUGUAY 2025)
# Basado en consumo Dodge Ram, mantenimiento y operativa
COSTOS_KM = {
    "Flete Estándar": 65,
    "Mudanza Residencial": 85,
    "Remolque de Embarcación": 110,
    "Maquinaria de Peso Medio": 125
}

BASES_SALIDA = {
    "Flete Estándar": 1800,
    "Mudanza Residencial": 4500,
    "Remolque de Embarcación": 6500,
    "Maquinaria de Peso Medio": 8000
}

PRECIO_PEAJE = 143 # Tarifa Telepeaje Cat 1 y 2 aproximada

# 6. CÁLCULO Y RESULTADO
st.markdown("<br>", unsafe_allow_html=True)
if st.button("GENERAR PRESUPUESTO FINAL"):
    base = BASES_SALIDA[servicio]
    precio_km = COSTOS_KM[servicio]
    
    # Lógica de peajes (1 cada 130km aprox en rutas uruguayas)
    num_peajes = (distancia // 130) + 1
    total_peajes = num_peajes * PRECIO_PEAJE
    
    total_final = base + (distancia * precio_km) + total_peajes
    
    st.markdown(f"""
        <div class="result-box">
            <p style="color: #aeb4be; margin-bottom: 5px;">TOTAL ESTIMADO (PESOS URUGUAYOS)</p>
            <h1 style="color: #ffffff; font-size: 45px; margin: 0;">${int(total_final)}</h1>
            <p style="color: #2ec4b6; font-weight: bold;">Ruta: {ciudad_origen} ➔ {ciudad_destino}</p>
            <hr style="border: 0.5px solid #3e444c;">
            <div style="text-align: left; font-size: 14px; color: #aeb4be;">
                • Base y Operativa: ${base}<br>
                • Recorrido ({distancia}km): ${int(distancia * precio_km)}<br>
                • Peajes estimados: ${int(total_peajes)}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # WhatsApp Directo
    msg = f"Hola! Solicito {servicio} desde {ciudad_origen} hasta {ciudad_destino} ({distancia}km). Presupuesto: ${int(total_final)}."
    st.markdown(f"""
        <a href="https://wa.me/59899417716?text={msg.replace(' ', '%20')}" target="_blank" class="btn-whatsapp">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="20" style="margin-right:10px;">
            RESERVAR POR WHATSAPP
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("Desarrollado por Leonardo Olivera - Litoral Operaciones Inmobiliarias")
