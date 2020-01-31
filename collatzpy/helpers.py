import json
import os

def load_json(fpath, fname):
  if os.path.exists(f'{fpath}/{fname}'):
    with open(f'{fpath}/{fname}') as f:
      dat = json.load(f)
  else:
    return None

  return dat


# def create_json(fpath, fname):
#   with open(f'{fpath}/{fname}', 'w') as f:
#     json.dump('', f, ensure_ascii=False)

def save_to_json(fpath, fname, data):
  with open(f'{fpath}/{fname}', 'w') as f:
    json.dump(data, f)
