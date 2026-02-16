import streamlit as st
import pandas as pd
import re
import math

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- TARIFAS ACTUALIZADAS SEGÚN GUSTAVO ---
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0   

# --- LOGO RESPONSIVO (SE ADAPTA A CELULAR Y PC) ---
st.markdown(
    """
    <style>
    .main-title-container {
        text-align: center;
        padding: 10px;
    }
    .anchor-icon {
        font-size: 50px;
        margin-bottom: -10px;
    }
    .flex-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        flex-wrap: nowrap; /* Evita que se parta en dos líneas */
    }
    .side-icon {
        font-size: 40px;
    }
    .main-text {
        color: #01579b;
        font-family: 'sans-serif';
        font-weight: bold;
        /* El truco mágico: vw significa 'viewport width'. Se adapta al ancho de la pantalla */
        font-size: clamp(18px, 5vw, 40px); 
        margin: 0;
        white-space: nowrap; /* Fuerza a que se mantenga en una sola línea */
    }
    @media (max-width: 480px) {
        .anchor-icon { font-size: 40px; }
        .side-icon { font-size: 30px; }
    }
    </style>
    
    <div class="main-title-container">
        <div class="anchor-icon">⚓</div>
        <div class="flex-container">
            <span class="side-icon">🚤</span>
            <h1 class="main-text">CONEXIÓN LOGÍSTICA SUR</h1>
            <span class="side-icon">🚛</span>
        </div>
        <p style="color: gray; font-size: clamp(14px, 2vw, 18px); margin-top: 5px;">
            Transporte Nacional e Internacional
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --- CARGA DE DATOS (Mismo código anterior) ---
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv('localidades-29-7nm (1).csv')
        def get_centroid(wkt):
            coords = re.findall(r"[-+]?\d*\.\d+|\d+", wkt)
            coords = [float(c) for c in coords]
            xs, ys = coords[0::2], coords[1::2]
            return (sum(xs)/len(xs), sum(ys)/len(ys)) if xs else (0,0)
        df['centroid_x'], df['centroid_y'] = zip(*df['wkt'].apply(get_centroid))
        return df
    except:
        return None

df_localidades = cargar_datos()

if df_localidades is not None:
    # --- SELECCIÓN DE RUBRO ---
    rubro = st.radio("### 🛠️ ¿Qué tipo de traslado necesita?", 
                     ["📦 Mudanzas, Mercaderías u Objetos", "🚤 Embarcaciones"], 
                     horizontal=True)

    # --- SELECTORES ORIGEN/DESTINO ---
    col1, col2 = st.columns(2)
    with col1:
        depto_origen = st.selectbox("Dpto. Origen:", sorted(df_localidades['departamento'].unique()))
        loc_origen = st.selectbox("Ciudad Origen:", sorted(df_localidades[df_localidades['departamento'] == depto_origen]['localidad'].unique()))
    with col2:
        depto_destino = st.selectbox("Dpto. Destino:", sorted(df_localidades['departamento'].unique()))
        loc_destino = st.selectbox("Ciudad Destino:", sorted(df_localidades[df_localidades['departamento'] == depto_destino]['localidad'].unique()))

    # --- CÁLCULO ---
    p_a = df_localidades[(df_localidades['departamento'] == depto_origen) & (df_localidades['localidad'] == loc_origen)].iloc[0]
    p_b = df_localidades[(df_localidades['departamento'] == depto_destino) & (df_localidades['localidad'] == loc_destino)].iloc[0]
    dist_km = (math.sqrt((p_b['centroid_x'] - p_a['centroid_x'])**2 + (p_b['centroid_y'] - p_a['centroid_y'])**2) / 1000) * 1.2
    
    precio = dist_km * (TARIFA_MUDANZA_KM if "📦" in rubro else TARIFA_BARCO_KM)

    st.info(f"📏 Distancia: **{round(dist_km, 1)} km**")
    st.markdown(f"<h1 style='text-align: center; color: #1B5E20;'>$ {precio:,.2f} UYU</h1>", unsafe_allow_html=True)
else:
    st.error("Por favor sube el archivo CSV a GitHub.")

# --- BOTÓN WHATSAPP ---
if st.button("📲 SOLICITAR COTIZACIÓN"):
    st.balloons()
