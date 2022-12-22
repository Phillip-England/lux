import time

def login(page, username, password, chat_label):
  print('Attempting to login at groupme..')
  page.goto('https://web.groupme.com/signin')
  page.wait_for_selector('input#signinUserNameInput')
  page.type('input#signinUserNameInput', username)
  page.type('input#signinPasswordInput', password)
  page.keyboard.press('Enter')
  page.wait_for_selector(f'button[aria-label="{chat_label}"]')
  print("Login at groupme successful")
  return page