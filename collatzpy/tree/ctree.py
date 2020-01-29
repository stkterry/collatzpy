from .cnode import CNode
from itertools import count

class NodeIter:
  def __init__(self, node):
    self.current_node = node
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.current_node.next:
      self.current_node = self.current_node.next
      return self.current_node.n
    else: 
      raise StopIteration
      


class CTree:

  def __init__(self):
    self.root = CNode(1)
    self.refs = {1: self.root}

  def calc_next(self, n):
    return (n // 2) if (n % 2 == 0) else (3 * n + 1)

  def __add_node(self, n):
    node = CNode(n)
    self.refs[n] = node
    return node

  def collect(self, n):
    if n in self.refs: return

    node = self.__add_node(n)
    new_nodes = [node]

    while True:
      n = self.calc_next(n)

      if n in self.refs:
        node.next = self.refs[n]

        seqLen = node.next.seqLen
        l = len(new_nodes)
        for i, new_node in enumerate(new_nodes):
          new_node.seqLen += seqLen + l - i
        break

      node.next = self.__add_node(n)
      node = node.next
      new_nodes.append(node)

  def collect_from_range(self, a, b):
    a = 2 if a < 2 else a
    for n in range(a, b+1): self.collect(n)
  
  def collect_from_list(self, nlist):
    nlist = [n for n in nlist if n > 1]
    for n in nlist: self.collect(n)
  

  def path(self, n):
    if not n in self.refs: return []

    node = self.refs[n]
    path = [0] * (node.seqLen + 1)
    for i in count():
      path[i] = node.n
      node = node.next
      if not node: break
    
    return path

  def longest_seq(self):
    n = None
    seqLen = 0
    for i, node in self.refs.items():
      if node.seqLen > seqLen:
        seqLen = node.seqLen
        n = i
    
    return {'n': n, 'seqLen': seqLen}
