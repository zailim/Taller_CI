from flask import Flask, request, jsonify
from primos import es_primo

app = Flask(__name__)

# app.py
#raise RuntimeError("Rompiendo el deploy para probar la notificación")

@app.route("/")
def inicio():
    return "API de numeros primos - Taller de integracion continua"

@app.route("/es_primo", methods=["GET"])
def verificar():
    numero = request.args.get("n")

    if numero is None:
        return jsonify({"error": "falta el parámetro n"}), 400
    
    try:
        n = int(numero)
        resultado = es_primo(n)
        return jsonify({"numero": n, "es_primo": resultado})
    except ValueError:
        return jsonify({"error": "el parámetro n debe ser un número entero"}),
    
if __name__ == "__main__":
        import os
        puerto = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=puerto)