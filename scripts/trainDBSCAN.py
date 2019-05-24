import pickle
import numpy as np
from utils import *
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

path = '../dataset/com-youtube.ungraph.txt'
data = pd.read_csv(path, sep='\t', skiprows=3)
print("Hay", data.to_numpy().shape[0],
      "conexiones en el dataset de youtube")
np_data = data.to_numpy()

dbscan_data = StandardScaler().fit_transform(
    np_data)  # mean zero and variance one

DBS = DBSCAN(eps=0.001)
train_model(DBS, dbscan_data)

stats = DBS.labels_

with open('stats.pickle', 'wb') as f:
    pickle.dump(stats, f, pickle.HIGHEST_PROTOCOL)
