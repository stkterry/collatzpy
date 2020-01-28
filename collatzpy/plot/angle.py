from matplotlib import pyplot as plt, cm
from matplotlib.collections import LineCollection as LC
from math import sin, cos
import numpy as np
import random
rand_uni = random.uniform

from .size_fix import set_size


def angle_plot(tree, selection, a1=0.3, a2=0.38, af=1.08,
               e=1.3, cmName='plasma_r', cmR=(0, 1),
               save=False, dpi=100, facecolor='black',
               output_name='output.png', pxw=2560, pxh=1200):

  cmap = cm.get_cmap(cmName)
  nMax = max(selection)

  fig, ax = plt.subplots(1, 1)
  fig.patch.set_facecolor(facecolor)
  plt.gca().set_position([0.025, 0.025, 0.95, 0.95])

  for n in selection:
    path = tree.path(n)
    path.reverse()
    pathLen = len(path)

    x, y = [0]*(pathLen + 1), [0]*(pathLen + 1)
    theta = 0
    for i, k in enumerate(path):
      rho = k / (1 + k**e)
      theta += a1 * (a2 - af*(k % 2))
      x[i+1] = rho * cos(theta) + x[i]
      y[i+1] = rho * sin(theta) + y[i]

    lmax = 6*(nMax - n) / nMax
    lwidths = [lmax - x*lmax/pathLen for x in range(pathLen)]
    color = cmap(rand_uni(cmR[0], cmR[1]))
    alpha = 0.5*((n / nMax)**3)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LC(segments, color=color, alpha=alpha, linewidths=lwidths)
    ax.add_collection(lc)



  ax.autoscale(enable=True, axis="both", tight=False)
  ax.axis("off")
  set_size(fig, (pxw/dpi, pxh/dpi))
  if save:
    plt.savefig(output_name, facecolor=facecolor,
                bbox_inches="tight")
  plt.show()



def angle_plot_f(tree, selection, a1=0.3, a2=0.38, af=1.08,
               e=1.3, cmName='plasma_r', cmR=(0, 1), 
               save=False, dpi=100, facecolor='black',
               output_name='output.png', pxw=2560, pxh=1200):

  cmap = cm.get_cmap(cmName)
  nMax = max(selection)

  # dpi = 256
  # mfac = 2
  fig, ax = plt.subplots(1, 1)
  fig.set_size_inches(pxw/dpi, pxh/dpi)
  fig.patch.set_facecolor('black')

  for n in selection:
    path = tree.path(n)
    path.reverse()
    pathLen = len(path)

    x, y = [0]*(pathLen + 1), [0]*(pathLen + 1)
    theta = 0
    for i, k in enumerate(path):
      rho = k / (1 + k**e)
      theta += a1 * (a2 - af*(k % 2))
      x[i+1] = rho * cos(theta) + x[i]
      y[i+1] = rho * sin(theta) + y[i]

    lmax = 8*(nMax - n) / nMax
    color = cmap(rand_uni(cmR[0], cmR[1]))
    alpha = 0.5*((n / nMax)**3)

    plt.plot(x, y, color = color, alpha = alpha, linewidth=lmax)

  # ax.autoscale(enable=True, axis="both", tight=True)
  ax.axis("off")
  set_size(fig, (pxw/dpi, pxh/dpi))
  if save:
    plt.savefig(output_name, dpi=dpi, facecolor=facecolor,
                bbox_inches="tight", pad_inches=0)
  plt.show()
