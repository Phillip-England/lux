import os
import sys

from dotenv import load_dotenv
load_dotenv()

from projects import work

if __name__ == '__main__':

  if sys.argv[1] == "catering":
    work.message.catering()

  if sys.argv[1] == 'cems':
    work.message.cems()









