from time import localtime, strftime


def auto_name(ext):
  time_str = strftime("%Y-%m-%d_%H:%M:%S", localtime())
  return f'{time_str}.{ext}'

def auto_name_with_dir(directory, ext):
  time_str = strftime("%Y-%m-%d_%H:%M:%S", localtime())
  return f'{directory}/{time_str}.{ext}'
