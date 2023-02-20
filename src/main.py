import sys
from flask import Flask, Response, request, jsonify, Blueprint
import os
from new.descriptor_check import *
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
	acc = smile_descriptor_test_with_model(smile)
	return str(acc)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)