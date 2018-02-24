"""
Development usage:
(omit the FLASK_DEBUG line for deployment)

$ export FLASK_APP=server.py
$ export FLASK_DEBUG=1 
$ flask run

Note: on Windows use SET in place of EXPORT

"""

from power_model import PowerModel as Model

from flask import Flask
import json

mo = None

def initialize_app():
    app = Flask(__name__)
    # Initialization code
    mo = Model()
    return app

app = initialize_app()

@app.route('/score')
def score_data(input_json):
    validated_data = mo.validate(input_json)
    transformed_data = mo.transform(validated_data)
    predictions = mo.predict(transformed_data)
    outputs = mo.score(predictions)
    return json.dumps(outputs)

@app.route('/')
def service_information():
    return "This is a scoring service."
    