import os
import platform

from collatzpy.config import _SESSION_DIR
from collatzpy.helpers import load_json, save_to_json


def __gen_paths(paths: dict) -> None:
  """Makes directories in the locations provided by paths.

  Will skip pre-existing directories.
  """

  for _, v in paths.items():
    if not os.path.isdir(v):
      os.makedirs(v)


def __os_path() -> str:
  """Returns a path str to a default directory based on the user's OS."""

  if platform.system() == 'Windows':
    path = R'C:\Users\$USERNAME\Documents\collatzpy'
  else:
    path = '~/Documents/collatzpy'

  return os.path.expanduser(path)


def fpaths(dir: str = None, reset: bool = False) -> dict:
  """Generates default directories for user data made using this lib.

  Adds generated directories to a session.json file with the package itself.
  After first run, will use this json for all future calls to fpaths.
  Passing a dir will set the default paths to that location instead.
  Passing reset will reset to default directories.  fpaths will never
  remove any created directories or data.

  Args:
    dir: A string pointing to a user directory. Passing this arg sets
      a session.json file and future calls to this function
      will return the dir stored to that file.
    reset: Resets the session.json file to default values.
      Alternatively passing a dir arg will update the session.json.

  Returns:
    A dict of paths for convenient reference when saving files.
      paths = fpaths(dir='~/my/fav/dir')
      ...which returns,
      paths: {"root": "~/my/fav/dir",
              "imgs": "~/my/fav/dir/images",
              "pickles": "~/my/fav/dir/pickles",
              "dots": "~/my/fav/dir/dots"}
  """

  if os.path.exists(f'{_SESSION_DIR}/session.json'):
    session_dat = load_json(_SESSION_DIR, 'session.json')
  else:
    save_to_json(_SESSION_DIR, 'session.json', {})
    session_dat = {}

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

  if 'paths' not in session_dat or not paths == session_dat['paths']:
    save_to_json(_SESSION_DIR, 'session.json', {'paths': paths})

  return paths
