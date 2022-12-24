def failsafe(fn, count=0, **kwargs):
  try:
    if kwargs:
      fn(kwargs['options'])
    else:
      fn()
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