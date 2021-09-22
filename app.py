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
    l = ['Clau', 'Tonny', 'Lucho', 'Facu', 'Luis', 'Nico', 'Emi']
    random.shuffle(l)
    msg = ""
    counter = 1
    for member in l:
        msg += str(counter) + ". " + member + "\n"
        counter += 1

    msg += "\n\n"
    msg += "Link al jira: https://mercadolibre.atlassian.net/secure/RapidBoard.jspa?rapidView=915&projectKey=AMP"

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
