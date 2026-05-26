from flask import Flask, jsonify

app = Flask(__name__)

# rota principal
@app.route('/')
def home():
    return 'Servidor funcionando!'

# exemplo de API
@app.route('/usuarios')
def usuarios():
    return jsonify([
        {"id": 1, "nome": "Henrique"},
        {"id": 2, "nome": "João"}
    ])

# inicia o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)