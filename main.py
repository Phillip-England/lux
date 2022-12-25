import os
import sys

from dotenv import load_dotenv
load_dotenv()

from projects import work

if __name__ == '__main__':

  try: 
    if sys.argv[3] == '-h': headless = True
  except: 
    headless = False  

  if sys.argv[1] == "catering":
    work.message.catering({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'cems':
    work.message.cems({
      'headless': headless,
      'account': sys.argv[2]
    })









