import time

def login(page, login_url, username, password):
  page.goto(login_url)
  time.sleep(20)
