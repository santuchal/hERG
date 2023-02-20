import sys
from flask import Flask, Response, request, jsonify, Blueprint
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from errors import errors

app = Flask(__name__)
app.register_blueprint(errors)

@app.route('/')
def default_route():
    return Response("OK", status=200)

@app.route('/predict')
def predict():
	smile = request.args.get('smile')
	return smile

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)