import time

def login_groupme(page, username, password):
  print('Attempting to login at groupme..')
  page.goto('https://web.groupme.com/signin')
  page.wait_for_selector('input#signinUserNameInput')
  page.type('input#signinUserNameInput', username)
  page.type('input#signinPasswordInput', password)
  page.keyboard.press('Enter')

  # each time you use a new browser you will need to confirm a pin from your phone
  # the below try:except waits for a popup
  # if it finds it, you have the change to submit your pin
  # only happens on first time you use a new browser

  try:
    print("Waiting for popup pin..")
    pin_popup = page.wait_for_selector('div.modal-content', timeout=10000)
    print('Pin popup is active')
    pin = input("What is the pin: ")
    page.type('input[ng-model="enteredPIN"]', pin)
    page.keyboard.press('Enter')
  except:
    print('Pin popup not found')


  page.wait_for_selector(f'button[aria-label="Start a new chat"]')
  print("Login at groupme successful")
  return page