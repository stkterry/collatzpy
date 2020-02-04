class CollatzNode:
  """Node class for the CollatzTree class."""

  def __init__(self, n: int):
    self.n = n
    self.next = None
    self.seq_len = 0
    self.is_terminal = False

  def __eq__(self, other):
    return (
        isinstance(other, CollatzNode)
        and self.n == other.n
        and self.next == other.next
        and self.seq_len == other.seq_len
        and self.is_terminal == other.is_terminal
    )
