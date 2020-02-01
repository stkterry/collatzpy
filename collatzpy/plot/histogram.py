from matplotlib import pyplot as plt, mlab, cm
from matplotlib.lines import Line2D
import numpy as np

from collatzpy.config import _MPL_STYLES_DIR
from .plot_helpers import auto_name
PATH_STYLE = f'file://{_MPL_STYLES_DIR}/scatter.mplstyle'


def histogram(tree, rng, save=False, output_name=None):

  x, y, h = [], [], []
  seq_count = {}
  for _, node in tree.filter(lambda j: j[0] > rng[0] and j[0] < rng[1]):
    h.append(node.seq_len)
    if node.seq_len in seq_count:
      seq_count[node.seq_len] += 1
    else:
      seq_count[node.seq_len] = 1
    
  for seq_len, cnt in sorted(seq_count.items(), key = lambda j: j[0]):
    x.append(seq_len)
    y.append(cnt)

  # max_count = max(seq_count.values())
  # min_count = min(seq_count.values())

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

    plt.bar(x, y, align='edge', width=1)
    # plt.yscale('log')
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, seq_len])
    plt.ylim(bottom=2)
    plt.xlabel("Sequence Length")
    plt.ylabel("Frequency")
    plt.title("Histogram")

    # if save or output_name:
    #   output_name = output_name or auto_name('png')
    #   plt.savefig(output_name, bbox_inches="tight")

  plt.show()


# def histogram(tree, rng, save=False, output_name=None):

#   x, y = [], []
#   seq_count = {}
#   for n, node in tree.filter(lambda j: j[0] > rng[0] and j[0] < rng[1]):
#     x.append(n)
#     y.append(node.seq_len)

#     if node.seq_len in seq_count:
#       seq_count[node.seq_len] += 1
#     else:
#       seq_count[node.seq_len] = 1

#   nx, ny = [], []
#   for seq_len, cnt in sorted(seq_count.items(), key=lambda j: j[0]):
#     x.append(seq_len)
#     y.append(cnt)

#   max_count = max(seq_count.values())
#   min_count = min(seq_count.values())

#   with plt.style.context(PATH_STYLE, 'ggplot'):
#     _, ax = plt.subplots()

#     plt.plot(nx, ny)
#     plt.show()

#   # path = tree.path(n)
#   # seq_len = tree(n).seq_len
#   # pathIdx = [x for x in range(0, seq_len+1)]

#   # plt.plot(pathIdx, path)
#   # plt.fill_between(pathIdx, path, alpha=0.2)

#   # ax.grid(which="minor", linestyle="--", color='#f2f2f2')
#   # plt.xlim([0, seq_len])
#   # plt.ylim(bottom=2)
#   # plt.xlabel("Sequence Step")
#   # plt.ylabel("Integer Result")
#   # plt.title(f"N: {n}, Seq Length: {seq_len}")

#   # if save or output_name:
#   #   output_name = output_name or auto_name('png')
#   #   plt.savefig(output_name, bbox_inches="tight")

#   # plt.show()




