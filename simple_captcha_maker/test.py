# -*- coding: utf-8 -*-

import Image
import ImageDraw
import ImageFont
from os import chdir, path

font_dir = "/usr/share/fonts/truetype/msttcorefonts/"
fnt = ImageFont.truetype(font_dir +"Verdana.ttf", 62)
img = Image.new('L', (300, 100), 255)
draw = ImageDraw.Draw(img)
text_to_draw = unicode('Яндекс', 'utf-8')
draw.text((10, 10), text_to_draw, font= fnt)
del draw

img.save('image.png')