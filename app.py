from flask import Flask, request, jsonify
from primos import es_primo

app = Flask(__name__)

@app.route('/es_primo')
def verificar_primo():
    numero = request.args.get('num', type=int, default=0)
    
    respuesta = {
        "numero": numero,
        "es_primo": es_primo(numero)
    }

    return jsonify(respuesta)  # 🔹 Esto garantiza que se devuelva JSON correctamente

if __name__ == '__main__':
    app.run(debug=True)
