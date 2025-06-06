## Gerador de Início de História com IA
Este aplicativo Streamlit permite criar o começo de uma história personalizada usando a inteligência artificial do Google Gemini. Com algumas escolhas simples, você pode gerar um ponto de partida único e inspirador para sua próxima aventura literária!

## 🚀 Funcionalidades
Nome do Protagonista: Defina o nome do seu personagem principal.
Gênero Literário: Escolha o estilo da sua história (Fantasia, Ficção Científica, Mistério, Aventura, Terror ou Romance).
Local Inicial: Selecione o cenário onde a narrativa começará.
Frase de Efeito/Desafio: Adicione uma frase impactante ou um desafio inicial para ser incorporado ao enredo.
Geração com IA: O modelo Gemini do Google vai criar um ou dois parágrafos de introdução com base nas suas escolhas.
🛠️ Tecnologias Utilizadas
Streamlit: Framework Python para construir aplicações web interativas com facilidade.
Google Gemini API: Interface de programação que oferece acesso aos modelos de IA do Google (como o gemini-2.0-flash) para geração de texto.
Python: Linguagem de programação que orquestra todo o aplicativo.
⚙️ Como Usar
1. Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema.

Você também precisará de uma Chave de API do Google Gemini. Se não tiver uma, siga estes passos:

Acesse o Google AI Studio.
Faça login com sua conta Google.
Crie uma nova chave de API e copie-a.
2. Instalação
Primeiro, obtenha o código do aplicativo. Você pode clonar o repositório (se ele estiver em um) ou criar um arquivo .py (por exemplo, app_historia.py) e colar o código fornecido nele.

Bash

# Se você tiver o repositório:
# git clone <URL_DO_SEU_REPOSITORIO>
# cd <nome_do_seu_repositorio>

# Se você tem apenas o arquivo .py:
# Crie um arquivo chamado app_historia.py
# Cole o código Python do aplicativo nesse arquivo.
Em seguida, instale as bibliotecas necessárias:

Bash

pip install streamlit google-generativeai
3. Configuração da Chave de API
É altamente recomendável configurar sua chave de API como uma variável de ambiente para proteger suas credenciais.

No Linux/macOS (Terminal):

Bash

export GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
Para que a chave seja permanente, adicione essa linha ao seu arquivo .bashrc, .zshrc ou .profile.

No Windows (Prompt de Comando ou PowerShell):

DOS

set GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
Para torná-la permanente, adicione-a nas variáveis de ambiente do sistema (pesquise por "Editar variáveis de ambiente do sistema" no menu Iniciar).

Alternativa (Menos Segura): Você pode substituir "SUA_CHAVE_AQUI" diretamente no código Python, na linha genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")). Atenção: Expor sua chave no código não é uma prática segura para produção.

4. Executando o Aplicativo
Com a chave de API configurada e as dependências instaladas, execute o aplicativo no seu terminal:

Bash

streamlit run app_historia.py
Uma nova aba será aberta automaticamente no seu navegador, exibindo a interface do aplicativo.

📝 Exemplo de Uso
No campo "Nome do Protagonista:", digite, por exemplo, "Sir Kael".
Em "Gênero Literário:", escolha "Fantasia".
No "Local Inicial da História:", selecione "Um castelo assombrado".
Se quiser, adicione uma frase em "Frase de Efeito ou Desafio Inicial:", como "O silêncio era a canção mais assustadora.".
Clique em "Gerar Início da História" e observe a IA criar a introdução da sua narrativa!
