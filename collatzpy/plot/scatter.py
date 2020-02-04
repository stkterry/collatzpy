from typing import TypeVar, List

from matplotlib import pyplot as plt, cm
from matplotlib.lines import Line2D

from collatzpy.config import _MPL_STYLES_DIR
from .helpers import auto_name, seqs
from .helpers.colormaps import parula as cm_parula

CollatzTree = TypeVar('CollatzTree')

PATH_STYLE = f'file://{_MPL_STYLES_DIR}/scatter.mplstyle'


def scatter_heat(tree: CollatzTree, selection: List[int] = None,
                 save: bool = False, output_name: str = None):
  """A 'total stopping time' plot with heatmap.

  Uses the sequence length frequency for heat projection.
  X-axis/Y-axis is collatz number / sequence length. Leaving
  selection blank will default to using all terminal nodes.

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

  max_count = max(seq_count.values())
  min_count = min(seq_count.values())

  colors = [seq_count[seq_len] for seq_len in seq_lens]

  with plt.style.context(PATH_STYLE, 'ggplot'):

    _, ax = plt.subplots(1, 1)
    plt.scatter(selection, seq_lens, c=colors, cmap=cm_parula)
    plt.colorbar(ax=ax, label="Frequency", pad=0.05)
    plt.clim(min_count, max_count)
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, len(selection) + 10])
    plt.ylim(bottom=2)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Total Stopping Time")
    plt.subplots_adjust(right=1, left=0.1)

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()


def scatter_tst(tree: CollatzTree, selection: List[int] = None,
                save: bool = False, output_name: str = None):
  """A 'total stopping time' plot with even/odd delineation.

  X-axis/Y-axis is collatz number / sequence length. Leaving
  selection blank will default to using all terminal nodes.

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

  cmap = cm.get_cmap('coolwarm')

  selection = selection or tree.terminals()
  seq_lens = seqs.seq_lens(tree, selection)

  colors = [cmap(1.0) if n % 2 else cmap(0.0) for n in selection]

  with plt.style.context(PATH_STYLE, 'ggplot'):

    legend = [
        Line2D([0], [0], markerfacecolor=cmap(0.0), marker='o', markersize=10,
               markeredgecolor='none', color='none', lw=4, label='Even'),
        Line2D([0], [0], markerfacecolor=cmap(1.0), marker='o', markersize=10,
               markeredgecolor='none', color='none', lw=4, label='Odd')
    ]

    _, ax = plt.subplots()

    plt.scatter(selection, seq_lens, c=colors)
    ax.legend(handles=legend)
    ax.grid(which="minor", linestyle="--", color='#f2f2f2')
    plt.xlim([0, len(selection) + 1])
    plt.ylim(bottom=2)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Total Stopping Time")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()


def hexbin(tree: CollatzTree, selection: List[int] = None, gridsize: int = 50,
           save: bool = False, output_name: str = None):
  """A 'total stopping time' heatmap using a hexbin.

  Uses the sequence length frequency for heat projection.
  X-axis/Y-axis is collatz number / sequence length. Leaving
  selection blank will default to using all terminal nodes.

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

  max_count = max(seq_count.values())
  min_count = min(seq_count.values())

  colors = [seq_count[slen] for slen in seq_lens]

  with plt.style.context(PATH_STYLE, 'ggplot'):

    _, ax = plt.subplots(1, 1)
    plt.hexbin(selection, seq_lens, C=colors,
               gridsize=gridsize, cmap=cm_parula)
    plt.clim(min_count, max_count)
    ax.grid(False, which="both")
    plt.xlim([0, len(selection) + 10])
    plt.ylim(bottom=2)
    plt.colorbar(ax=ax, label="Frequency", pad=0.05)
    plt.xlabel("Collatz number")
    plt.ylabel("Sequence Length")
    plt.title("Frequency Hexbin Heatmap")
    plt.subplots_adjust(right=1, left=0.1)

    if save or output_name:
      output_name = output_name or auto_name('png')
      plt.savefig(output_name, bbox_inches="tight")

  plt.show()
