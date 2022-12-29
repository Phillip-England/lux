import time

def slack_message_route(page, message_list, channel_ids):
  print('Attempting to send slack message')

  for channel_id in channel_ids:
    page.click(f'div#{channel_id}')
    for line in message_list:
        if line == 'BREAK':
          page.keyboard.press("Shift+Enter")
        else:
          page.type('div[data-qa="message_input"]', line)
    page.keyboard.press('Enter')
    time.sleep(2)

    print('Slack messages sent')
