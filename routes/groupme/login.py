import time

def login(page, username, password):
  print('Attempting to login at groupme..')
  page.goto('https://web.groupme.com/signin')
  page.wait_for_selector('input#signinUserNameInput')
  page.type('input#signinUserNameInput', username)
  page.type('input#signinPasswordInput', password)
  page.keyboard.press('Enter')

  # if it your first time loggin on with a new browser, you will need to use a pin
  # the code below helps you submit your pin.
  pin_popup = page.query_selector('div.modal-content')

  if pin_popup == None:
    print('Pin not required')
  else:
    print('Pin required')
    pin = input("What is the pin: ")
    page.type('input[ng-model="enteredPIN"]', pin)
    page.keyboard.press('Enter')

  page.wait_for_selector(f'button[aria-label="Start a new chat"]')
  print("Login at groupme successful")
  return page