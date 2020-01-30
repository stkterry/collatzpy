from time import localtime, strftime


def auto_name(directory, ext):
  time_str = strftime("%Y-%m-%d_%H:%M:%S", localtime())
  return f'{directory}/{time_str}.{ext}'