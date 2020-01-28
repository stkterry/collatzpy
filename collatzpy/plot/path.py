from .rc_cfg import set_config
from matplotlib import (
  pyplot as plt,
  colors,
  cm
)

plt.style.use('ggplot')
set_config(plt)

def path_plot(tree, n):
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
  _, ax = plt.subplots()

  for n in nList:
    path = tree.path(n)
    pathIdx = [x for x in range(1, len(path)+1)]

    path.reverse()
    plt.plot(pathIdx, path, label=f"{n}, {tree.refs[n].seqLen}")
    plt.fill_between(pathIdx, path, alpha=0.2)


  # plt.xlim([0, len(path)+1])
  ax.grid(which="minor", linestyle="--", color='#f2f2f2')
  leg = plt.legend(loc="upper left", title="N, SeqLen")
  # leg._legend_box.align = "right"
  plt.xlabel("Sequence Step")
  plt.ylabel("Integer Result")
  plt.ylim(bottom=2)
  plt.title(f"Multi-Path: Reverse Aligned")

  plt.show()
