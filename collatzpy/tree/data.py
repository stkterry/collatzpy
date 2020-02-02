from typing import TypeVar
import dill

CollatzTree = TypeVar('CollatzTree')

def save_tree(tree:CollatzTree, fpath:str, fname:str) -> None:
  """Saves the given tree to the combined path 'fpath/fname'.

  Args:
    tree: An instance of the CollatzTree.
    fpath: A string pointed to a directory.
    fname: The filename for your saved tree.
  """

  tree_file = open(fname, 'ab')
  dill.dump(tree, tree_file)
  tree_file.close()


def load_tree(fpath:str, fname:str) -> CollatzTree:
  """Loads a tree from the combined path 'fpath/fname'.


  Args:
    fpath: A string pointed to a directory.
    fname: The filename of the tree you want to load.
  """
  tree_file = open(fname, 'rb')
  tree = dill.load(tree_file)
  tree_file.close()

  return tree
