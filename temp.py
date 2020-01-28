# import collatzpy
# from collatzpy import tree
import random
import collatzpy.tree as ctree

tree = ctree.CTree()
tree.collect_from_range(2, 50000)

# ctree.save(tree, 'data/trees', 'mytree')

import collatzpy.plot as cplot

# cplot.path_plot(tree, 27)

selection = random.sample([n for n in range(2, 50000)], 10)
print(selection)
cplot.path_plot_from_list(tree, selection)
