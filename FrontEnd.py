import streamlit as st
import requests

st.set_page_config(
    page_title="ReceitAI", 
    page_icon="Logo.png", 
    layout="wide",
    initial_sidebar_state="expanded",
)

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header("🍴ReceitAI")
st.divider()
st.write("Quais ingredientes você tem em casa?")
st.sidebar.title("ReceitAI")
st.sidebar.write("Esse é um projeto de demonstração de uma aplicação de IA para sugerir receitas com base nos ingredientes que você tem em casa.")

ingredients = st.text_input("Insira os ingredientes separados por vírgula", "")
restricao = st.selectbox("Possui alguma restrição alimentar?", ["Nenhuma", "Vegetariano", "Vegano", "Sem Glúten", "Sem Lactose"])
refeicao = st.selectbox("Qual refeição você deseja?", ["Café da manhã", "Almoço", "Jantar", "Sobremesa", "Lanche", "Qualquer"])
tempo_preparo = st.slider("Tempo máximo de preparo (minutos)", 1, 120, 30)

if st.button("Enviar"):
    if ingredients:
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
        response = requests.post('http://localhost:5000/api/submit', json={
            "ingredients": ingredients_list, 
            "restricao": restricao, 
            "refeicao": refeicao,
            "tempo_preparo": tempo_preparo
        })
        
        st.divider()
        if response.status_code == 200:
            data = response.json()
            st.write("Receita Sugerida:")
            st.markdown(data['instructions'])
            st.write("🍴Bom apetite!")

            if data.get('video_url'):
                st.write("Veja o modo de preparo no vídeo abaixo:")
                video_url = data['video_url']
                video_html = f"""
                <div class="video-container">
                    <iframe src="{video_url}" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
                """
                st.markdown(video_html, unsafe_allow_html=True)

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
