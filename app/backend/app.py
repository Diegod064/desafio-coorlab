import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('../data.json', 'r') as file:
    travel_data = json.load(file)

@app.route('/fetch-cities')
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
@app.route('/travels', methods=['GET'])
def get_travels():
    
    destination = request.args.get('destino')
    date = request.args.get('data')

    passages_destination = [transport for transport in travel_data['transport'] if transport['city'] == destination]

    cheapest_economy = min(passages_destination, key=lambda x: float(x['price_econ'].replace('R$ ', '')))
    cheapest_comfort = min(passages_destination, key=lambda x: float(x['price_confort'].replace('R$ ', '')))

    if float(cheapest_economy['price_econ'].replace('R$ ', '')) <= float(cheapest_comfort['price_confort'].replace('R$ ', '')):
        cheapest_passage = cheapest_economy
        cheapest_passage_type = 'Economica'
        seat = f"Poltrona {cheapest_economy['seat']}"
        cheapest_price = cheapest_economy['price_econ']
    else:
        cheapest_passage = cheapest_comfort
        cheapest_passage_type = 'Confort'
        seat = cheapest_comfort['bed']
        cheapest_price = cheapest_comfort['price_confort']

    fastest_passage = min(passages_destination, key=lambda x: int(x['duration'].replace('h', '')))

    if cheapest_passage == fastest_passage and cheapest_passage_type == 'Confort':
        return jsonify({
            "cheapest_passage": {
                "name": cheapest_passage["name"],
                "price": cheapest_price,
                "duration": cheapest_passage["duration"],
                "seatType": cheapest_passage_type,
                "seat": seat,
                "isFast": True,
                "isCheapest": True
            }
        })

    cheapest_passage_data = {
        "name": cheapest_passage["name"],
        "price": cheapest_price,
        "duration": cheapest_passage["duration"],
        "seatType": cheapest_passage_type,
        "seat": seat,
        "isFastest": False,
        "isCheapest": True
    }

    fastest_passage_data = {
        "name": fastest_passage["name"],
        "price": fastest_passage['price_confort'],
        "duration": fastest_passage["duration"],
        "seatType": "Confort",
        "seat": fastest_passage['bed'],
        "isFastest": True,
        "isCheapest": False
    }

    return jsonify({
        "cheapest_passage": cheapest_passage_data,
        "fastest_passage": fastest_passage_data,
    })


if __name__ == '__main__':
    app.run(debug=True, port=3000)