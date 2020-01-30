import pygraphviz as pgv
from math import floor

from collatzpy.config import (
  _GRAPHVIZ_STYLES_DIR, 
  _NODE_GRAPH_IMG_DIR,
  _NODE_GRAPH_DOT_DIR
)

from .helpers import load_json, auto_name, HexColorMap, fopen
attrs = load_json(f'{_GRAPHVIZ_STYLES_DIR}/default.json')

def node_tree(tree, n_list, img_name=None, 
              write_dot=False, prog='dot'):
  max_seq = tree.longest_seq()['seqLen']

  G = pgv.AGraph()
  G.graph_attr.update(**attrs['graph_attr'])
  G.node_attr.update(**attrs['node_attr'])
  G.edge_attr.update(**attrs['edge_attr'])

  cmap = HexColorMap('cool')

  G.add_node(1, fillcolor=cmap(0))
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
        G.add_node(n, fillcolor=cmap(node.seqLen/max_seq))
        edges.append((n, node.next.n))
        node = node.next
  
  for i, j in edges:
    G.add_edge(i, j)
  
  G.layout(prog=prog)

  img_name = img_name or auto_name(_NODE_GRAPH_IMG_DIR, '')
  
  if write_dot:
    G.write(f'{img_name}dot')

  G.draw(f'{img_name}png')

  fopen(f'{img_name}png')