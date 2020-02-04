import json
import os


def load_json(fpath: str, fname: str) -> dict:
  """Returns the data from a json located in fpath/fname"""

  if os.path.exists(f'{fpath}/{fname}'):
    with open(f'{fpath}/{fname}') as f:
      dat = json.load(f)
  else:
    return None

  return dat


def save_to_json(fpath: str, fname: str, data: dict) -> None:
  """Saves data to a json located at fpath/fname"""
  with open(f'{fpath}/{fname}', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)