import time

def message_groupme(page, chat_labels, message_list):
  print('Attempting to send message on groupme...')
  for label in chat_labels:
    page.click(f'button[aria-label="{label}"]')
    for line in message_list:
      if line == 'BREAK':
        page.keyboard.press("Shift+Enter")
      else:
        page.type('div[aria-label="Start typing and press enter to send"]', line)
    page.keyboard.press('Enter')
    page.click('button[ng-click="closeChat()"]')
  print("Groupme message successfully sent")