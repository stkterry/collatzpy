from typing import TypeVar, List

from matplotlib import pyplot as plt, cm
from matplotlib.collections import LineCollection as LC
import numpy as np
from random import uniform

from .helpers import set_size, auto_name

CollatzTree = TypeVar('CollatzTree')


def angle_path(tree: CollatzTree, selection: List[int] = None,
               alpha: float = 0.3, beta: float = 0.38, gamma: float = 1.08,
               sigma: float = 1.3, cmName: str = 'plasma_r',
               cmR: tuple = (0, 1), pointed: bool = False, save: bool = False,
               dpi: int = 100, pxw: int = 2560, pxh: int = 1440,
               facecolor: str = 'black', output_name: str = None):
  """Plots a path using even/odd parity for each step in a sequence.

  For each sequence n -> 1, traces a path turning left/right each
  step k, determined by whether k is even/odd.

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
    alpha: Affects maximum rotation per step.
    beta: Works with gamma to set the left/right turn ratio.
    gamma: Works with beta to set the left/right turn ratio.
    sigma: Affects the length of each successive step.  Values
      larger than 1 will increasingly lower the maximum bounded
      length of the path.
    cmName: The color map used in the resultant image.  Accepts
      any string recognized by matplotlib's cm library.
    cmR: Sets the range of colors to use in the color map.
    pointed: If true, each path will slowly taper to a point.
      Drawbacks are longer draw times and potentially visibly
      segmented lines.
    facecolor: The background color for the image.
    dpi: Dots per inch of the saved image.
    pxw: Width of the image in pixels.
    pxh: Height of the image in pixels.
  """

  selection = selection or tree.terminals()

  cmap = cm.get_cmap(cmName)
  nMax = max(selection)

  fig, ax = plt.subplots(1, 1)
  fig.patch.set_facecolor(facecolor)
  plt.gca().set_position([0.025, 0.025, 0.95, 0.95])

  for n in selection:

    path = np.asarray(tree.path(n))
    path = path[::-1]
    pathLen = len(path)

    rho = path / (1 + path**sigma)
    theta = alpha * (beta - gamma * (path % 2))
    theta = np.cumsum(theta)
    xy = np.array([rho * np.cos(theta),
                   rho * np.sin(theta)])
    xy = np.cumsum(xy, 1)

    lmax = 6 * (nMax - n) / nMax
    color = cmap(uniform(*cmR))
    opacity = 0.5 * ((n / nMax)**3)

    if pointed:
      lwidths = [lmax - x * lmax / pathLen for x in range(pathLen)]
      points = xy.T.reshape(-1, 1, 2)
      segments = np.concatenate([points[:-1], points[1:]], axis=1)
      lc = LC(segments, color=color, alpha=opacity, linewidths=lwidths)
      ax.add_collection(lc)
    else:
      plt.plot(xy[0], xy[1], color=color, alpha=opacity, linewidth=lmax)

  ax.autoscale(enable=True, axis="both", tight=False)
  ax.axis("off")
  set_size(fig, (pxw / dpi, pxh / dpi))

  if save or output_name:
    output_name = output_name or auto_name('png')
    plt.savefig(output_name, facecolor=facecolor,
                bbox_inches="tight")

  plt.show()
