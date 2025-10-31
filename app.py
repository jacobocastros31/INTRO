import streamlit as st
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(
    page_title="Mi Primera App Multimodal | Jacobo Castro",
    page_icon="🧠",
    layout="centered"
)

# --- Encabezado principal ---
st.markdown("""
<h1 style='text-align: center; color: #4ECDC4;'>🚀 Mi Primera App Multimodal</h1>
<h3 style='text-align: center; color: #888;'>Desarrollada por <b>Jacobo Castro</b></h3>
<p style='text-align: center; color: #555; font-size:18px;'>
Explorando el mundo de las <b>interfaces multimodales</b> — combinando lo visual, auditivo y táctil para mejorar la interacción humano-computador.
</p>
<hr style='border: 1px solid #ccc;'>
""", unsafe_allow_html=True)

# --- Imagen principal ---
image = Image.open('intro.png')
st.image(image, caption='Interfaces multimodales', use_container_width=True)

# --- Texto de entrada ---
st.markdown("### ✍️ Escribe algo:")
texto = st.text_input('Introduce tu texto aquí:', 'Este es mi texto')
st.write('📘 El texto escrito es:', texto)

# --- Sección de columnas ---
st.markdown("## 🧩 Dos Modalidades, Dos Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Primera Columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario al combinar distintos sentidos.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('✅ ¡Correcto! Las interfaces multimodales crean experiencias más naturales.')

with col2:
    st.subheader("🔊 Segunda Columna")
    modo = st.radio("Selecciona la modalidad principal en tu interfaz:", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.info('👁️ La vista es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.info('🎧 La audición es fundamental para tu interfaz.')
    elif modo == 'Táctil':
        st.info('✋ El tacto es fundamental para tu interfaz.')

# --- Botón interactivo ---
st.markdown("## 🕹️ Interacción con botones")
if st.button('Presiona el botón'):
    st.success('🎉 ¡Gracias por presionar el botón!')
else:
    st.warning('⏳ Aún no has presionado el botón.')

# --- Selectbox ---
st.markdown("## 🎛️ Selecciona la modalidad de interacción")
in_mod = st.selectbox(
    "Selecciona una modalidad:",
    ("Audio", "Visual", "Háptico"),
)

if in_mod == "Audio":
    set_mod = "🔊 Reproducir audio"
elif in_mod == "Visual":
    set_mod = "🎬 Reproducir video"
elif in_mod == "Háptico":
    set_mod = "💫 Activar vibración"

st.success(f"La acción seleccionada es: {set_mod}")

# --- Barra lateral ---
with st.sidebar:
    st.header("⚙️ Configuración de Modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar:",
        ("Visual", "Auditiva", "Háptica")
    )
    st.caption("💡 Usa esta sección para configurar el tipo de interacción multimodal.")

# --- Pie de página ---
st.markdown("""
<hr style='border: 1px solid #ccc;'>
<p style='text-align: center; color: #999; font-size: 14px;'>
Desarrollado con ❤️ por <b>Jacobo Castro</b> — Proyecto de Interfaces Multimodales.
</p>
""", unsafe_allow_html=True)
