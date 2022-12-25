import os
import sys

from dotenv import load_dotenv
load_dotenv()

from projects import cfa_catering_message_project
from projects import cfa_cem_message_project

if __name__ == '__main__':

  try: 
    if sys.argv[3] == '-h': headless = True
  except: 
    headless = False  

  if sys.argv[1] == "catering":
    cfa_catering_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'cems':
    cfa_cem_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })









