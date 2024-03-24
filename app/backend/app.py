import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carregar os dados das viagens a partir do arquivo JSON
with open('../data.json', 'r') as file:
    travel_data = json.load(file)

@app.route('/api/travels')
def get_travels():
    return jsonify(travel_data)

@app.route('/cities')
def fetch():
    with open('../data.json') as file:
        data = json.load(file)

    transports = data['transport']
    cities = set()

    for transport in transports:
        city = transport['city']
        if city not in cities:
            cities.add(city)

    return jsonify(sorted((list(cities))))

# @app.route('/passagens/<string:destination>/', methods=['GET'])
@app.route('/passagens', methods=['GET'])
def get_passagens():
    # # Obtenha os parâmetros da solicitação
    destino = request.args.get('destino')
    data = request.args.get('data')

    # # Lógica para encontrar a passagem mais econômica e a mais rápida
    # passagem_economica = min(passagens, key=lambda x: float(x['price_econ'].replace('R$ ', '')))
    # passagem_rapida = min(passagens, key=lambda x: int(x['duration'].replace('h', '')))

    return jsonify({
        # "passagem_economica": passagem_economica,
        # "passagem_rapida": passagem_rapida
        "paramDestino": destino,
        "paramData": data,
    })


if __name__ == '__main__':
    app.run(debug=True, port=3000)