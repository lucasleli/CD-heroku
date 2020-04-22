import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá a todos os cuzões que reclamam diariamente na porra do FORUM. VAMOS DAR 140 NÃO SEI OQUE PARA VOCES. "

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
