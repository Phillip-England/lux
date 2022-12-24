def login_cfahome(page, username, password):
  print("Attempting to login at cfahome.com..")
  page.goto('https://www.cfahome.com')
  page.wait_for_load_state('load')
  page.type('#okta-signin-username', username)
  page.click('#okta-signin-submit')
  page.wait_for_load_state('load')
  page.type("#input59", password)
  page.click("input.button.button-primary[type='submit'][value='Verify'][data-type='save']")
  page.wait_for_selector('div.chik-header')
  print('Login at cfahome.com successful')
  return page