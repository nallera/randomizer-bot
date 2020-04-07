import logging
from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/random-list', methods=['GET', 'POST'])
def randomlist():
    l = ['Clau', 'Juan', 'Tonny', 'Dani', 'Tincho', 'Dari', 'Lucho']
    random.shuffle(l)
    msg = ""
    counter = 1
    for member in l:
        msg += str(counter) + ". " + member + "\n"
        counter += 1

    msg += "\n"
    msg += "Reminder: Llenar el doc :point_down: \nhttps://docs.google.com/document/d/1pJJ3SE4bHeKOFzWgBdDPiCgD_Mt7H9QrRYErx4oynnQ/edit \n\n"
    msg += "Que tengan buen día Release Team :party_parrot: #LoMejorEstaLlegando"

    response = {
        "response_type": "in_channel",
        "text": msg
    }
    return jsonify(response)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)
