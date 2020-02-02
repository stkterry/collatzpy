from typing import TypeVar, List
import pygraphviz as pgv

from collatzpy.config import _GRAPHVIZ_STYLES_DIR
from collatzpy.helpers import load_json
from .helpers import auto_name, HexColorMap

CollatzTree = TypeVar('CollatzTree')
attrs = load_json(_GRAPHVIZ_STYLES_DIR, 'default.json')


def node_graph(tree: CollatzTree, selection: List[int] = None,
               save: bool = False, img_name: str = None, dot_name: str = None,
               prog: str = 'dot', write_dot: bool = False, show: bool = True,
               graph_attr: dict = None, node_attr: dict = None,
               edge_attr: dict = None):

  """Generates a dot tree graph.

  Uses graphviz and pygraphviz.  By default images are shown
  through xlib.  graph_att, node_attr, and edge_attr will
  take most graphviz attributes wrapped as a dict and
  apply them to the graph.

  Args:
    tree: An instance of the CollatzTree class.
    selection: The list of collatz numbers you wish to graph.
      If you leave selection blank the graph will default
      to using all nodes marked as terminal in the tree.
    save: If true the graph will be saved as a png format.
      If you don't include an img_name, a name will be
      automatically generated based on the current
      local time/date and the image will be saved to the
      current directory.
    img_name: The dir/name of the output image file.
    write_dot: If true the graph will be saved as dot
      format.  If neither img_name nor dot_name are given
      the dot file will share the same name and directory
      of the auto-generated img_name.  If an img_name is
      specified the dot_file will share that name/dir instead.
    dot_name: The dir/name of the output dot file.
    show: If true the function will try and show the image
      via xlib/x11.
    graph_attr: A dict of graphviz compatible attributes
      for the graph.
    node_attr: A dict of graphviz compatible attributes
      for the nodes.
    edge_attr: A dict of graphviz compatible attributes
      for the edges.
  """
  selection = selection or tree.terminals()

  max_seq = tree.best()['seq_len']

  G = pgv.AGraph()
  G.graph_attr.update(**attrs['graph_attr'])
  if graph_attr:
    G.graph_attr.update(**graph_attr)
  G.node_attr.update(**attrs['node_attr'])
  if node_attr:
    G.node_attr.update(**node_attr)
  G.edge_attr.update(**attrs['edge_attr'])
  if edge_attr:
    G.edge_attr.update(**edge_attr)

  cmap = HexColorMap('cool')

  G.add_node(1, fillcolor=cmap(0))
  seen = {1}
  edges = []

  for nn in selection:
    node = tree[nn]
    while True:
      n = node.n
      if n in seen:
        break
      else:
        seen.add(n)
        G.add_node(n, fillcolor=cmap(node.seq_len / max_seq))
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
