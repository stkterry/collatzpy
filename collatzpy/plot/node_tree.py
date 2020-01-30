import pygraphviz as pgv
from matplotlib import cm
from math import floor

from collatzpy.config import (
  _GRAPHVIZ_STYLES_DIR, 
  _NODE_GRAPH_IMG_DIR,
  _NODE_GRAPH_DOT_DIR
)

from .helpers import load_json, auto_name
attrs = load_json(f'{_GRAPHVIZ_STYLES_DIR}/default.json')

class rgbaMap():
  def __init__(self, cmap):
    self.cm = {0: None}
    self.__convert_cmap_to_rgba(cmap)

  def __convert_cmap_to_rgba(self, cmap):
    for i in range(0, 1024):
      rgba = (floor(x*255) for x in cmap(i/1023))
      self.cm[i] = "#{:02x}{:02x}{:02x}{:02x}".format(*rgba)
    

  def cmap(self, val):
    idx = floor(val * 1023)
    if idx in self.cm:
      return self.cm[idx]
    else:
      raise AttributeError("Wrong")


def node_tree(tree, n_list, img_name=None, 
              write_dot=False):
  max_seq = tree.longest_seq()['seqLen']

  G = pgv.AGraph()
  # for attr, val in attrs.graph_attr.items():
  #   G.graph_attr[attr] = val
  # for attr, val in attrs.node_attr.items():
  #   G.node_attr[attr] = val
  # for attr, val in attrs.edge_attr.items():
  #   G.edge_attr[attr] = val

  cmap = rgbaMap(cm.get_cmap('cool'))
  G.add_node(1, fillcolor=cmap.cmap(0))
  seen = {1}
  edges = []

  for nn in n_list:
    node = tree.refs[nn]
    while True:
      n = node.n
      if n in seen:
        break
      else:
        seen.add(n)
        G.add_node(n, fillcolor=cmap.cmap(node.seqLen/max_seq))
        edges.append((n, node.next.n))
        node = node.next
  
  for i, j in edges:
    G.add_edge(i, j)
  
  G.layout(prog='dot')

  img_name = img_name or auto_name(_NODE_GRAPH_IMG_DIR, '')
  
  if write_dot:
    G.write(f'{img_name}dot')

  G.draw(f'{img_name}png')
  

