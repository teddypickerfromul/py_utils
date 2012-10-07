#!/usr/bin/env
# -*- coding: utf-8 -*-

from ConfigParser import SafeConfigParser


class Properties:
        """Класс делающий картинку с нужным т"""
        def __init__(self, fname):
                self.filename = fname
                self.cfgParser = SafeConfigParser()

        def load(self):
                self.cfgParser.read(self.filename)

        def getNumber(self):
                return self.cfgParser.get('default', 'number')

        def getImageWidth(self):
                return self.cfgParser.get('default', 'width')

        def getImageHeight(self):
                return self.cfgParser.get('default', 'height')

        def getFontSize(self):
                return self.cfgParser.get('default', 'font_size')

        def getWordLength(self):
                return self.cfgParser.get('default', 'word_length')

        def getWordType(self):
                return self.cfgParser.get('default', 'word_type')                