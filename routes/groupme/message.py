import time

def message(page, chat_label, message_list):
  print('Attempting to send message on groupme...')
  page.click(f'button[aria-label="{chat_label}"]')
  for line in message_list:
    if line == 'BREAK':
      page.keyboard.press("Shift+Enter")
    else:
      page.type('div[aria-label="Start typing and press enter to send"]', line)
  page.keyboard.press('Enter')
  print("Groupme message successfully sent")