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
    response = {
        "response_type": "in_channel",
        "text": str(l)
    }
    return jsonify(response)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)
