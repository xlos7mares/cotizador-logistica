import streamlit as st
import pandas as pd
import re
import math

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CLS - Cotizador Oficial", page_icon="🚛", layout="centered")

# --- TARIFAS ACTUALIZADAS SEGÚN GUSTAVO ---
TARIFA_MUDANZA_KM = 55.0  
TARIFA_BARCO_KM = 80.0   

# --- FUNCIONES TÉCNICAS (PROCESAMIENTO DE DATOS) ---
@st.cache_data
def cargar_datos():
    # Cargamos el archivo que subiste
    df = pd.read_csv('localidades-29-7nm (1).csv')
    
    def get_centroid(wkt):
        # Extraemos coordenadas X e Y del formato MULTIPOLYGON
        coords = re.findall(r"[-+]?\d*\.\d+|\d+", wkt)
        coords = [float(c) for c in coords]
        xs = coords[0::2]
        ys = coords[1::2]
        if xs and ys:
            return sum(xs)/len(xs), sum(ys)/len(ys)
        return 0, 0

    # Calculamos el punto central de cada localidad para medir distancias
    df['centroid_x'], df['centroid_y'] = zip(*df['wkt'].apply(get_centroid))
    return df

try:
    df_localidades = cargar_datos()
except:
    st.error("Error: No se encontró el archivo 'localidades-29-7nm (1).csv'. Asegúrate de subirlo a GitHub.")
    st.stop()

# --- LOGO PERSONALIZADO (ANCLA ARRIBA, BARCO IZQ, CAMIÓN DER) ---
st.markdown(
    """
    <div style="text-align: center; line-height: 1;">
        <div style="font-size: 70px; margin-bottom: 10px;">⚓</div>
        <div style="display: flex; align-items: center; justify-content: center; gap: 20px;">
            <span style="font-size: 60px;">🚤</span>
            <h1 style="color: #01579b; font-family: sans-serif; font-size: 42px; margin: 0;">
                CONEXIÓN LOGÍSTICA SUR
            </h1>
            <span style="font-size: 60px;">🚛</span>
        </div>
        <p style="color: gray; font-size: 20px; margin-top: 15px;">
            Servicios de Transporte Nacional e Internacional
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --- 1. SELECCIÓN DE RUBRO ---
rubro = st.radio(
    "### 🛠️ ¿Qué tipo de traslado necesita?",
    ["📦 Mudanzas, Mercaderías u Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    index=0,
    horizontal=True
)

st.markdown("---")

# --- 2. SELECTOR DE ORIGEN Y DESTINO ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📍 Origen")
    depto_origen = st.selectbox("Departamento de salida:", sorted(df_localidades['departamento'].unique()))
    locs_origen = df_localidades[df_localidades['departamento'] == depto_origen]
    loc_origen = st.selectbox("Ciudad/Localidad de salida:", sorted(locs_origen['localidad'].unique()))

with col2:
    st.markdown("### 🏁 Destino")
    depto_destino = st.selectbox("Departamento de llegada:", sorted(df_localidades['departamento'].unique()))
    locs_destino = df_localidades[df_localidades['departamento'] == depto_destino]
    loc_destino = st.selectbox("Ciudad/Localidad de llegada:", sorted(locs_destino['localidad'].unique()))

# --- 3. CÁLCULO DE DISTANCIA ---
# Obtenemos las coordenadas de las localidades elegidas
punto_a = df_localidades[(df_localidades['departamento'] == depto_origen) & (df_localidades['localidad'] == loc_origen)].iloc[0]
punto_b = df_localidades[(df_localidades['departamento'] == depto_destino) & (df_localidades['localidad'] == loc_destino)].iloc[0]

# Cálculo de distancia euclidiana (UTM a Kilómetros)
distancia_m = math.sqrt((punto_b['centroid_x'] - punto_a['centroid_x'])**2 + (punto_b['centroid_y'] - punto_a['centroid_y'])**2)
distancia_km = round(distancia_m / 1000, 1)

# Ajuste por curvas en carretera (se suele sumar un 15-20% a la distancia lineal)
distancia_final = round(distancia_km * 1.2, 1)

st.info(f"📏 Distancia estimada de ruta: **{distancia_final} km**")

# --- 4. CÁLCULO DE COSTO ---
if "📦 Mudanzas" in rubro:
    total = distancia_final * TARIFA_MUDANZA_KM
    tarifa_actual = TARIFA_MUDANZA_KM
else:
    total = distancia_final * TARIFA_BARCO_KM
    tarifa_actual = TARIFA_BARCO_KM

# --- RESULTADO FINAL ---
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>Presupuesto Estimado:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #1B5E20; font-size: 55px;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)
st.caption(f"Calculado a una tarifa de ${tarifa_actual} por km.")

# Registro de foto
st.subheader("📷 Registro Fotográfico")
st.file_uploader("Suba una imagen para validar dimensiones", type=['png', 'jpg', 'jpeg'])

if st.button("📲 SOLICITAR COTIZACIÓN POR WHATSAPP"):
    st.balloons()
    st.success("Enviando ruta y presupuesto a Leonardo Olivera...")

# --- FIRMA ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")
