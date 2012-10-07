#!/usr/bin/env
# -*- coding: utf-8 -*-

import Image
import ImageDraw
import ImageFont
from os import chdir, path

class Captcha():
    """Класс делающий картинку с нужным текстом, размерами и шрифтом"""
    def __init__(self, Text, Font_size, ImageWidth, ImageHeight):
        self.text = unicode(Text, 'utf-8')
        self.font_size = Font_size
        self.width = ImageWidth
        self.height = ImageHeight

    # def __init__(self, text=u"", font_size=62, width=300, height=100)
	
	def setText(self, Text):
		self.text = unicode(Text, 'utf-8')

    def setFontSize(self, Font_size):
        self.font_size = Font_size

    def setWidth(self, ImageWidth):
        self.width = ImageWidth

    def setHeight(self, ImageHeight):
        self.height = ImageHeight

    def getText(self):
        return self.text

    def getFontSize(self):
        return self.font_size

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    #TODO: убрать хардкод и сделать выравнивание + подгонку размера текста
    def saveImage(self):
        font_dir = "/usr/share/fonts/truetype/msttcorefonts/"
        fnt = ImageFont.truetype(font_dir +"Verdana.ttf", self.getFontSize())
        img = Image.new('L', (self.width, self.height), 255)
        draw = ImageDraw.Draw(img)
        text_to_draw = self.text
        draw.text((5, 5), text_to_draw, font= fnt)
        img.save(self.text+'.png')
        return draw
    
	def saveImageToPath(self, Path):
		font_dir = "/usr/share/fonts/truetype/msttcorefonts/"
        fnt = ImageFont.truetype(font_dir +"Verdana.ttf", self.font_size)
        img = Image.new('L', (self.width, self.height), 255)
        draw = ImageDraw.Draw(img)
        text_to_draw = self.text
        draw.text((5, 5), text_to_draw, font= fnt)
        if Path.endswith('/'):
            img.save(Path+self.text+'.png')
        else:
            img.save(Path+'/'+self.text+'.png')
        return draw
