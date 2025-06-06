import streamlit as st
import google.generativeai as genai
import os # Importar os para usar variáveis de ambiente

# AVISO: É ALTAMENTE RECOMENDADO USAR VARIÁVEIS DE AMBIENTE PARA A CHAVE DE API.
# hardcodear a chave de API diretamente no código não é seguro em produção.
# Se você realmente precisa, pode usar a chave diretamente como feito, mas esteja ciente dos riscos.
# genai.configure(api_key="AIzaSyAJF-eK20AS9m5FQDsDNZ7vM10QeSz9zho")
# Idealmente, faríamos assim:
try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSyAJF-eK20AS9m5FQDsDNZ7vM10QeSz9zho"))
    # Substitua "SUA_CHAVE_AQUI" pela sua chave real se não estiver usando variável de ambiente.
    # Se você está obtendo a chave de um ambiente, use apenas os.environ["GEMINI_API_KEY"]
except Exception as e:
    st.error(f"Erro na configuração da API: {e}. Verifique se sua chave de API está correta.")
    st.stop()


# Certifique-se de que o modelo "gemini-2.0-flash" está disponível e suporta generateContent
# Você pode ter que ajustar o nome do modelo se o erro 404 persistir
# Para listar modelos disponíveis:
# for m in genai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)

model = genai.GenerativeModel("gemini-2.0-flash")

# Configurações da página Streamlit
st.set_page_config(page_title="Gerador de Início de História", layout="centered")

st.title("Gerador de Início de História com IA")
st.markdown("Crie o ponto de partida para sua próxima grande aventura!")

# 1. Pedir o Nome do Protagonista
nome_protagonista = st.text_input("Nome do Protagonista:", placeholder="Ex: Elara, Kael, Professor Enigma")

# 2. Permitir que o usuário escolha um Gênero Literário
genero_literario = st.selectbox(
    "Gênero Literário:",
    options=["Fantasia", "Ficção Científica", "Mistério", "Aventura", "Terror", "Romance"]
)

# 3. Permitir que o usuário selecione um Local Inicial
local_inicial = st.radio(
    "Local Inicial da História:",
    options=["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado",
             "Uma nave espacial à deriva", "Um laboratório secreto", "Um vilarejo pacato"]
)

# 4. Permitir que o usuário adicione uma Frase de Efeito ou Desafio Inicial
frase_desafio = st.text_area(
    "Frase de Efeito ou Desafio Inicial (opcional, será incorporada à história):",
    placeholder="Ex: 'E de repente, tudo ficou escuro.' ou 'O mapa indicava um perigo iminente.'"
)

# 5. Ter um botão "Gerar Início da História"
if st.button("Gerar Início da História"):
    if not nome_protagonista:
        st.warning("Por favor, forneça um nome para o protagonista.")
    else:
        # Lógica do Aluno (Prompt Engineering):
        # Criação do prompt para a IA Gemini usando todas as variáveis
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
                # Gerar a história usando o modelo configurado
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a história: {e}")
                st.info("Verifique se sua chave de API está configurada corretamente, se o modelo 'gemini-2.0-flash' está disponível e se você tem acesso à API Gemini.")

