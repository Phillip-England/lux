import time

def groupme_message_route(page, chat_labels, message_list):
  print('Attempting to send message on groupme...')
  for label in chat_labels:
    page.click(f'input[placeholder="Find chats"]')
    page.keyboard.type(label.lower())
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Enter')
    for line in message_list:
      if line == 'BREAK':
        page.keyboard.press("Shift+Enter")
      else:
        page.type('div[aria-label="Start typing and press enter to send"]', line)
    page.keyboard.press('Enter')
    time.sleep(2)
    page.click('button[ng-click="closeChat()"]')
  print("Groupme message successfully sent")