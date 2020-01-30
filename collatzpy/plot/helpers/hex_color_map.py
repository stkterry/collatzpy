from matplotlib import cm
from math import floor

class HexColorMap():
  def __init__(self, cmap, size=1024, as_int=False):
    self.cm_name = cmap
    self.__cm = {0: None}
    self.__size = size - 1
    self.__convert_cmap_to_rgba(cm.get_cmap(cmap))

  def __convert_cmap_to_rgba(self, cmap):
    for i in range(0, self.__size + 1):
      rgba = (floor(x*255) for x in cmap(i/self.__size))
      self.__cm[i] = "#{:02x}{:02x}{:02x}{:02x}".format(*rgba)

  def __call__(self, val):
    idx = floor(val * self.__size)
    if idx in self.__cm:
      return self.__cm[idx]
    else:
      raise AttributeError(
        "Input value must be (0 -> 1), inclusive." 
        + f'Value given: {val}'
      )

