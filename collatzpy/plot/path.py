from matplotlib import pyplot as plt
import sys, os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def path_plot(tree, n):

  with plt.style.context(f'file://{THIS_DIR}/styles/path.mplstyle', 'ggplot'):
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

  plt.show()


def path_plot_from_list(tree, nList):

  with plt.style.context(f'file://{THIS_DIR}/styles/path.mplstyle', 'ggplot'):
    _, ax = plt.subplots()

  for n in nList:
    path = tree.path(n)
    pathIdx = [x for x in range(1, len(path)+1)]

    path.reverse()
    plt.plot(pathIdx, path, label=f"{n}, {tree.refs[n].seqLen}")
    plt.fill_between(pathIdx, path, alpha=0.2)


  ax.grid(which="minor", linestyle="--", color='#f2f2f2')
  plt.legend(loc="upper left", title="N, SeqLen")
  plt.xlabel("Sequence Step")
  plt.ylabel("Integer Result")
  plt.ylim(bottom=2)
  plt.title(f"Multi-Path: Reverse Aligned")

  plt.show()
