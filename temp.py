# import collatzpy
# from collatzpy import tree
import random
import collatzpy.tree as ctree
import collatzpy.plot as cplot

# tree = ctree.CTree()
# tree.collect_from_range(2, 50000)

# ctree.save(tree, 'mytree')


# cplot.path_plot(tree, 27)


# selection = [random.randint(2, 50000) for n in range(10)]
# print(selection)
# cplot.path_plot_from_list(tree, selection)


# nMin = 2000
# nMax = 200000000
# nNums = 5000
# random.seed(111)
# treeArgs = {'nMin': 2000, 'nMax': 200000000,
#             'nNums': 10, 'tree': tree}
# selection = random.sample([n for n in range(nMin, nMax)], nNums)
# tree.collect_from_list(selection)
# pathArgs = {'a1': .3, 'a2': .38, 'af': 1.08,
#              'e': 1.3, 'cmName': 'plasma_r', 
#              'cmR': (0, 1)}
# saveArgs = {'save': True, 'output_name':'images/output.png',
#             'dpi':100, 'facecolor':'black', 'pxw':2560/2, 'pxh': 1440/2}

tree = ctree.CTree()
nMin = 10000
nMax = 200000000
nNums = 200
selection = [random.randint(nMin, nMax) for n in range(nNums)]
tree.collect_from_list(selection)

pathArgs = {'a1': 1.1, 'a2': .386, 'af': 1,
            'e': 1.3, 'cmName': 'plasma_r',
            'cmR': (0, 1), 'pointed': False}

plotArgs = {'dpi': 100, 'facecolor': 'black', 
            'pxw': 2560/2, 'pxh': 1440/2}

saveArgs = {'save': False}

cplot.angle_plot(tree, selection, **plotArgs, **saveArgs, **pathArgs)

# from time import time

# repeats = 200
# selection = [random.randint(2, 50000) for n in range(repeats)]

# stime = time()
# for n in selection: 
#   tree.path(n)
# print('path time:' + str((time() - stime)/repeats))

# stime = time()
# for n in selection:
#   tree.path_f(n)
# print('path_f time:' + str((time() - stime)/repeats))
# import faulthandler; faulthandler.enable()
# min = 2
# max = 50
# tree = ctree.CTree()
# tree.collect_from_range(min, max)

# cplot.node_tree(tree, [n for n in range(min, max)])