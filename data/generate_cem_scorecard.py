import os

from PIL import Image, ImageDraw, ImageFont

from util import format_date
from util import get_past_date

def generate_cem_scorecard(options):

  with Image.open(os.path.join(os.environ['PROJECT_PATH'], 'images', 'cfa', 'test', 'cem_scorecard_base.jpg')) as base_image:

    # pulling in data
    mtd_cems = options['mtd_cems']
    mtd_osat = mtd_cems['osat']
    mtd_taste = mtd_cems['taste']
    mtd_speed = mtd_cems['speed']
    mtd_ace = mtd_cems['ace']
    mtd_clean = mtd_cems['clean']
    mtd_accuracy = mtd_cems['accuracy']

    # score x position
    score_x_position = 1170

    #y positions
    osat_y = 225

    mtd_osat = '100%'
    if len(mtd_osat) == 3:
      osat_x = 1185
    else:
      osat_x = 1170

    # pasting the scorecard base onto the new image
    new_image = Image.new(mode=base_image.mode, size=base_image.size)
    new_image.paste(base_image)

    # creating draw object
    draw = ImageDraw.Draw(new_image)

    # selecting correct font
    font = ImageFont.truetype(os.path.join(os.environ['PROJECT_PATH'], 'fonts', 'Lato', 'Lato-Regular.ttf'), 32)

    # drawing osat
    draw.text((osat_x, osat_y), f'{mtd_osat}', font=font, fill=(0, 0, 0))
    # draw.text((score_x_position, 295), f'99%', font=font, fill=(0, 0, 0))



    new_image.save(os.path.join(os.environ['PROJECT_PATH'], 'images', 'cfa', 'test', 'cem_scorecard.jpg'))
