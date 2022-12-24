import time

def login_servicepoint(page, pin):
  print("Attempting to login to service point..")
  page.goto('https://www.cfahome.com/go/appurl.go?app=RSMW')
  page.wait_for_selector('input#MainContent_txtEchoWindow')
  page.type('input#MainContent_txtEchoWindow', pin)
  page.click('input#MainContent_btnEnter')
  page.wait_for_selector('div#btnMakeFavorite')
  print('Service point login successful')
  return page