from matplotlib import pyplot as plt, cm
from matplotlib.collections import LineCollection as LC
import numpy as np
from random import uniform
from time import localtime, strftime

from .helpers.size_fix import set_size
from collatzpy.config import _IMG_DIR

def angle_plot(tree, selection, a1=0.3, a2=0.38, af=1.08,
               e=1.3, cmName='plasma_r', cmR=(0, 1), pointed=False,
               save=False, dpi=100, facecolor='black',
               output_name=None, pxw=2560, pxh=1440):

  cmap = cm.get_cmap(cmName)
  nMax = max(selection)

  fig, ax = plt.subplots(1, 1)
  fig.patch.set_facecolor(facecolor)
  plt.gca().set_position([0.025, 0.025, 0.95, 0.95])

  for n in selection:

    path = np.asarray(tree.path(n))
    path = path[::-1]
    pathLen = len(path)

    rho = path / (1 + path**e)
    theta = a1 * (a2 - af * (path % 2))
    theta = np.cumsum(theta)
    xy = np.array([rho * np.cos(theta), 
                   rho * np.sin(theta)])

    xy = np.cumsum(xy, 1)

  
    lmax = 6*(nMax - n) / nMax
    color = cmap(uniform(*cmR))
    alpha = 0.5*((n / nMax)**3)

    if pointed:
      lwidths = [lmax - x*lmax/pathLen for x in range(pathLen)]
      points = xy.T.reshape(-1, 1, 2)
      segments = np.concatenate([points[:-1], points[1:]], axis=1)
      lc = LC(segments, color=color, alpha=alpha, linewidths=lwidths)
      ax.add_collection(lc)
    else:
      plt.plot(xy[0], xy[1], color=color, alpha=alpha, linewidth=lmax)

  ax.autoscale(enable=True, axis="both", tight=False)
  ax.axis("off")
  set_size(fig, (pxw/dpi, pxh/dpi))
  if save:

    # imgConfig = {
    #   'pathArgs': {'a1': a1, 'a2': a2, 'af': af, 'e': e, 
    #                'cmName': cmName, 'cmR': cmR, 'pointed': pointed},
    #   'plotArgs': {'dpi': dpi, 'facecolor': facecolor, 'pxw': pxw, 'pxh': pxh},
    # }

    if not output_name:
      current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
      output_name = f'{_IMG_DIR}/{current_time}.png'
    plt.savefig(output_name, facecolor=facecolor,
                bbox_inches="tight")

  plt.show()