def get_sales_list(sales_dict):

  message_list = []

  day = sales_dict['day']
  date = sales_dict['date']
  breakfast_sales = sales_dict['breakfast_sales']
  lunch_sales = sales_dict['lunch_sales']
  midshift_sales = sales_dict['midshift_sales']
  dinner_sales = sales_dict['dinner_sales']
  total_sales = sales_dict['total_sales']
  message_list.append(f'{day}, {date}')
  message_list.append('BREAK')
  message_list.append("========================")
  message_list.append('BREAK')
  message_list.append(f'Breakfast Sales: {breakfast_sales}')
  message_list.append('BREAK')
  message_list.append(f'Lunch Sales: {lunch_sales}')
  message_list.append('BREAK')
  message_list.append(f'Midshift Sales: {midshift_sales}')
  message_list.append('BREAK')
  message_list.append(f'Dinner Sales: {dinner_sales}')
  message_list.append('BREAK')
  message_list.append(f'Total Sales: {total_sales}')


  return message_list
