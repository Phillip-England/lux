def failsafe(fn, count=0, **kwargs):
  try:
    if kwargs:
      return_value = fn(kwargs['options'])
      return return_value
    else:
      return_value = fn()
      return return_value
  except Exception as e:
    print(e)
    if count < 5:
      if kwargs:
        failsafe(fn, count+1, options=kwargs['options'])
      else:
        failsafe(fn, count+1)
    else:
      print(e)
      raise e