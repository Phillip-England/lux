from util import contains_substring

def extract_time_punch(pdf_text):

  employees_in_report = []
  astrick_positions = []
  employee_total_positions = []
  employees_with_astricks = []

  for i in range(len(pdf_text)):
    if pdf_text[i] == '*' and pdf_text[i+1] != '-':
      astrick_positions.append(i)

  for position in astrick_positions:
    day = pdf_text[position+1]
    date = pdf_text[position+2]
    while True:
      if pdf_text[position] == 'Totals' and pdf_text[position-1] == 'Employee':
        employee_total_positions.append({
          'position': position, 
          'day': day, 
          'date': date
        })
        break
      position = position - 1
  
  # print(astrick_positions)
  # print(employee_total_positions)

  for dict in employee_total_positions:
    position = dict['position']
    day = dict['day']
    date = dict['date']
    while True:
      if contains_substring(pdf_text[position], ','):
        employees_with_astricks.append({
          'first_name': pdf_text[position],
          'last_name': pdf_text[position+1],
          'day': day,
          'date': date,
        })
        break
      else:
        position += 1
  
  message = ''
  for time_detail in employees_with_astricks:
    first_name = time_detail['first_name']
    last_name = time_detail['last_name']
    day = time_detail['day']
    date = time_detail['date']
    message = message + f'{first_name} {last_name} | {day} {date}\n'

  return message