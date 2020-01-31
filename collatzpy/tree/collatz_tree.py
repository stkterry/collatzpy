from .collatz_node import CollatzNode as CNode
from itertools import count
import numpy as np

class CollatzTree:

  def __init__(self):
    self.__root = CNode(1)
    self.__best_node = self.__root
    self.__refs = {1: self.__root}

  def __call__(self, n):
    if n in self.__refs:
      return self.__refs[n]
  
  def has(self, n):
    return n in self.__refs

  def splay(self, n):
    if not self.has(n): return
    node = self.__refs[n]
    info = {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n}
    return info

  def best(self):
    node = self.__best_node
    return {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n}

  def calc_next(self, n):
    return (n // 2) if (n % 2 == 0) else (3 * n + 1)

  def __add_node(self, n):
    node = CNode(n)
    self.__refs[n] = node
    return node

  def collect(self, n):
    if self.has(n): return

    node = self.__add_node(n)
    new_nodes = [node]

    while True:
      n = self.calc_next(n)

      if self.has(n):
        node.next = self(n)

        seq_len = node.next.seq_len
        l = len(new_nodes)
        for i, new_node in enumerate(new_nodes):
          new_node.seq_len += seq_len + l - i
        
        if new_nodes[0].seq_len >= self.__best_node.seq_len:
          self.__best_node = new_nodes[0]
        break

      node.next = self.__add_node(n)
      node = node.next
      new_nodes.append(node)

  def collect2(self, n):
    if self.has(n): return

    node = self.__add_node(n)
    new_nodes = [node]

    while True:
      n = self.calc_next(n)

      if self.has(n):
        node.next = self(n)

        seq_len = node.next.seq_len
        l = len(new_nodes)
        for i, new_node in enumerate(new_nodes):
          new_node.seq_len += seq_len + l - i
        
        if new_nodes[0].seq_len >= self.__best_node.seq_len:
          self.__best_node = new_nodes[0]
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
    if not n in self.__refs: return []

    node = self.__refs[n]
    path = [None] * (node.seq_len + 1)
    for i in count():
      path[i] = node.n
      node = node.next
      if not node: break
    
    return path

  def longest_seq(self):
    n = None
    seq_len = 0
    for i, node in self.__refs.items():
      if node.seq_len > seq_len:
        seq_len = node.seq_len
        n = i
    
    return {'n': n, 'seq_len': seq_len}

  def size(self):
    return len(self.__refs)