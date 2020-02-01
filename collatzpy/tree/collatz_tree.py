from .collatz_node import CollatzNode as CNode
from itertools import count
import numpy as np

class CollatzTree(dict):

  def __init__(self):
    self.__root = CNode(1)
    self.__best_node = self.__root
    self[1] = self.__root

  def __call__(self, n):
    if n in self:
      return self[n]
  
  def has(self, n):
    return n in self

  def splay(self, n):
    if not self.has(n): return
    node = self[n]
    info = {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n}
    return info

  def best(self):
    node = self.__best_node
    return {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n}

  def calc_next(self, n):
    return (3 * n + 1) if (n % 2) else (n // 2)

  def __add_node(self, n):
    node = CNode(n)
    self[n] = node
    return node

  def collect(self, n):
    if n in self: return

    sn = n
    seq = 1
    node = self.__add_node(n)

    while True:
      n = self.calc_next(n)

      if n in self:
        node.next = self[n]

        seq_len = node.next.seq_len
        node = self[sn]
        while seq > 0:
          node.seq_len = seq_len + seq
          node = node.next
          seq -= 1

        if self[n].seq_len >= self.__best_node.seq_len:
          self.__best_node = self[sn]
        break

      node.next = self.__add_node(n)
      node = node.next
      seq += 1


  def collect_from_range(self, a, b):
    a = 2 if a < 2 else a
    for n in range(a, b+1): self.collect(n)
  
  def collect_from_list(self, nlist):
    nlist = [n for n in nlist if n > 1]
    for n in nlist: self.collect(n)

  def path(self, n):
    if not n in self: return []

    node = self[n]
    path = [None] * (node.seq_len + 1)
    for i in count():
      path[i] = node.n
      node = node.next
      if not node: break
    
    return path


  def longest_seq(self):
    n = None
    seq_len = 0
    for i, node in self.items():
      if node.seq_len > seq_len:
        seq_len = node.seq_len
        n = i
    
    return {'n': n, 'seq_len': seq_len}

  def size(self):
    return len(self)
