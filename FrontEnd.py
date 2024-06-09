import streamlit as st
import requests

st.set_page_config(
    page_title="ReceitAI", 
    page_icon="Logo.png", 
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("🍴ReceitAI")
st.divider()
st.write("Quais ingredientes você tem em casa?")
st.sidebar.title("ReceitAI")
st.sidebar.write("Esse é um projeto de demonstração de uma aplicação de IA para sugerir receitas com base nos ingredientes que você tem em casa.")

ingredients = st.text_input("Insira os ingredientes separados por vírgula", "")
restricao = st.selectbox("Possui alguma restrição alimentar?", ["Nenhuma", "Vegetariano", "Vegano", "Sem Glúten", "Sem Lactose"])
refeicao = st.selectbox("Qual refeição você deseja?", ["Café da manhã", "Almoço", "Jantar", "Sobremesa", "Lanche", "Qualquer"])

if st.button("Enviar"):
    if ingredients:
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
        response = requests.post('http://localhost:5000/api/submit', json={"ingredients": ingredients_list, "restricao": restricao, "refeicao" : refeicao}, )
        
        st.divider()
        if response.status_code == 200:
            data = response.json()
            st.write("Receita Sugerida:")
            st.markdown(data['instructions'])
            st.write("🍴Bom apetite!")
            st.download_button(
                label="Baixar Receita",
                data=data['instructions'],
                file_name="receita.txt",
                mime="text/plain",
            )
        else:
            st.error("Erro ao obter a receita. Tente novamente.")
    else:
        st.warning("Por favor, insira pelo menos um ingrediente.")