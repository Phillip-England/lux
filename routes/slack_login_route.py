import time

def slack_login_route(page, login_url, username, password):
  print("Attempting to login to slack..")
  page.goto(login_url)
  page.type('input[data-qa="login_email"]', username)
  page.type('input[data-qa="login_password"]', password)
  page.click('button[data-qa="signin_button"]')
  page.wait_for_selector('div#c-coachmark-anchor')
  print('Slack login successful')
  return page
