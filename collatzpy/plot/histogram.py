from matplotlib import pyplot as plt, mlab, cm

from collatzpy.config import _MPL_STYLES_DIR
from .helpers import auto_name, seqs
PATH_STYLE = f'file://{_MPL_STYLES_DIR}/scatter.mplstyle'


def histogram(tree, selection:list=None, save:bool=False, output_name:str=None):
  """Plots a histogram of the given tree.
  
  If no selection is given, the histogram will use terminal nodes in the tree. 
  """

  selection = selection or tree.terminals()
  seq_lens = seqs.seq_lens(tree, selection)
  seq_count = seqs.seq_hist(seq_lens)

  x, y = [], []
  for seq_len, cnt in sorted(seq_count.items(), key = lambda j: j[0]):
    x.append(seq_len)
    y.append(cnt)

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

    plt.bar(x, y, align='center', width=1, alpha=0.5)
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, len(x) + 1])
    plt.ylim(bottom=2)
    plt.xlabel("Sequence Length")
    plt.ylabel("Frequency")
    plt.title("Histogram")

    if save or output_name:
      output_name = output_name or auto_name('png')
      plt.savefig(output_name, bbox_inches="tight")

  plt.show()

