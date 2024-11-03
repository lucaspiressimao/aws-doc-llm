from flask import Flask, render_template, request, jsonify
from utils.llm_helpers import generate_documentation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    query = data.get("query", "")
    
    # Chama a função para enviar a consulta para o Ollama
    result = generate_documentation(query, data={})  # Adapte 'data' se precisar enviar dados adicionais
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
