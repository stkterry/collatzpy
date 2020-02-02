from typing import TypeVar, List, Dict
CollatzTree = TypeVar('CollatzTree')

from matplotlib import pyplot as plt

from collatzpy.config import _MPL_STYLES_DIR
from .helpers import auto_name
PATH_STYLE = f'file://{_MPL_STYLES_DIR}/path.mplstyle'


def path(tree:CollatzTree, n:int, save:bool=False, output_name:str=None):
  """Plots the collatz sequence of n --> 1.

  Args:
    tree: An instance of the CollatzTree.
    n: The collatz number whose sequence you want to plot.
    save: Boolean, set to true if you want to save an image
      of your plot.  If you don't pass an output_name,
      a name will be generated automatically based on the
      local date/time and saved to the current working directory.
    output_name: The path/name of the image file you want to 
      save.  If you pass an output_name it will save
      without or without passing a save arg as well.
  """

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

  path = tree.path(n)
  seq_len = tree(n).seq_len
  pathIdx = [x for x in range(0, seq_len+1)]

  plt.plot(pathIdx, path)
  plt.fill_between(pathIdx, path, alpha=0.2)

  ax.grid(which="minor", linestyle="--", color='#f2f2f2')
  plt.xlim([0, seq_len])
  plt.ylim(bottom=2)
  plt.xlabel("Sequence Step")
  plt.ylabel("Integer Result")
  plt.title(f"N: {n}, Seq Length: {seq_len}")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()


def paths(tree:CollatzTree, selection:List[int],
          save:bool=False, output_name:str=None):
  """Plots the collatz sequence of n --> 1 for each n given.
  
  Paths are reverse-aligned to better demonstrate
  sequence overlap.  There's no limit on the size of the
  collection, but it's best to keep it short, as the
  legend is auto-generated from it and could be
  spuriously long.

  Args:
    tree: An instance of the CollatzTree.
    selection: A list of collatz number sequences you want to plot.
    save: Boolean, set to true if you want to save an image
      of your plot.  If you don't pass an output_name,
      a name will be generated automatically based on the
      local date/time and saved to the current working directory.
    output_name: The path/name of the image file you want to 
      save.  If you pass an output_name it will save
      without or without passing a save arg as well.
  """

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

  for n in selection:
    path = tree.path(n)
    seq_len = tree(n).seq_len
    path_idx = [x for x in range(0, seq_len + 1)]

    path.reverse()
    plt.plot(path_idx, path, label=f"{n}, {seq_len}")
    plt.fill_between(path_idx, path, alpha=0.1)

  ax.grid(which="minor", linestyle="--", color='#f2f2f2')
  plt.legend(loc="upper left", title="N, Seq Len")
  plt.xlabel("Sequence Step")
  plt.ylabel("Integer Result")
  plt.ylim(bottom=2)
  plt.title(f"Multi-Path: Reverse Aligned")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()
