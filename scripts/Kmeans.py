import numpy as np
from utils import *
import pandas as pd
from sklearn.cluster import KMeans

from absl import flags
from absl import logging
from absl import app

FLAGS = flags.FLAGS
flags.DEFINE_integer('nodes', 1000, 'Numero de nodos a tener en cuenta:')
flags.DEFINE_integer('n_clusters', 10, 'Numero de clusters:')


def main(argv):
    path = '../dataset/com-youtube.ungraph.txt'
    data = pd.read_csv(path, sep='\t', skiprows=3)
    print("Hay", data.to_numpy().shape[0],
          "conexiones en el dataset de youtube")
    np_data = data.to_numpy()

    kmeans_data = np_data[:FLAGS.nodes]
    kmeans = KMeans(n_clusters=FLAGS.n_clusters)
    train_model(kmeans, kmeans_data)

    n_labels = len(np.unique(kmeans.labels_))
    colors_kmeans = rand_cmap(n_labels, first_color_black=False, verbose=False)
    cdict = get_color_dict(colors_kmeans)
    print('...')
    plot_graph(kmeans.labels_, kmeans_data, cdict,
               'Kmeans', str(FLAGS.n_clusters))


app.run(main)
