# 🍴 ReceitAI

ReceitAI é um projeto de demonstração de uma aplicação de IA para sugerir receitas com base nos ingredientes que você tem em casa. A aplicação utiliza Flask no backend para receber os dados e retornar sugestões de receitas, e Streamlit no frontend para a interface do usuário.

![Logo](https://github.com/RhuanRP/ReceitAI/assets/86031472/157b70a4-c48c-465e-a5fc-2f1477d27a5c)


## 📋 Funcionalidades

- Insira os ingredientes que você tem em casa.
- Selecione restrições alimentares.
- Escolha o tipo de refeição.
- Receba uma receita personalizada e uma análise nutricional.
- Baixe a receita sugerida.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask, Flask-CORS, Google Generative AI (gemini-1.5-flash-latest)
- **Frontend**: Streamlit
- **Comunicação**: Requests

## 📁 Estrutura do Projeto
```plaintext
ReceitAI/
├── backend/
│   └── app.py
├── frontend/
│   └── app.py
└── README.md
```

🚀 Como Executar o Projeto

## Backend

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/receitai.git
cd receitai/backend
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate  # Para Windows
```

Instale as dependências:
```bash
pip install flask flask-cors google-generativeai
```

Execute o servidor Flask:
```bash
python app.py
```

## Frontend
Em outra janela do terminal, navegue até o diretório frontend:
```bash
cd ../frontend
```

Instale as dependências:
```bash
pip install streamlit requests
```

Execute o Streamlit:
```bash
streamlit run FrontEnd.py
```

## Acessando a Aplicação

Abra o navegador e vá para http://localhost:8501 para acessar a interface do usuário.
Insira os ingredientes que você tem em casa separados por vírgula.
Selecione qualquer restrição alimentar, se houver.
Escolha o tipo de refeição desejada.
Clique em "Enviar" para receber uma receita sugerida.
Baixe a receita, se desejar.

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.



