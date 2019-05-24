import numpy as np
from utils import *
import pandas as pd
from sklearn.datasets import *
import matplotlib.pyplot as plt

from absl import flags
from absl import logging
from absl import app

FLAGS = flags.FLAGS
flags.DEFINE_integer('nodes', 1000, 'Numero de nodos a tener en cuenta:')


def main(argv):
    path = '../dataset/com-youtube.ungraph.txt'
    data = pd.read_csv(path, sep='\t', skiprows=3)
    print("Hay", data.to_numpy().shape[0],
          "conexiones en el dataset de youtube")
    data.head()
    np_data = data.to_numpy()
    most_important(np_data[:FLAGS.nodes], 'CGC')


app.run(main)
