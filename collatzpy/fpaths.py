import os, platform

from collatzpy.config import _SESSION_DIR
from collatzpy.helpers import load_json, save_to_json

def __gen_paths(paths):
    for _, v in paths.items(): 
      if not os.path.isdir(v): os.makedirs(v)


def __os_path():
  if platform.system() == 'Windows':
    path = R'C:\Users\$USERNAME\Documents\collatzpy'
  else:
    path = '~/Documents/collatzpy'
    
  return os.path.expanduser(path)

def fpaths(dir=None, reset=False):
  session_dat = load_json(_SESSION_DIR, 'session.json')

  if not session_dat:
    save_to_json(_SESSION_DIR, 'session.json', {})

  if reset:
    try:
      del session_dat['paths']
    except KeyError:
      print("Key 'paths' not found")

  if 'paths' in session_dat and not dir:
    paths = session_dat['paths']
    __gen_paths(paths)
    return paths

  root_path = dir or __os_path()

  paths = {'root': root_path,
          'imgs': f'{root_path}/images',
          'pickles': f'{root_path}/pickles',
          'dots': f'{root_path}/dots'}

  __gen_paths(paths)

  if not 'paths' in session_dat or not paths == session_dat['paths']:
    save_to_json( _SESSION_DIR, 'session.json', {'paths': paths})

  return paths
