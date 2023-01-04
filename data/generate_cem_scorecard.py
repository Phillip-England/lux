import os

from PIL import Image, ImageDraw, ImageFont

from util import format_date
from util import get_past_date

def generate_cem_scorecard(options):

  with Image.open(os.path.join(os.environ['PROJECT_PATH'], 'images', 'base', 'cem_scorecard_base.jpg')) as base_image:

    # pulling in data
    account = options['account']
    mtd_cems = options['mtd_cems']
    mtd_osat = mtd_cems['osat']
    mtd_taste = mtd_cems['taste']
    mtd_speed = mtd_cems['speed']
    mtd_ace = mtd_cems['ace']
    mtd_clean = mtd_cems['clean']
    mtd_accuracy = mtd_cems['accuracy']

    #y positions
    osat_y = 225
    ace_y = 295
    speed_y = 510
    accuracy_y = 575
    taste_y = 809
    clean_y = 879


    # settings cords based off length of scores

    # osat cords
    if len(mtd_osat) == 3: osat_x = 1183
    else: osat_x = 1170

    # ace cords
    if len(mtd_ace) == 3: ace_x = 1183
    else: ace_x = 1170

    # speed cords
    if len(mtd_speed) == 3: speed_x = 1183
    else: speed_x = 1170

    # accuracy cords
    if len(mtd_accuracy) == 3: accuracy_x = 1183
    else: accuracy_x = 1170

    # taste cords
    if len(mtd_taste) == 3: taste_x = 1183
    else: taste_x = 1175

    # clean cords
    if len(mtd_clean) == 3: clean_x = 1185
    else: clean_x = 1175

    # updated date cords
    date_y = 770
    # possible lengths are 17, 18, and 19
    todays_date = f'Updated: {format_date(get_past_date(0))}'
    if len(todays_date) == 17: date_x = 253
    if len(todays_date) == 18: date_x = 240
    if len(todays_date) == 19: date_x = 227


    # pasting the scorecard base onto the new image
    new_image = Image.new(mode=base_image.mode, size=base_image.size)
    new_image.paste(base_image)

    # creating draw object
    draw = ImageDraw.Draw(new_image)

    # selecting correct font
    font = ImageFont.truetype(os.path.join(os.environ['PROJECT_PATH'], 'fonts', 'Lato', 'Lato-Regular.ttf'), 32)

    # drawing osat
    draw.text((osat_x, osat_y), f'{mtd_osat}', font=font, fill=(0, 0, 0))

    # drawing ace
    draw.text((ace_x, ace_y), f'{mtd_ace}', font=font, fill=(0, 0, 0))

    # drawing speed
    draw.text((speed_x, speed_y), f'{mtd_speed}', font=font, fill=(0, 0, 0))

    # drawing accuracy
    draw.text((accuracy_x, accuracy_y), f'{mtd_accuracy}', font=font, fill=(0, 0, 0))

    # drawing taste
    draw.text((taste_x, taste_y), f'{mtd_taste}', font=font, fill=(0, 0, 0))

    # drawing clean
    draw.text((clean_x, clean_y), f'{mtd_clean}', font=font, fill=(0, 0, 0))

    # drawing date
    draw.text((date_x, date_y), f'{todays_date}', font=font, fill=(0, 0, 0))

    new_image.save(os.path.join(os.environ['PROJECT_PATH'], 'images', 'cfa', f'{account}', 'cem_scorecard.jpg'))
