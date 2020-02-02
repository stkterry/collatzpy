from typing import TypeVar
import dill

CollatzTree = TypeVar('CollatzTree')

def save_tree(tree:CollatzTree, fpath:str, fname:str) -> None:
  """Saves the given tree to the combined path 'fpath/fname'."""

  tree_file = open(fname, 'ab')
  dill.dump(tree, tree_file)
  tree_file.close()


def load_tree(fpath:str, fname:str) -> CollatzTree:
  """Loads a tree from the combined path 'fpath/fname'."""
  
  tree_file = open(fname, 'rb')
  tree = dill.load(tree_file)
  tree_file.close()

  return tree
