def get_catering_list(catering_dict):

    message_list = []
    orders_for_day = []

    for day in catering_dict.values():
        date = day['date']
        orders_for_day.append(f'Catering Order Report: {date}')
        orders_for_day.append("BREAK")
        orders_for_day.append("========================")
        orders_for_day.append("BREAK")
        for order in day['pickup']:
            orders_for_day.append(order)
            orders_for_day.append("BREAK")
        for order in day['delivery']:
            orders_for_day.append(order)
            orders_for_day.append("BREAK")
        message_list.extend(orders_for_day)
        orders_for_day = []
    
    return message_list