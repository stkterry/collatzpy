import pygraphviz as pgv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from math import floor

from collatzpy.config import  _GRAPHVIZ_STYLES_DIR
from collatzpy.helpers import load_json

from .plot_helpers import auto_name, HexColorMap, fopen, set_size
attrs = load_json(_GRAPHVIZ_STYLES_DIR, 'default.json') 


def node_graph(tree, n_list, img_name=None, 
              write_dot=False, prog='dot', graph_attr=None):
  max_seq = tree.best()['seq_len']

  G = pgv.AGraph()
  G.graph_attr.update(**attrs['graph_attr'])
  if graph_attr: G.graph_attr.update(**graph_attr)
  G.node_attr.update(**attrs['node_attr'])
  G.edge_attr.update(**attrs['edge_attr'])

  cmap = HexColorMap('cool')

  G.add_node(1, fillcolor=cmap(0))
  seen = {1}
  edges = []

  for nn in n_list:
    node = tree(nn)
    while True:
      n = node.n
      if n in seen:
        break
      else:
        seen.add(n)
        G.add_node(n, fillcolor=cmap(node.seq_len/max_seq))
        edges.append((n, node.next.n))
        node = node.next
  
  for i, j in edges:
    G.add_edge(i, j)
  
  G.layout(prog=prog)

  img_name = img_name or auto_name('')
  
  if write_dot:
    G.write(f'{img_name}dot')

  G.draw(f'{img_name}png')

  img = mpimg.imread(f'{img_name}png')


  fig, ax = plt.subplots(1, 1)
  fig.patch.set_facecolor('black')
  plt.gca().set_position([0.025, 0.025, 0.95, 0.95])
  ax.autoscale(enable=True, axis="both", tight=False)
  ax.axis("off")
  set_size(fig, (12, 10))
  plt.imshow(img)
  plt.show()

  # fopen(f'{img_name}png')
