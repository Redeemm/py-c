from flask import Flask, request, jsonify, render_template

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/chat")
def chat():
    text = request.get_json.get("message")
    response = get_response(text)
    mesaage = {"answer": response}
    return jsonify(mesaage)

if __name__ == "__name__":
    app.run(debug=True)
