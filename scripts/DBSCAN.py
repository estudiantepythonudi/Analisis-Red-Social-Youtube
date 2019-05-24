import numpy as np
from utils import *
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from absl import flags
from absl import logging
from absl import app

FLAGS = flags.FLAGS
flags.DEFINE_integer('nodes', 1000, 'Numero de nodos a tener en cuenta:')
flags.DEFINE_float('epsilon', 0.001, 'Tolerancia entre nodos:')


def main(argv):
    if FLAGS.epsilon <= 0:
        print("Epsilon debe ser mayor a 0")
        return

    path = '../dataset/com-youtube.ungraph.txt'
    data = pd.read_csv(path, sep='\t', skiprows=3)
    print("Hay", data.to_numpy().shape[0],
          "conexiones en el dataset de youtube")
    np_data = data.to_numpy()

    dbscan_data = StandardScaler().fit_transform(
        np_data)  # mean zero and variance one
    dbscan_data = dbscan_data[:FLAGS.nodes]

    DBS = DBSCAN(eps=FLAGS.epsilon)
    train_model(DBS, dbscan_data)

    n_labels = len(np.unique(DBS.labels_))
    colors = rand_cmap(n_labels, first_color_black=False, verbose=False)
    cdict = get_color_dict(colors)
    print('...')
    plot_graph(DBS.labels_, dbscan_data, cdict, 'DBSCAN', str(FLAGS.epsilon))


app.run(main)
