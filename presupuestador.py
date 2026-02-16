import streamlit as st
import pandas as pd
import re
import math

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- TARIFAS Y COSTOS FIJOS ---
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0    
COSTO_TRAILER_PESADO = 200.0  # Alquiler de tráiler para embarcaciones grandes

# --- DISEÑO RESPONSIVO (LOGO ADAPTABLE) ---
st.markdown(
    """
    <style>
    .header-container { text-align: center; font-family: sans-serif; padding-bottom: 10px; }
    .anchor-top { font-size: 50px; margin-bottom: -15px; }
    .logo-row { display: flex; align-items: center; justify-content: center; gap: 10px; flex-wrap: nowrap; }
    .icon-side { font-size: clamp(30px, 6vw, 50px); }
    .title-text { 
        color: #01579b; font-weight: 800; margin: 0;
        font-size: clamp(16px, 4.5vw, 38px); 
        white-space: nowrap; text-transform: uppercase;
    }
    </style>
    <div class="header-container">
        <div class="anchor-top">⚓</div>
        <div class="logo-row">
            <span class="icon-side">🚤</span>
            <h1 class="title-text">CONEXIÓN LOGÍSTICA SUR</h1>
            <span class="icon-side">🚛</span>
        </div>
        <p style="color: gray; font-size: 16px;">Transporte Nacional e Internacional</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

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
    # 1. Rubro
    rubro = st.radio("### 🛠️ ¿Qué desea cotizar?", ["📦 Mudanzas/Mercadería", "🚤 Embarcaciones"], horizontal=True)

    # 2. Origen y Destino
    c1, c2 = st.columns(2)
    with c1:
        d_o = st.selectbox("Dpto. Origen:", sorted(df['departamento'].unique()))
        l_o = st.selectbox("Ciudad Origen:", sorted(df[df['departamento']==d_o]['localidad'].unique()))
    with c2:
        d_d = st.selectbox("Dpto. Destino:", sorted(df['departamento'].unique()))
        l_d = st.selectbox("Ciudad Destino:", sorted(df[df['departamento']==d_d]['localidad'].unique()))

    # 3. Detalles específicos
    extra_barco = 0
    if "🚤" in rubro:
        tipo_b = st.selectbox("Tipo de Embarcación:", ["Lancha chica", "Crucero mediano", "Embarcación Grande (Pesada)"])
        if "Grande" in tipo_b:
            extra_barco = COSTO_TRAILER_PESADO
            st.warning(f"Se incluye costo de alquiler de tráiler: ${COSTO_TRAILER_PESADO}")

    # 4. Cálculo de Distancia (Ida y Vuelta)
    p1 = df[(df['departamento']==d_o) & (df['localidad']==l_o)].iloc[0]
    p2 = df[(df['departamento']==d_d) & (df['localidad']==l_d)].iloc[0]
    
    # Distancia lineal con ajuste del 20% por curvas
    dist_solo_ida = (math.sqrt((p2['cx']-p1['cx'])**2 + (p2['cy']-p1['cy'])**2)/1000) * 1.2
    dist_total = dist_solo_ida * 2  # IDA Y VUELTA

    # 5. Cálculo Final
    tarifa = TARIFA_MUDANZA_KM if "📦" in rubro else TARIFA_BARCO_KM
    subtotal_viaje = dist_total * tarifa
    precio_final = subtotal_viaje + extra_barco

    st.info(f"📏 Distancia Total (Ida y Vuelta): **{round(dist_total, 1)} km**")
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>Presupuesto Estimado:</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: #1B5E20; font-size: 50px;'>$ {precio_final:,.2f} UYU</h1>", unsafe_allow_html=True)
    st.caption(f"Cálculo: ({round(dist_total,1)} km x ${tarifa}) + ${extra_barco} (extras)")

else:
    st.error("Sube el archivo CSV a GitHub para habilitar el cotizador.")

# Pie de página
st.sidebar.markdown(f"**Desarrollador:** Leonardo Olivera")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")
