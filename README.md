# ReceitAI 🍴

ReceitAI é um projeto de demonstração de uma aplicação de IA para sugerir receitas com base nos ingredientes que você tem em casa. A aplicação utiliza Flask no backend para receber os dados e retornar sugestões de receitas, e Streamlit no frontend para a interface do usuário.

## Funcionalidades

- Insira os ingredientes que você tem em casa.
- Selecione restrições alimentares.
- Escolha o tipo de refeição.
- Receba uma receita personalizada e uma análise nutricional.
- Baixe a receita sugerida.

## Tecnologias Utilizadas

- Flask
- Flask-CORS
- Google Generative AI (gemini-1.5-flash-latest)
- Streamlit
- Requests

## Estrutura do Projeto

ReceitAI/
├── backend/
│   ├── app.py
├── frontend/
│   ├── app.py
├── README.md


## Como Executar o Projeto

### Backend

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/receitai.git
   cd receitai/backend
Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate  # Para Windows

2. **Instale as dependências:**

pip install flask flask-cors google-generativeai
Execute o servidor Flask:
Copiar código
python app.py

## Frontend
Em outra janela do terminal, navegue até o diretório frontend:

cd ../frontend
Crie e ative um ambiente virtual (se necessário):

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate  # Para Windows
Instale as dependências:

pip install streamlit requests
Execute o Streamlit:


streamlit run app.py
Acessando a Aplicação
Abra o navegador e vá para http://localhost:8501 para acessar a interface do usuário.
Insira os ingredientes que você tem em casa separados por vírgula.
Selecione qualquer restrição alimentar, se houver.
Escolha o tipo de refeição desejada.
Clique em "Enviar" para receber uma receita sugerida.
Baixe a receita, se desejar.


   
