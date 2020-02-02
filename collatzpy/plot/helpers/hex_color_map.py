from matplotlib import cm
from math import floor

class HexColorMap(dict):
  """Takes normalized values and returns hex string conversion in colorspace.
  
  Accepts any recognized matplotlib.cm colormap as a string and 
  returns a callable class that returns hex equivalent color 
  values as strings.
  """

  def __init__(self, cmap:str, size:int=1024):
    self.cm_name = cmap
    self.__size = size - 1
    self.__convert_cmap_to_rgba(cm.get_cmap(cmap))

  def __convert_cmap_to_rgba(self, cmap:str):
    for i in range(0, self.__size + 1):
      rgba = (floor(x*255) for x in cmap(i/self.__size))
      self[i] = "#{:02x}{:02x}{:02x}{:02x}".format(*rgba)

  def __call__(self, val):
    idx = floor(val * self.__size)
    if idx in self:
      return self[idx]
    else:
      raise AttributeError(
        "Input value must be (0 -> 1), inclusive." 
        + f'Value given: {val}'
      )

