import os, platform

from collatzpy.config import _SESSION_DIR
from collatzpy.helpers import load_json, save_to_json

def __gen_paths(paths):
    for _, v in paths.items(): 
      if not os.path.isdir(v): os.makedirs(v)

def __create_session():
  save_to_json(_SESSION_DIR, 'session.json', {})

def fpaths(dir=None, reset=False):
  session_dat = load_json(_SESSION_DIR, 'session.json')

  if not session_dat:
    __create_session()

  if session_dat and reset:
    try:
      del session_dat['paths']
    except KeyError:
      print("Key 'paths' not found")

  if 'paths' in session_dat and not dir:
    paths = session_dat['paths']
    __gen_paths(paths)
    return paths


  if dir:
    root_path = dir
  else:
    if platform.system() == 'Windows':
      path = R'C:\Users\$USERNAME\Documents\collatzpy'
    else:
      path = '~/Documents/collatzpy'
    root_path = os.path.expanduser(path)

  paths = {'root': root_path,
          'imgs': f'{root_path}/images',
          'pickles': f'{root_path}/pickles',
          'dots': f'{root_path}/dots'}

  __gen_paths(paths)

  if 'paths' in session_dat and not paths == session_dat['paths']:
    save_to_json( _SESSION_DIR, 'session.json', {'paths': paths})

  return paths