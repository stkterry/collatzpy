from typing import TypeVar, List, Dict

CollatzTree = TypeVar('CollatzTree')


def seq_lens(tree:CollatzTree, selection:List[int]) -> List[int]:
  """Returns an unordered list of sequence lengths.
  
  For each n in selection, adds the corresponding node's
  sequence length to a list.
  """
  seq_lens = [None] * len(selection)
  for i, n in enumerate(selection):
    seq_lens[i] = tree[n].seq_len
  
  return seq_lens

def seq_hist(seq_lens:List[int]) -> Dict[int, int]:
  """Returns a dict of sequence_length/count key/val pairs.
  
  For each entry in the list of sequence lengths, tabulates
  the frequency of appearance in the list and returns the
  data as a dict.  Useful for histogram operations on sequence 
  length.
  """
  seq_count = {}
  for slen in seq_lens:
    if slen in seq_count: seq_count[slen] += 1
    else: seq_count[slen] = 1
  
  return seq_count