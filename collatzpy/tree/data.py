import pickle
# import pathlib
# THIS_DIR = pathlib.Path().absolute()

def save(tree, fpath):

  tree_file = open(fpath, 'ab')
  pickle.dump(tree, tree_file)
  tree_file.close()


def load(fpath):

  tree_file = open(fpath, 'rb')
  tree = pickle.load(tree_file)
  tree_file.close()

  return tree
