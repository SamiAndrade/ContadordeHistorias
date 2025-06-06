import streamlit as st
import google.generativeai as genai
import os 


try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI"))
    # Substitua "SUA_CHAVE_AQUI" pela sua chave real se não estiver usando variável de ambiente.
    # Se você está obtendo a chave de um ambiente, use apenas os.environ["GEMINI_API_KEY"]
except Exception as e:
    st.error(f"Erro na configuração da API: {e}. Verifique se sua chave de API está correta.")
    st.stop()


model = genai.GenerativeModel("gemini-2.0-flash")


st.set_page_config(page_title="Gerador de Início de História", layout="centered")

st.title("Gerador de Início de História com IA")
st.markdown("Crie o ponto de partida para sua próxima grande aventura!")


nome_protagonista = st.text_input("Nome do Protagonista:", placeholder="Ex: Elara, Kael, Professor Enigma")


genero_literario = st.selectbox(
    "Gênero Literário:",
    options=["Fantasia", "Ficção Científica", "Mistério", "Aventura", "Terror", "Romance"]
)


local_inicial = st.radio(
    "Local Inicial da História:",
    options=["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado",
             "Uma nave espacial à deriva", "Um laboratório secreto", "Um vilarejo pacato"]
)


frase_desafio = st.text_area(
    "Frase de Efeito ou Desafio Inicial (opcional, será incorporada à história):",
    placeholder="Ex: 'E de repente, tudo ficou escuro.' ou 'O mapa indicava um perigo iminente.'"
)


if st.button("Gerar Início da História"):
    if not nome_protagonista:
        st.warning("Por favor, forneça um nome para o protagonista.")
    else:
        
        prompt = (
            f"Crie o início de uma história de '{genero_literario}' com o protagonista chamado '{nome_protagonista}'. "
            f"A história começa em '{local_inicial}'. "
        )

        if frase_desafio:
            prompt += f"Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'. "
        else:
            prompt += "Apresente o protagonista e o cenário de forma cativante. "

        prompt += "Gere apenas um parágrafo ou dois de introdução, sem títulos ou formatação extra."

        st.subheader("Seu Início de História:")
        with st.spinner("Gerando sua história..."):
            try:
               
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a história: {e}")
                st.info("Verifique se sua chave de API está configurada corretamente, se o modelo 'gemini-2.0-flash' está disponível e se você tem acesso à API Gemini.")

