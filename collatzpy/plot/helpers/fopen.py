import subprocess, os, platform

def fopen(fpath):
  if platform.system() == 'Darwin':       # macOS
      subprocess.call(('open', fpath))
  elif platform.system() == 'Windows':    # Windows
      os.startfile(fpath)
  else:                                   # linux variants
      subprocess.call(('xdg-open', fpath))