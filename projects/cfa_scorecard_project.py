import os

from PIL import Image, ImageDraw, ImageFont

from util import failsafe
from util import format_date
from util import get_past_date
from util import get_current_month
from data import generate_cem_scorecard

def cfa_scorecard_project(options):
  
  headless = options['headless']
  account = options['account']

  generate_cem_scorecard({
    'account': account
  })



 