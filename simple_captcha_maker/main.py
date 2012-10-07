#!/usr/bin/env
# -*- coding: utf-8 -*-

try:
    import argparse
except:
    print 'You need to install argparse package.'
    sys.exit()    

from properties import Properties
from captcha import Captcha
from random_string import RandomString
from random_word import RandomWord

def main():

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--type', action="store", dest="type")
    argparser.add_argument('-n', action="store", dest="n", type=int)
    argparser.add_argument('--width', action="store", dest="width", type=int)
    argparser.add_argument('--height', action="store", dest="height", type=int)
    argparser.add_argument('--fontsize', action="store", dest="fontsize", type=int)
    argparser.add_argument('-l', action="store", dest="length", type=int)
    options = argparser.parse_args()

    if options.type == None and options.n == None and options.width == None and options.height == None and options.fontsize == None and options.length == None:
        print "No params given, i will use settings.ini"

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
            print ("word type must be random or natural")

        print ("Done, generated "+props.getNumber()+" captchas")

    #TODO: сделать возможность часть параматров брать из settings.ini а часть из консоли
    else:

        rand_word = RandomWord()
        rand_str = RandomString(options.length)
        word_type = options.type

        if word_type == "natural":
            i = 0
            while (i < int(count)):
                i = i+1
                print (rand_word.getFixedLengthWord(options.length))
                captcha=Captcha(rand_word.getFixedLengthWord(options.length, options.fontsize, options.width, options.height))
                captcha.saveImage()

        elif word_type == "random":
            i = 0
            while (i < int(count)):
                i = i+1
                print (rand_str.shuffle(options.length))
                captcha=Captcha(rand_str.shuffle(options.length, options.fontsize, options.width, options.height))
                captcha.saveImage()

        else :
            print ("word type must be random or natural")

        print ("Done, generated "+props.getNumber()+" captchas")        


if __name__ == '__main__':
    main()
