def extract_catering_orders(pdf_data):

  destination_step = 1
  order_time_step = 5
  order_am_or_pm_step = 6
  dollor_sign_count_test = 0
  dollar_sign_count_real = 0
  delivery_orders = []
  pickup_orders = []
  date = f'{pdf_data[9]} {pdf_data[10]} {pdf_data[11]}'

  for i in range(len(pdf_data)):
    
    if pdf_data[i][0] == '$':
        dollor_sign_count_test += 1

  for i in range(len(pdf_data)):

    if pdf_data[i][0] == '$':
        dollar_sign_count_real += 1
        if dollar_sign_count_real != dollor_sign_count_test:
            cost = pdf_data[i]
            destination = pdf_data[i+destination_step]
            time = f'{pdf_data[i+order_time_step]}{pdf_data[i+order_am_or_pm_step]}'


            if destination == 'DELIVERY':
                delivery_orders.append(f'{destination} {time} {cost}')

            if destination == 'PICKUP':
                pickup_orders.append(f'{destination} {time} {cost}')
  
  return {
    'pickup': pickup_orders,
    'delivery': delivery_orders,
    'date': date
  }
      
      