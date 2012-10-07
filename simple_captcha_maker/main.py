#!/usr/bin/env
# -*- coding: utf-8 -*-

import re

from properties import Properties
from captcha import Captcha
from random_string import RandomString
from random_word import RandomWord

def main():
    props = Properties("settings.ini")
    props.load()
    count = props.getNumber()

    rand_word = RandomWord()
    rand_str = RandomString(int(props.getWordLength()))
    word_type = props.getWordType()

    if word_type == "natural":
        i = 0
        while (i < int(count)):
            i = i+1
            print (rand_word.getFixedLengthWord(int(props.getWordLength())))
            captcha=Captcha(rand_word.getFixedLengthWord(int(props.getWordLength())), int(props.getFontSize()), int(props.getImageWidth()), int(props.getImageHeight()))
            captcha.saveImage()

    elif word_type == "random":
        i = 0
        while (i < int(count)):
            i = i+1
            print (rand_str.shuffle(int(props.getWordLength())))
            captcha=Captcha(rand_str.shuffle(int(props.getWordLength())), int(props.getFontSize()), int(props.getImageWidth()), int(props.getImageHeight()))
            captcha.saveImage()

    else :
        print ("random or natural")



if __name__ == '__main__':
    main()
