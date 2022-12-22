import time

def login(page, workspace, username, password):
  page.goto('https://www.slack.com/workspace-signin')
  time.sleep(10)
