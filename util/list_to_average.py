def list_to_average(list):

  number_of_items = len(list)
  total = 0

  for item in list:
    total = total + float(item)

  average = total / number_of_items
  return round(average, 2)
  