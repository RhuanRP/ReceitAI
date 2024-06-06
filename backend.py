from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app, origins=["*"])

gemini_api_key = ""

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
)

chat_session = model.start_chat(history=[])

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    ingredients = data.get('ingredients')
    ingredients_list = ', '.join(ingredients)
    restricao = data.get('restricao')
    refeicao = data.get('refeicao')
    phrase = f"Gemini, qual receita posso fazer com somente esses ingredientes que tenho em casa: {ingredients_list}, e qual o modo de preparo ? Desejo que esse receita seja adquada para o(a): {refeicao}. Tenho essa restrição: {restricao}. Me traga também uma análise nutricional da receita."
    response_from_gemini = chat_session.send_message(phrase)
    
    response_text = ""
    if response_from_gemini and response_from_gemini._result and response_from_gemini._result.candidates:
        content = response_from_gemini._result.candidates[0].content
        if content and content.parts:
            response_text = content.parts[0].text

    return jsonify({"message": "Dados recebidos com sucesso!", "instructions": response_text})

if __name__ == '__main__':
    app.run(debug=True)