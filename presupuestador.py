import streamlit as st
import pandas as pd
import re
import math

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- TARIFAS ACTUALIZADAS SEGÚN GUSTAVO ---
TARIFA_MUDANZA_KM = 55.0  #
TARIFA_BARCO_KM = 80.0    #

# --- ESTILO CSS PARA DISEÑO RESPONSIVO ---
st.markdown(
    """
    <style>
    .header-container {
        text-align: center;
        font-family: 'Arial', sans-serif;
        padding-bottom: 20px;
    }
    .anchor-top {
        font-size: 50px; /* Tamaño del ancla */
        margin-bottom: -15px;
    }
    .logo-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        flex-wrap: nowrap; /* Evita que los iconos bajen */
    }
    .icon-side {
        font-size: clamp(30px, 6vw, 55px); /* Se achica en móviles */
    }
    .title-text {
        color: #01579b;
        font-weight: 800;
        margin: 0;
        /* El tamaño de letra se ajusta solo: mínimo 18px, máximo 40px */
        font-size: clamp(18px, 4.5vw, 40px); 
        white-space: nowrap; /* Fuerza a que no se parta la palabra */
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    @media (max-width: 480px) {
        .logo-row { gap: 8px; }
    }
    </style>

    <div class="header-container">
        <div class="anchor-top">⚓</div>
        <div class="logo-row">
            <span class="icon-side">🚤</span>
            <h1 class="title-text">CONEXIÓN LOGÍSTICA SUR</h1>
            <span class="icon-side">🚛</span>
        </div>
        <p style="color: #555; font-size: 16px; margin-top: 5px;">
            Transporte Nacional e Internacional
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --- CARGA Y CÁLCULO (Asegúrate de tener el CSV en GitHub) ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('localidades-29-7nm (1).csv')
        def get_centroid(wkt):
            c = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", wkt)]
            return (sum(c[0::2])/len(c[0::2]), sum(c[1::2])/len(c[1::2])) if c else (0,0)
        df['cx'], df['cy'] = zip(*df['wkt'].apply(get_centroid))
        return df
    except: return None

df = load_data()

if df is not None:
    # Selector de rubro
    rubro = st.radio("### 🛠️ ¿Qué desea cotizar?", 
                     ["📦 Mudanzas/Mercadería", "🚤 Embarcaciones"], horizontal=True)
    
    # Origen y Destino
    c1, c2 = st.columns(2)
    with c1:
        d_o = st.selectbox("Dpto. Origen:", sorted(df['departamento'].unique()))
        l_o = st.selectbox("Ciudad Origen:", sorted(df[df['departamento']==d_o]['localidad'].unique()))
    with c2:
        d_d = st.selectbox("Dpto. Destino:", sorted(df['departamento'].unique()))
        l_d = st.selectbox("Ciudad Destino:", sorted(df[df['departamento']==d_d]['localidad'].unique()))

    # Cálculo de distancia y precio
    p1 = df[(df['departamento']==d_o) & (df['localidad']==l_o)].iloc[0]
    p2 = df[(df['departamento']==d_d) & (df['localidad']==l_d)].iloc[0]
    dist = (math.sqrt((p2['cx']-p1['cx'])**2 + (p2['cy']-p1['cy'])**2)/1000) * 1.2 # +20% curvas
    
    precio = dist * (TARIFA_MUDANZA_KM if "📦" in rubro else TARIFA_BARCO_KM)

    st.info(f"📏 Distancia estimada: **{round(dist, 1)} km**")
    st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {precio:,.2f} UYU</h1>", unsafe_allow_html=True)
else:
    st.error("Error: Sube el archivo 'localidades-29-7nm (1).csv' a tu repositorio de GitHub.")

# Pie de página con firma
st.sidebar.markdown(f"**Desarrollador:** Leonardo Olivera")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")
