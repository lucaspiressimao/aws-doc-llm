from flask import Flask, render_template, request, jsonify
from utils.llm_helpers import generate_and_execute_aws_query

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    query = data.get("query", "")
    region = data.get("region", "ALL")

    # Inclua a região como parte do prompt para o Ollama
    if region == "ALL":
        region_text = "all AWS regions"
    else:
        region_text = f"the {region} AWS region"

    # Atualize o prompt para incluir a região
    full_query = f"{query} in {region_text}"
    result = generate_and_execute_aws_query(full_query)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
