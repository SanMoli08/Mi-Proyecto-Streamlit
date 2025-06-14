import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

st.sidebar.title("Configuración de la IA")
modelo = st.sidebar.selectbox("Elegí el modelo", ["llama3-8b-8192"])

st.title("Mi Primera Aplicación con Streamlit")

nombre = st.text_input("¿Cuál es tu nombre?")
if st.button("Saludar"):
    st.write(f"¡Hola {nombre}! Bienvenido/a 😊")

st.subheader("Mi chat de IA")
mensaje = st.text_input("Escribí tu mensaje:")

if mensaje:
    try:
        respuesta = client.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": mensaje}]
        )
        st.write("Respuesta del modelo:")
        st.write(respuesta.choices[0].message.content)
    except Exception as e:
        st.error(f"Error al obtener respuesta: {e}")










