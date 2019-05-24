import colorsys
import numpy as np
import igraph as ig
from igraph import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def most_important(data, name_file):
    G = nx.Graph()
    for i in data:
        G.add_edge(i[0], i[1], weight=1)
    ranking = nx.betweenness_centrality(G).items()
    r = [x[1] for x in ranking]
    m = sum(r)/len(r)  # centralidad
    t = m*3  # se mantiene los nodos  con promedio de aparicion de 3 veces
    Gt = G.copy()
    for k, v in ranking:
        if v < t:
            Gt.remove_node(k)
    nodes = [[i[0], i[1]] for i in Gt.edges.data()]
    labels = np.unique(nodes)
    print("Los nodos mas representatios son:",labels)

    g = Graph.TupleList([tuple(i) for i in data])
    g.vs["color"] = [
        'blue' if i in labels else 'white' for i in range(len(data))]
    layout = g.layout("kk")
    fig = plot(g, layout=layout)
    fig.save('./graphs/'+name_file+'_'+str(len(data))+'.png')
    return fig


def train_model(model, data):
    model.fit(data)
    print("Number of labels:", len(np.unique(model.labels_)))


def plot_graph(labels, data, color_dict, name_file):
    g = Graph.TupleList([tuple(i) for i in data])
    g.vs["color"] = [color_dict[i] for i in labels]
    layout = g.layout("kk")
    fig = plot(g, layout=layout)
    fig.save('./graphs/'+name_file+'_'+str(len(data))+'.png')
    return fig


def get_color_dict(colors):
    dicts = {}
    keys = range(len(colors))
    dicts[-1] = (255, 255, 255)
    for i in keys:
        dicts[i] = colors[i]
    return dicts


def rand_cmap(nlabels, type='bright', first_color_black=True, last_color_black=False, verbose=True):

    if type not in ('bright', 'soft'):
        print('Please choose "bright" or "soft" for type')
        return

    if verbose:
        print('Number of labels: ' + str(nlabels))

    # Generate color map for bright colors, based on hsv
    if type == 'bright':
        randHSVcolors = [(
            np.random.uniform(low=0.0, high=1),
            np.random.uniform(low=0.2, high=1),
            np.random.uniform(low=0.9, high=1)
        ) for i in xrange(nlabels)]

        # Convert HSV list to RGB
        randRGBcolors = []
        for HSVcolor in randHSVcolors:
            randRGBcolors.append(colorsys.hsv_to_rgb(
                HSVcolor[0], HSVcolor[1], HSVcolor[2]))

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]

        if last_color_black:
            randRGBcolors[-1] = [0, 0, 0]

        random_colormap = LinearSegmentedColormap.from_list(
            'new_map', randRGBcolors, N=nlabels)

    # Generate soft pastel colors, by limiting the RGB spectrum
    if type == 'soft':
        low = 0.6
        high = 0.95
        randRGBcolors = [(
            np.random.uniform(low=low, high=high),
            np.random.uniform(low=low, high=high),
            np.random.uniform(low=low, high=high)
        ) for i in xrange(nlabels)]

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]

        if last_color_black:
            randRGBcolors[-1] = [0, 0, 0]
        random_colormap = LinearSegmentedColormap.from_list(
            'new_map', randRGBcolors, N=nlabels)

    # Display colorbar
    if verbose:
        from matplotlib import colors, colorbar
        from matplotlib import pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(15, 0.5))

        bounds = np.linspace(0, nlabels, nlabels + 1)
        norm = colors.BoundaryNorm(bounds, nlabels)

        cb = colorbar.ColorbarBase(
            ax, cmap=random_colormap,
            norm=norm,
            spacing='proportional',
            ticks=None,
            boundaries=bounds,
            format='%1i',
            orientation=u'horizontal'
        )
    return randRGBcolors
