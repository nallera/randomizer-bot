import logging
from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/random-list/ar', methods=['GET', 'POST'])
def randomlist():
    l = ['Clau', 'Tonny', 'Facu', 'Nico', 'Emi', 'Flavio']
    random.shuffle(l)
    msg = ""
    counter = 1
    for member in l:
        msg += str(counter) + ". " + member + "\n"
        counter += 1

    msg += "\n\n"
    msg += "Link al jira: https://mercadolibre.atlassian.net/jira/software/c/projects/PRI/boards/5839"

    response = {
        "response_type": "in_channel",
        "text": msg
    }
    return jsonify(response)

@app.route('/random-list/br', methods=['GET', 'POST'])
def randomlist():
    l = ['Adolpho', 'Philippe', 'Natan', 'Gabriel', 'Pedro', 'Valdeir', 'Gabriel']
    random.shuffle(l)
    msg = ""
    counter = 1
    for member in l:
        msg += str(counter) + ". " + member + "\n"
        counter += 1

    msg += "\n\n"
    msg += "Link al jira: https://mercadolibre.atlassian.net/jira/software/c/projects/PRI/boards/5839"

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
