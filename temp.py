# import collatzpy
# from collatzpy import tree

import collatzpy.tree as ctree

tree = ctree.CTree()
tree.collect_from_range(2, 50000)

ctree.save(tree, 'data/trees', 'mytree')