from matplotlib import pyplot as plt

from collatzpy.config import _MPL_STYLES_DIR
from .plot_helpers import auto_name
PATH_STYLE = f'file://{_MPL_STYLES_DIR}/path.mplstyle'


def path(tree, n, save=False, output_name=None):

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

  path = tree.path(n)
  pathIdx = [x for x in range(1, len(path)+1)]

  plt.plot(pathIdx, path)
  plt.fill_between(pathIdx, path, alpha=0.2)

  ax.grid(which="minor", linestyle="--", color='#f2f2f2')
  plt.xlim([0, len(path)+1])
  plt.ylim(bottom=2)
  plt.xlabel("Sequence Step")
  plt.ylabel("Integer Result")
  plt.title(f"N: {n}, Seq Length: {len(path)}")

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, bbox_inches="tight")

  plt.show()


def path_from_list(tree, nList, save=False, output_name=None):

  with plt.style.context(PATH_STYLE, 'ggplot'):
    _, ax = plt.subplots()

  for n in nList:
    path = tree.path(n)
    path_idx = [x for x in range(1, len(path)+1)]

    path.reverse()
    plt.plot(path_idx, path, label=f"{n}, {tree(n).seq_len}")
    plt.fill_between(path_idx, path, alpha=0.2)


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
