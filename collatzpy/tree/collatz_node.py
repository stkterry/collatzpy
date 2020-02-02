class CollatzNode:
  """Node class for the CollatzTree class."""

  def __init__(self, n:int):
    self.n = n
    self.next = None
    self.seq_len = 0
    self.is_terminal = False