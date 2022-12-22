def catering_message_list(catering_dict):

    message_list = [
        'Catering Order Report',
    ]

    orders_for_day = []
    for day in catering_dict.values():
        orders_for_day.append("BREAK")
        orders_for_day.append("BREAK")
        orders_for_day.append("========================")
        orders_for_day.append("BREAK")
        orders_for_day.append(day['date'])
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