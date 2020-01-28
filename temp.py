# import collatzpy
# from collatzpy import tree
import random
import collatzpy.tree as ctree

tree = ctree.CTree()
tree.collect_from_range(2, 50000)

ctree.save(tree, 'mytree')

import collatzpy.plot as cplot

# cplot.path_plot(tree, 27)


selection = [random.randint(2, 50000) for n in range(10)]
print(selection)
cplot.path_plot_from_list(tree, selection)


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

# nMin = 10000
# nMax = 200000000
# nNums = 2000
# selection = [random.randint(nMin, nMax) for n in range(nNums)]
# print('start')
# tree.collect_from_list(selection)
# print('end')
# pathArgs = {'a1': 1.1, 'a2': .386, 'af': 1,
#             'e': 1.3, 'cmName': 'plasma_r',
#             'cmR': (0, 1)}

# cplot.angle_plot(tree, selection, **pathArgs)
