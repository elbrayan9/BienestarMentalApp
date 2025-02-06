import streamlit as st
from transformers import pipeline

# Título de la app
st.title('🧘🏻‍♂️Clasificador de Sentimientos🧘🏻‍♂️: ¿Cómo te sientes hoy?')

# Crear un pipeline de Hugging Face para análisis de sentimiento
sentiment_analyzer = pipeline("sentiment-analysis")

# Solicitar al usuario que ingrese un texto
texto_usuario = st.text_area("Escribe lo que sientes🧠:")

# Botón para activar el análisis de sentimiento
if st.button("✨Analizar sentimiento✨"):
    if texto_usuario:
        # Analizar el sentimiento del texto ingresado
        resultado = sentiment_analyzer(texto_usuario)

        # Mostrar el resultado de la clasificación
        label = resultado[0]['label']
        score = resultado[0]['score']

        st.write(f"Sentimiento detectado: **{label}**")
        st.write(f"Confianza del modelo: {score:.2f}")

        # Respuestas basadas en el tipo de sentimiento
        if label == 'NEGATIVE':
            st.warning("Parece que estás pasando por un momento difícil. Aquí tienes algunas sugerencias:")
            st.write("1. Respira profundamente. 🧘‍♀️")
            st.write("2. Haz una actividad que te relaje, como escuchar música o dar un paseo. 🎶")
            st.write("3. Si necesitas ayuda, no dudes en hablar con un profesional de la salud mental. 📞")
        elif label == 'POSITIVE':
            st.success("¡Me alegra saber que te sientes bien! Sigue así.")
            st.write("Recuerda seguir cultivando tu bienestar y disfrutar de tus momentos felices. 🌟")
        else:
            st.info("Parece que estás neutral. Si hay algo en lo que te gustaría mejorar, ¡estoy aquí para ayudarte!")
            st.write("Recuerda que es importante cuidar tu salud emocional todos los días. 💙")
    else:
        st.error("Por favor, escribe algo para analizar.")
