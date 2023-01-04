

def signpresenter_select_account_route(page, account_name):
  print(f'Attempting to select account {account_name}..')
  page.click('i.fa-caret-down')
  account_button = page.locator("#userAccounts").get_by_role("link", name=" Chick-fil-A at Southroads")
  account_button.click()
  page.click('a#mainNavMessages')
  page.wait_for_selector('div#messagesSidebar')
  print(f'Account {account_name} selected')
  return page