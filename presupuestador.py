import streamlit as st
import pandas as pd
import re
import math

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- VALORES DINÁMICOS ---
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0    
COSTO_TRAILER_PESADO = 200.0
COTIZACION_DOLAR_BROU = 42.50 # Actualizable manualmente

# --- DISEÑO RESPONSIVO ---
st.markdown(
    """
    <style>
    .header-container { text-align: center; font-family: sans-serif; }
    .anchor-top { font-size: 50px; margin-bottom: -15px; }
    .logo-row { display: flex; align-items: center; justify-content: center; gap: 10px; flex-wrap: nowrap; }
    .title-text { 
        color: #01579b; font-weight: bold; 
        font-size: clamp(16px, 5vw, 35px); 
        white-space: nowrap; 
    }
    .price-box {
        background-color: #f1f8e9;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #2e7d32;
        margin-top: 20px;
    }
    </style>
    <div class="header-container">
        <div class="anchor-top">⚓</div>
        <div class="logo-row">
            <span style="font-size: 40px;">🚤</span>
            <h1 class="title-text">CONEXIÓN LOGÍSTICA SUR</h1>
            <span style="font-size: 40px;">🚛</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- CARGA DE DATOS ---
@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv('localidades-29-7nm (1).csv')
        def get_centroid(wkt):
            c = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", wkt)]
            return (sum(c[0::2])/len(c[0::2]), sum(c[1::2])/len(c[1::2])) if c else (0,0)
        df['cx'], df['cy'] = zip(*df['wkt'].apply(get_centroid))
        return df
    except: return None

df = cargar_datos()

if df is not None:
    rubro = st.radio("### 🛠️ ¿Qué desea cotizar?", ["📦 Mudanzas/Mercadería", "🚤 Embarcaciones"], horizontal=True)

    c1, c2 = st.columns(2)
    with c1:
        d_o = st.selectbox("Dpto. Origen:", sorted(df['departamento'].unique()))
        l_o = st.selectbox("Ciudad Origen:", sorted(df[df['departamento']==d_o]['localidad'].unique()))
    with c2:
        d_d = st.selectbox("Dpto. Destino:", sorted(df['departamento'].unique()))
        l_d = st.selectbox("Ciudad Destino:", sorted(df[df['departamento']==d_d]['localidad'].unique()))

    extra_pesada = 0
    detalle_carga = ""
    if "🚤" in rubro:
        tipo_b = st.selectbox("Tamaño de Embarcación:", ["Lancha chica", "Crucero mediano", "Embarcación Grande (Pesada)"])
        detalle_carga = tipo_b
        if "Pesada" in tipo_b:
            extra_pesada = COSTO_TRAILER_PESADO
            st.warning(f"⚠️ Se suma costo de carga pesada: ${COSTO_TRAILER_PESADO} UYU")
    else:
        detalle_carga = st.text_input("Detalle de la mercadería:", "Mudanza general")

    # Cálculo (Ida y Vuelta + 20% curvas)
    p1 = df[(df['departamento']==d_o) & (df['localidad']==l_o)].iloc[0]
    p2 = df[(df['departamento']==d_d) & (df['localidad']==l_d)].iloc[0]
    dist_total = (math.sqrt((p2['cx']-p1['cx'])**2 + (p2['cy']-p1['cy'])**2)/1000) * 1.2 * 2
    
    tarifa = TARIFA_MUDANZA_KM if "📦" in rubro else TARIFA_BARCO_KM
    precio_pesos = (dist_total * tarifa) + extra_pesada
    precio_dolares = precio_pesos / COTIZACION_DOLAR_BROU

    # --- RESULTADO FINAL ---
    st.markdown(f"""
        <div class="price-box">
            <h3 style="margin:0; color:#2e7d32;">PRESUPUESTO ESTIMADO</h3>
            <h1 style="margin:0; font-size: 42px; color:#1b5e20;">$ {precio_pesos:,.2f} UYU</h1>
            <p style="font-size: 20px; color:#555;">Equivale a: <b>U$S {precio_dolares:,.2f}</b></p>
            <small>Dólar BROU: ${COTIZACION_DOLAR_BROU} | Distancia Total: {round(dist_total,1)} km</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    # --- SUBIDA DE IMAGEN ---
    st.subheader("📷 Foto de lo que desea trasladar")
    foto = st.file_uploader("Suba una imagen para validar dimensiones (Obligatorio)", type=['png', 'jpg', 'jpeg'])

    # --- BOTÓN DE ENVÍO ---
    if st.button("📲 SOLICITAR COTIZACIÓN"):
        if foto is not None:
            st.balloons()
            st.success(f"¡Presupuesto generado! Por favor, envíe el detalle a: conexionlogisticasur@gmail.com")
            # Aquí podrías agregar un mailto link si lo deseas
        else:
            st.error("Por favor, sube una foto antes de solicitar la cotización.")

else:
    st.error("Error al cargar localidades.")

st.sidebar.markdown(f"**Desarrollador:** Leonardo Olivera")
