#!/usr/bin/env
# -*- coding: utf-8 -*-

import random

class RandomString():
    """Просто делаем строчку из случайных символов"""
    def __init__(self, Length):
        self.word = ''
        for i in range(Length):
            self.word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

    def getWord(self):
        return self.word

    def shuffle(self, Length):
        self.word = ''
        for i in range(Length):
            self.word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        return self.word
