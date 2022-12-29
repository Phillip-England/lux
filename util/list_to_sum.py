def list_to_sum(list, is_float, round_to):

  total = 0

  for item in list:
    if is_float:
      total = total + float(item)
    else:
      total = total + int(item)

  if round_to == 0:
    return total
  else:
    return round(total, round_to)