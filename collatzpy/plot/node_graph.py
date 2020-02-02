import pygraphviz as pgv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from math import floor

from collatzpy.config import  _GRAPHVIZ_STYLES_DIR
from collatzpy.helpers import load_json

from .helpers import auto_name, HexColorMap, set_size
attrs = load_json(_GRAPHVIZ_STYLES_DIR, 'default.json') 


def node_graph(tree, n_list, save=False, img_name=None, dot_name=None, write_dot=False, 
               prog='dot', show=True, graph_attr=None):
  """Generates a dot tree graph.
  
  Uses graphviz and pygraphviz.  By default images are shown through xlib.
  
  """

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
    node = tree[nn]
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

  img_name = img_name or auto_name('png')

  if save:
    G.draw(img_name)

  if write_dot or dot_name:
    dot_name = dot_name or f'{img_name[:-4]}.dot'
    G.write(dot_name)
      
  if show:
    G.draw('temp.xlib')


  # if show:
  #   img = mpimg.imread(img_name)

  #   fig, ax = plt.subplots(1, 1)
  #   fig.patch.set_facecolor('gray')
  #   plt.gca().set_position([0, 0, 1, 1])
  #   ax.autoscale(enable=True, axis="both", tight=False)
  #   ax.axis("off")
  #   if 'size' in G.graph_attr:
  #     size_str = G.graph_attr['size']
  #     size_str = size_str[:-1] if size_str[-1] == '!' else size_str
  #     size = (float(x) for x in size_str.split(','))
  #     set_size(fig, size)
  #   plt.imshow(img)
  #   plt.show()

