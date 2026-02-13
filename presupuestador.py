import streamlit as st

# --- TARIFAS OFICIALES (AUDIO GUSTAVO) ---
PRECIO_MUDANZA_MERCADERIA_KM = 55.0  # El nuevo precio solicitado
PRECIO_EMBARCACIONES_KM = 80.0       # El precio base de barcos

st.set_page_config(page_title="CLS - Cotizador", page_icon="🚛")

# --- FIRMA PROFESIONAL ---
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("**Leonardo Olivera**")
st.sidebar.caption("Software & IA | Estudiante de Agronomía")

st.markdown("<h1 style='text-align: center;'>🚛 CONEXIÓN LOGÍSTICA SUR</h1>", unsafe_allow_html=True)

# --- CAMBIO A OPCIONES TIPO CÍRCULO (RADIO BUTTONS) ---
st.markdown("### Seleccione el rubro del traslado:")
rubro = st.radio(
    "Elija una opción:",
    ["📦 Mudanzas / Mercaderías / Objetos", "🚤 Embarcaciones (Lanchas/Cruceros)"],
    help="Marque el círculo correspondiente para ver las tarifas específicas."
)

st.markdown("---")

# --- LÓGICA POR RUBRO ---
if rubro == "📦 Mudanzas / Mercaderías / Objetos":
    st.subheader("Opciones de Carga General")
    # Aquí anexamos lo que pidió Gustavo
    tipo_carga = st.selectbox(
        "Detalle de lo que traslada:",
        ["Mudanza Particular", "Mercadería Comercial", "Objetos de Valor", "Muebles sueltos"]
    )
    distancia = st.number_input("Kilómetros de viaje (km):", min_value=1.0, value=1.0)
    
    # COSTO EXACTO: 55 por kilómetro
    total = distancia * PRECIO_MUDANZA_MERCADERIA_KM
    
    st.success(f"Tarifa Especial Gustavo: **${PRECIO_MUDANZA_MERCADERIA_KM} por km**")

else:
    st.subheader("Opciones de Náutica")
    # Aquí se mantienen tus opciones originales de lanchas
    tipo_lancha = st.selectbox(
        "Categoría de la embarcación:",
        ["Lancha chica", "Crucero mediano", "Embarcación Grande (Hasta 40 pies / 10 Ton)"]
    )
    distancia = st.number_input("Kilómetros de viaje (km):", min_value=1.0, value=1.0)
    
    # COSTO EMBARCACIONES: 80 por kilómetro
    total = distancia * PRECIO_EMBARCACIONES_KM
    
    st.info(f"Tarifa Náutica: **${PRECIO_EMBARCACIONES_KM} por km**")

# --- MOSTRAR RESULTADO ---
st.markdown("---")
st.markdown(f"### COSTO FINAL ESTIMADO ({tipo_carga if 'tipo_carga' in locals() else tipo_lancha})")
st.markdown(f"<h1 style='color: #1E88E5;'>$ {total:,.2f} UYU</h1>", unsafe_allow_html=True)

# Campo de imagen (Obligatorio)
st.subheader("📷 Foto del objeto/embarcación")
st.file_uploader("Suba una imagen para validar dimensiones", type=['png', 'jpg', 'jpeg'])

if st.button("📲 ENVIAR COTIZACIÓN"):
    st.balloons()
