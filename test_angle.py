import random
from collatzpy import tree, plot as cplot
from time import time
import numpy as np
import timeit


tree1 = tree.CTree()
tree2 = tree.CTree()
nMin = 10000
nMax = 200000000
nNums = 200
selection = [random.randint(nMin, nMax) for n in range(nNums)]
# tree1.collect_from_list(selection)

setup = '''
import random
from collatzpy import tree
tree1 = tree.CTree()
tree2 = tree.CTree()
nMin = 10000
nMax = 200000
nNums = 200

selection = [a for a in range(nMax)]
'''
c1 = '''
tree1.collect_from_list(selection)
'''
c2 = '''
tree2.collect_from_list2(selection)
'''

print(timeit.timeit(setup=setup, stmt=c1, number=100))
print(timeit.timeit(setup=setup, stmt=c2, number=100))

# start_time = time()
# tree1.collect_from_list(selection)
# t1 = (time()-start_time)
# print("c1 Elapsed time: " + str(t1))

# start_time = time()
# tree2.collect_from_list2(selection)
# t1 = (time()-start_time)
# print("c2 Elapsed time: " + str(t1))

# pathArgs = {'a1': 1.1, 'a2': .386, 'af': 1,
#             'e': 1.3, 'cmName': 'plasma_r',
#             'cmR': (0, 1), 'pointed': False}

# plotArgs = {'dpi': 100, 'facecolor': 'black',
#             'pxw': 2560/2, 'pxh': 1440/2}

# saveArgs = {'save': False}

# cplot.angle_plot(tree, selection, **plotArgs, **saveArgs, **pathArgs)
