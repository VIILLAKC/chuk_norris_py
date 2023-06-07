'''
//api.chucknorris.io/jokes/random
Se debe desarrollar un API RESTful que contenga un único endpoint el cual retorne un array con un rango definido de 25 objetos, diferentes unos de otros
Los objetos por el el siguiente endpoint:
Endpointhttps://api.chucknorris.io/jokes/random
'''
from flask import Flask, jsonify
import requests

app = Flask(__name__)

api_chuck = 'https://api.chucknorris.io/jokes/random'


def validate_chuck_data(value,data):
    if value in data:
        return 'Se repitio el id'
    else:
        return value
        

@app.route('/chucknorris')
def chucknorris():
    data = []
    for _ in range(25):
        request = requests.get(api_chuck)
        if request.status_code == 200:
            data.append(validate_chuck_data(request.json().get('id'), data))
        else:
            data.append('error')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=4000)