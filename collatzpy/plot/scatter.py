from matplotlib import pyplot as plt, mlab, cm
from matplotlib.lines import Line2D

from collatzpy.config import _MPL_STYLES_DIR
from .plot_helpers import auto_name
from .plot_helpers.colormaps import parula as cm_parula
PATH_STYLE = f'file://{_MPL_STYLES_DIR}/scatter.mplstyle'


def scatter_heat(tree, rng, save=False, output_name=None):

  x, y = [], []
  for n, node in tree.filter(lambda j: j[0] > rng[0] and j[0] < rng[1]):
    x.append(n)
    y.append(node.seq_len)

  seq_count = {}
  for slen in y:
    if slen in seq_count: seq_count[slen] += 1
    else : seq_count[slen] = 0
  max_count = max(seq_count.values())
  min_count = min(seq_count.values())
  
  colors = [seq_count[slen] for slen in y]


  with plt.style.context(PATH_STYLE, 'ggplot'):

    _, ax = plt.subplots(1, 1)
    plt.scatter(x, y, c=colors, cmap=cm_parula)
    plt.colorbar(ax=ax, label="Frequency", pad=0.05)
    plt.clim(min_count, max_count)
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, len(x)+10])
    plt.ylim(bottom=2)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Total Stopping Time")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.subplots_adjust(right=1, left=0.1)

  plt.margins()
  plt.show()


def scatter_tst(tree, rng, save=False, output_name=None):
  
  cmap = cm.get_cmap('coolwarm')

  x, y = [], []
  for n, node in tree.filter(lambda j: j[0] > rng[0] and j[0] < rng[1]):
    x.append(n)
    y.append(node.seq_len)

  colors = [cmap(1.0) if n % 2 else cmap(0.0) for n in x]
  # sizes = [15*(seq_count[slen]/max_count)**2 + 3 for slen in y]

  with plt.style.context(PATH_STYLE, 'ggplot'):

    legend = [
      Line2D([0], [0], markerfacecolor=cmap(0.0), marker='o', markersize=10,
             markeredgecolor='none', color='none', lw=4, label='Even'),
      Line2D([0], [0], markerfacecolor=cmap(1.0), marker='o', markersize=10,
             markeredgecolor='none', color='none', lw=4, label='Odd')
    ]

    _, ax = plt.subplots()

    plt.scatter(x, y, c=colors)
    ax.legend(handles=legend)
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, len(x)+1])
    plt.ylim(bottom=2)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Total Stopping Time")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()


def hexbin(tree, rng, save=False, output_name=None):

  x, y = [], []
  for n, node in tree.filter(lambda j: j[0] > rng[0] and j[0] < rng[1]):
    x.append(n)
    y.append(node.seq_len)

  seq_count = {}
  for slen in y:
    if slen in seq_count:
      seq_count[slen] += 1
    else:
      seq_count[slen] = 1
  max_count = max(seq_count.values())
  min_count = min(seq_count.values())

  colors = [seq_count[slen] for slen in y]

  with plt.style.context(PATH_STYLE, 'ggplot'):

    _, ax = plt.subplots(1, 1)
    plt.hexbin(x, y, C=colors, gridsize=50, cmap=cm_parula)
    plt.clim(min_count, max_count)
    ax.grid(False, which="both")
    plt.xlim([0, len(x)+10])
    plt.ylim(bottom=2)
    plt.colorbar(ax=ax, label="Frequency", pad=0.05)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Frequency Heatmap")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.subplots_adjust(right=1, left=0.1)

  plt.margins()
  plt.show()
