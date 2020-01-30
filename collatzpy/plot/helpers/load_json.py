import json

def load_json(fpath):
  with open(fpath) as f:
    dat = json.load(f)

  return dat