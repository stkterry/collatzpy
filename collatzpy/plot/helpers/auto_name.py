from time import localtime, strftime


def auto_name(ext:str) -> str:
  """Generates a string name using the local date/time and given ext.
  
  Return format is 'Y-m-d_H:M:S.ext'
  """
  time_str = strftime("%Y-%m-%d_%H:%M:%S", localtime())
  return f'{time_str}.{ext}'

def auto_name_with_dir(directory, ext):
  """Generates a string name using the local date/time and given dir/ext.
  
  Return format is 'directory/Y-m-d_H:M:S.ext'
  """
  time_str = strftime("%Y-%m-%d_%H:%M:%S", localtime())
  return f'{directory}/{time_str}.{ext}'
