
import time

import pyautogui


def signpresenter_update_message_route(page, options):
  
  message = options['message']
  submessage = options['submessage']
  file_path = options['file_path']
  
  print(f'Attempting to update message {message} and submessage {submessage}')
  wallboard_button = page.get_by_text(message)
  wallboard_button.click()
  cem_current_month_button = page.get_by_text(submessage)
  cem_current_month_button.click()
  page.wait_for_selector('img[alt="thumbnail"]')
  page.click('img[alt="thumbnail"]')
  page.click('button[class="btn btn-info btn-sm"]')
  time.sleep(10)
  pyautogui.typewrite(file_path, interval=0.1)
  pyautogui.press('Enter')
  time.sleep(10)
  update_button = page.get_by_role('button', name='Update')
  update_button.click()
  time.sleep(10)
  save_button = page.get_by_text('Save')
  save_button.click()
  time.sleep(10)
  print(f'Updated Message {message} and submessage {submessage}')
  return page