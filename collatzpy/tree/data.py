import pickle, dill

def save_tree(tree, fpath, fname):
  
  tree_file = open(fname, 'ab')
  dill.dump(tree, tree_file)
  tree_file.close()


def load_tree(fpath, fname):

  tree_file = open(fname, 'rb')
  tree = dill.load(tree_file)
  tree_file.close()

  return tree
