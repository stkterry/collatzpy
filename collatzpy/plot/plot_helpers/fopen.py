import subprocess, os, platform

def fopen(fpath):
  if platform.system() == 'Darwin':       # macOS
      subprocess.Popen(('open', fpath))
  elif platform.system() == 'Windows':    # Windows
      os.startfile(fpath)
  else:                                   # linux variants
      subprocess.Popen(('xdg-open', fpath))
