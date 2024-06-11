from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
CORS(app, origins=["*"])

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
)

chat_session = model.start_chat(history=[])

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def search_youtube_videos(query):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': youtube_api_key
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    if response.status_code == 200:
        videos = response.json().get('items', [])
        if videos:
            video_id = videos[0]['id']['videoId']
            return f"https://www.youtube.com/embed/{video_id}"
    return None

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    ingredients = data.get('ingredients')
    ingredients_list = ', '.join(ingredients)
    restricao = data.get('restricao')
    refeicao = data.get('refeicao')
    tempo_preparo = data.get('tempo_preparo')
    phrase = f"Gemini, qual receita posso fazer com somente esses ingredientes que tenho em casa: {ingredients_list}, e qual o modo de preparo? Desejo que essa receita seja adequada para o(a): {refeicao}. Tenho essa restrição: {restricao}. O tempo de preparo deve ser de no máximo {tempo_preparo} minutos. Me traga também uma análise nutricional da receita."
    response_from_gemini = chat_session.send_message(phrase)
    
    response_text = ""
    if response_from_gemini and response_from_gemini._result and response_from_gemini._result.candidates:
        content = response_from_gemini._result.candidates[0].content
        if content and content.parts:
            response_text = content.parts[0].text
    
    recipe_title = response_text.split('\n')[0] 
    video_url = search_youtube_videos(recipe_title)
    
    return jsonify({
        "message": "Dados recebidos com sucesso!", 
        "instructions": response_text,
        "video_url": video_url
    })

if __name__ == '__main__':
    app.run(debug=True)
