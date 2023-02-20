import pandas as pd
import numpy as np
import sys
import numbers
from rdkit import Chem, DataStructs
from mordred import Calculator, descriptors
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def mordred_descriptors(smile):
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
	return df

def smile_descriptor_test_with_model(smile):
	new_model = tf.keras.models.load_model('../saved_model/desc_model_train/whole_model/cardio_tox_fingerprint_model')
	X_test_data = mordred_descriptors(smile)
	acc = new_model.predict(X_test_data, verbose=2)
	return acc

smile = "C1=NC2NC3=CNCC3=CC2CC1"
print(smile_descriptor_test_with_model(smile))

