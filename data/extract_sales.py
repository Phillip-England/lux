def extract_sales(pdf_data):

  results = {
    'date': '',
    'day': '',
    'breakfast_sales': '',
    'breakfast_transactions': '',
    'breakfast_check_average': '',
    'lunch_sales': '',
    'lunch_transactions': '',
    'lunch_check_average': '',
    'midshift_sales': '',
    'midshift_transactions': '',
    'midshift_check_average': '',
    'dinner_sales': '',
    'dinner_transactions': '',
    'dinner_check_average': '',
    'total_sales': '',
    'total_transactions': '',
    'total_check_average': '',
    'carryout_transactions': '',
    'carryout_sales': '',
    'carryout_check_average': '',
    'cfa_delivery_transactions': '',
    'cfa_delivery_sales': '',
    'cfa_delivery_check_average': '',
    'delivery_transactions': '',
    'delivery_sales': '',
    'delivery_check_average': '',
    'dine_in_transactions': '',
    'dine_in_sales': '',
    'dine_in_check_average': '',
    'drive_thru_transactions': '',
    'drive_thru_sales': '',
    'drive_thru_check_average': '',
    'm_carryout_transactions': '',
    'm_carryout_sales': '',
    'm_carryout_check_average': '',
    'm_dine_in_transactions': '',
    'm_dine_in_sales': '',
    'm_dine_in_check_average': '',
    'm_drive_thru_transactions': '',
    'm_drive_thru_sales': '',
    'm_drive_thru_check_average': '',
    'on_demand_transactions': '',
    'on_demand_sales': '',
    'on_demand_check_average': '',
    'pickup_transactions': '',
    'pickup_sales': '',
    'pickup_check_average': '',
    'curbside_transactions': '',
    'curbside_sales': '',
    'curbside_check_average': '',
  }

  # date indicators
  date_indicator = 'Time:From'
  day_of_week_steps = 1
  month_steps = 2
  day_steps = 3
  year_steps = 4

  # breakfast indicators
  breakfast_indicator = 'Breakfast'
  breakfast_sales_steps = 4
  breakfast_transaction_steps = 6
  breakfast_check_average_steps = 5

  # lunch indicators
  lunch_indicator = 'Lunch'
  lunch_sales_steps = 4
  lunch_transaction_steps = 3
  lunch_check_average_steps = 5

  # midshift indicators
  midshift_indicator = 'Afternoon'
  midshift_sales_steps = 4
  midshift_transaction_steps = 3
  midshift_check_average_steps = 5

  # dinner indicators
  dinner_indicator = 'Dinner'
  dinner_sales_steps = 4
  dinner_transaction_steps = 3
  dinner_check_average_steps = 5

  # total indicators
  total_indicator = 'Totals:'
  total_sales_steps = 2
  total_transaction_steps = 1
  total_check_average_steps = 3

  # daypart indicators
  final_section_trigger = False
  
  for i in range(len(pdf_data)):

    # pdf_data about the date
    if pdf_data[i] == date_indicator:
        day_of_week_untrimmed = pdf_data[i+day_of_week_steps]
        day_of_week = day_of_week_untrimmed.rstrip(day_of_week_untrimmed[-1])
        business_month = pdf_data[i+month_steps]
        business_day = pdf_data[i+day_steps]
        business_year = pdf_data[i+year_steps]
        results['date'] = f'{business_month} {business_day} {business_year}'
        results['day'] = day_of_week

    #breakfast sales pdf_data
    if pdf_data[i] == breakfast_indicator:
        results['breakfast_sales'] = pdf_data[i + breakfast_sales_steps]
        results['breakfast_transactions'] = pdf_data[i + breakfast_transaction_steps]
        results['breakfast_check_average'] = pdf_data[i + breakfast_check_average_steps]

    #lunch sales pdf_data
    if pdf_data[i] == lunch_indicator:
        results['lunch_sales'] = pdf_data[i + lunch_sales_steps]
        results['lunch_transactions'] = pdf_data[i + lunch_transaction_steps]
        results['lunch_check_average'] = pdf_data[i + lunch_check_average_steps]

    #midshift sales pdf_data
    if pdf_data[i] == midshift_indicator:
        results['midshift_sales'] = pdf_data[i + midshift_sales_steps]
        results['midshift_transactions'] = pdf_data[i + midshift_transaction_steps]
        results['midshift_check_average'] = pdf_data[i + midshift_check_average_steps]

    #dinner sales pdf_data
    if pdf_data[i] == dinner_indicator:
        results['dinner_sales'] = pdf_data[i + dinner_sales_steps]
        results['dinner_transactions'] = pdf_data[i + dinner_transaction_steps]
        results['dinner_check_average'] = pdf_data[i + dinner_check_average_steps]

    #daily totals
    if pdf_data[i] == total_indicator and pdf_data[i-1] == 'Report':
        final_section_trigger = True
        results['total_sales'] = pdf_data[i + total_sales_steps]
        results['total_transactions'] = pdf_data[i + total_transaction_steps]
        results['total_check_average'] = pdf_data[i + total_check_average_steps]

    # carryout
    if pdf_data[i] == 'CARRY' and pdf_data[i+1] == 'OUT' and final_section_trigger == True:
      results['carryout_transactions'] = pdf_data[i+2]
      results['carryout_sales'] = pdf_data[i+4]
      results['carryout_check_average'] = pdf_data[i+3]

    # cfa delivery
    if pdf_data[i] == 'CFA' and pdf_data[i+1] == 'DELIVERY' and final_section_trigger == True:
      results['cfa_delivery_transactions'] = pdf_data[i+2]
      results['cfa_delivery_sales'] = pdf_data[i+4]
      results['cfa_delivery_check_average'] = pdf_data[i+3]

    # delivery
    if pdf_data[i] == 'DELIVERY' and final_section_trigger == True:
      results['delivery_transactions'] = pdf_data[i+1]
      results['delivery_sales'] = pdf_data[i+3]
      results['delivery_check_average'] = pdf_data[i+2]

    # dine in
    if pdf_data[i] == 'DINE' and pdf_data[i+1] == 'IN' and final_section_trigger == True:
      results['dine_in_transactions'] = pdf_data[i+2]
      results['dine_in_sales'] = pdf_data[i+4]
      results['dine_in_check_average'] = pdf_data[i+3]

    # drive thru
    if pdf_data[i] == 'DRIVE' and pdf_data[i+1] == 'THRU' and final_section_trigger == True:
      results['drive_thru_transactions'] = pdf_data[i+2]
      results['drive_thru_sales'] = pdf_data[i+4]
      results['drive_thru_check_average'] = pdf_data[i+3]

    # mobile carryout
    if pdf_data[i] == 'M-CARRYOUT' and final_section_trigger == True:
      results['m_carryout_transactions'] = pdf_data[i+1]
      results['m_carryout_sales'] = pdf_data[i+3]
      results['m_carryout_check_average'] = pdf_data[i+2]

    # mobile dine in
    if pdf_data[i] == 'M-DINEIN' and final_section_trigger == True:
      results['m_dine_in_transactions'] = pdf_data[i+1]
      results['m_dine_in_sales'] = pdf_data[i+3]
      results['m_dine_in_check_average'] = pdf_data[i+2]
      

    # mobile drive thru
    if pdf_data[i] == 'M-DRIVE-THRU' and final_section_trigger == True:
      results['m_drive_thru_transactions'] = pdf_data[i+1]
      # dt sales attaches weird info to it, we have to split it off
      results['m_drive_thru_sales'] = pdf_data[i+3].replace('Daypart/DestinationTransaction', '')
      results['m_drive_thru_check_average'] = pdf_data[i+2]

    # on demand
    if pdf_data[i] == 'DEMAND' and final_section_trigger == True:
      results['on_demand_transactions'] = pdf_data[i+1]
      results['on_demand_sales'] = pdf_data[i+3]
      results['on_demand_check_average'] = pdf_data[i+2]

    # pickup
    if pdf_data[i] == 'PICKUP' and final_section_trigger == True:
      results['pickup_transactions'] = pdf_data[i+1]
      results['pickup_sales'] = pdf_data[i+3]
      results['pickup_check_average'] = pdf_data[i+2]

    # pickup
    if pdf_data[i] == 'CURBSIDE' and final_section_trigger == True:
      results['curbside_transactions'] = pdf_data[i+1]
      results['curbside_sales'] = pdf_data[i+3]
      results['curbside_check_average'] = pdf_data[i+2]

  return results