from itertools import count
from typing import List, Callable, Iterator
from . import CollatzNode


class CollatzTree(dict):
  """Dictionary based tree that stores collatz numbers and sequences.

  Extends dict.  Uses CollatzNodes to create a collection of linked-lists.
  Each node in the dict is keyed by its collatz number and points to its
  subsequent node in its sequence. Any node in the list 'paths' back to 1.

  Tree is initialzed with the node n=1.
  """

  def __init__(self):
    self[1] = CollatzNode(1)
    self.__best_node = self[1]




  def has(self, n: int) -> bool:
    """Returns boolean True/False if n is contained in the tree."""
    return n in self

  def splay(self, n: int) -> dict:
    """Returns a dict of attributes for node n."""
    if n not in self:
      return None
    node = self[n]
    info = {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n, 'is_terminal': node.is_terminal}
    return info

  def best(self) -> dict:
    """Returns a dict of attributes for the node with the longest sequence."""
    node = self.__best_node
    return {'n': node.n, 'seq_len': node.seq_len,
            'next': node.next.n, 'is_terminal': node.is_terminal}

  def calc_next(self, n: int) -> int:
    """Given n, returns the next collatz number in the sequence of n"""
    return (3 * n + 1) if (n % 2) else (n // 2)

  def __add_node(self, n: int):
    node = CollatzNode(n)
    self[n] = node
    return node

  def collect(self, n: int) -> None:
    """Given n, gets the collatz sequence (n -> 1) and adds it to the tree.

    Will skip previously calculated sequences.  Updates the best node if
    one is found.  Calculates the sequence length for each node it finds
    and updates the nodes. Nodes explicitly passed to collect() are marked
    terminal but nodes in the path from n --> 1 are not. Nodes are updated
    as terminal if passed to collect() but have already been sequenced.
    """
    if n in self:
      self[n].is_terminal = True
      return

    sn = n
    seq = 1
    node = self.__add_node(n)
    node.is_terminal = True

    while True:
      n = self.calc_next(n)

      if n in self:
        node.next = self[n]

        seq_len = node.next.seq_len
        node = self[sn]
        while seq:
          node.seq_len = seq_len + seq
          node = node.next
          seq -= 1

        if self[sn].seq_len >= self.__best_node.seq_len:
          self.__best_node = self[sn]
        break

      node.next = self.__add_node(n)
      node = node.next
      seq += 1

  def collect_from_range(self, a: int, b: int = None) -> None:
    """Collects values in the range (a, b), inclusive.

    Values should be in the range (1, n).  Lower bounds less than 1
    will be set to 1.  Users may chose to pass only an upper bound,
    the lower bound will be set automatically to 1.
    """
    if not b:
      b = a
      a = 1
    else:
      a = 1 if a < 1 else a
    for n in range(a, b + 1):
      self.collect(n)

  def collect_from_list(self, collection: list) -> None:
    """Collects values given in the list.

    Values in the list should be in the range (1, n), inclusive. The list
    given will be filtered to accomadate this requirement.
    """
    collection = [n for n in collection if n >= 1]
    for n in collection:
      self.collect(n)

  def path(self, n: int) -> List[int]:
    """Given n, will return a list of integers in the sequence from n--> 1.

    Will return an empty list for values of n not previously sequenced.
    """
    if n not in self:
      return []

    node = self[n]
    path = [None] * (node.seq_len + 1)
    for i in count():
      path[i] = node.n
      node = node.next
      if not node:
        break

    return path

  def filter(self, fn: Callable) -> Iterator[tuple]:
    """Returns an iterable filter of the (n, node) pairs in the tree."""
    return filter(fn, self.items())

  def size(self) -> int:
    """Returns the total number of nodes in the tree.

    Equivalent to len(tree).
    """
    return len(self)

  def terminals(self) -> List[int]:
    """Returns a list of all terminal nodes."""
    terminals = []
    for n, _ in filter(lambda j: j[1].is_terminal, self.items()):
      terminals.append(n)
    return terminals
