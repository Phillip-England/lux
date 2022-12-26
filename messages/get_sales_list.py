def get_sales_list(sales_dict):

  message_list = []

  for business_day in sales_dict.values():
    day = business_day['day']
    date = business_day['date']
    breakfast_sales = business_day['breakfast_sales']
    lunch_sales = business_day['lunch_sales']
    midshift_sales = business_day['midshift_sales']
    dinner_sales = business_day['dinner_sales']
    total_sales = business_day['total_sales']
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
