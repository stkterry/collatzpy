from typing import TypeVar, List

from matplotlib import pyplot as plt

from collatzpy.config import _MPL_STYLES_DIR
from .helpers import auto_name, seqs

CollatzTree = TypeVar('CollatzTree')

PATH_STYLE = f'file://{_MPL_STYLES_DIR}/scatter.mplstyle'


def histogram(tree: CollatzTree, selection: List[int] = None,
              save: bool = False, output_name: str = None):
  """Plots a histogram of the given tree's sequence lengths.

  The histogram consists of taking each n in the given
  selection and tabulating the frequency/count of the sequence
  lengths.

  Args:
    tree: An instance of the CollatzTree.
    selection: A list of collatz numbers you want to plot.
      If no selection is passed, all terminal nodes in the
      tree will be used.
    save: Boolean, set to true if you want to save an image
      of your plot.  If you don't pass an output_name,
      a name will be generated automatically based on the
      local date/time and saved to the current working directory.
    output_name: The path/name of the image file you want to
      save.  If you pass an output_name it will save
      without or without passing a save arg as well.
  """

  selection = selection or tree.terminals()
  seq_lens = seqs.seq_lens(tree, selection)
  seq_count = seqs.seq_hist(seq_lens)

  x, y = [], []
  for seq_len, cnt in sorted(seq_count.items(), key=lambda j: j[0]):
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
