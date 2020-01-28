import pickle

from collatzpy.config import _DATA_DIR

def save(tree, fname):

  tree_file = open(f'{_DATA_DIR}/trees/{fname}', 'ab')
  pickle.dump(tree, tree_file)
  tree_file.close()


def load(fname):

  tree_file = open(f'{_DATA_DIR}/trees/{fname}', 'rb')
  tree = pickle.load(tree_file)
  tree_file.close()

  return tree
