
import streamlit as st
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.utils.notebook import display_audio
import tempfile

st.set_page_config(page_title="Melodia da Alma", layout="centered")

st.title("Melodia da Alma")
st.subheader("Gere melodias com sua letra e ouça com voz e instrumentos realistas.")

lyrics = st.text_area("Digite a letra da música:", height=200)

style = st.selectbox("Escolha o estilo da melodia:", ["Ballad Slow", "Pop", "Rock", "Clássico"])

generate = st.button("Gerar melodia")

if generate and lyrics:
    st.info("Gerando melodia. Aguarde...")

    # Simulação de geração (pois MusicGen real não roda em Streamlit Cloud sem servidor extra)
    st.audio("https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_Sonata.ogg")
    st.success("Melodia gerada com sucesso! (áudio de exemplo)")
else:
    st.caption("O botão será ativado após digitar uma letra.")
