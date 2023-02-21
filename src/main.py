import os
import sys
import numbers
import numpy as np
import pandas as pd
import tensorflow as tf
from rdkit import Chem, DataStructs
from mordred import Calculator, descriptors
from flask import Flask, Response, request, jsonify, Blueprint

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
	all_values = []
	all_key = []
	mol = Chem.MolFromSmiles(smile)
	calc = Calculator(descriptors, ignore_3D = False)
	desc_mol=calc(mol)
	for key in desc_mol.keys():
		all_key.append(key)
	df = pd.DataFrame(columns=all_key)
	for value in desc_mol.values():
		if isinstance(value, int) or isinstance(value, float):
			all_values.append(value)
		else:
			all_values.append(0)
	df.loc[-1] = np.array(all_values)
	new_model = tf.keras.models.load_model('/app/saved_model/desc_model_train/whole_model/cardio_tox_fingerprint_model')
	X_test_data = df
	acc = new_model.predict(X_test_data, verbose=2)	
	return str(acc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)