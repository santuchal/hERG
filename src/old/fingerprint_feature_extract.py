import pandas as pd
import numpy as np
import sys
from rdkit import Chem, DataStructs
import json
import csv
from rdkit.Chem import AllChem
from mordred import Calculator, descriptors
from new.PubChemFingerprints import *
from tqdm import tqdm 

df = pd.read_csv("data/train_validation_cardio_tox_data.csv")
total_activity = df.loc[:,'ACTIVITY']
total_smiles = df.loc[:,'smiles']



def CalculateECFP2Fingerprint(mol,radius=1): # copied from https://github.com/gadsbyfly/PyBioMed/blob/master/PyBioMed/PyMolecule/fingerprint.py 
	res=AllChem.GetMorganFingerprint(mol,radius)
	fp = tuple(AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits = 1024))
	return fp, res.GetNonzeroElements(), res

def calculate_different_fingerprint(smile):
	mol = Chem.MolFromSmiles(smile)
	ECFP2Fingerprint = CalculateECFP2Fingerprint(mol)
	PubChemFingerAll = calcPubChemFingerAll(mol)
	return np.asarray(list(ECFP2Fingerprint[0]) + list(PubChemFingerAll))
df = pd.DataFrame()
i = 0
total_finger_print = []
for smile in tqdm(total_smiles):
	total_finger_print.append(calculate_different_fingerprint(smile))
	i = i+1

with open('data/new_dataset/external_test_set_new_data_fingerprint_output.csv', 'w') as writeFile:
	writer = csv.writer(writeFile, delimiter=",")
	writer.writerows(total_finger_print)
writeFile.close()