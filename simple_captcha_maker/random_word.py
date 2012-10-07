#!/usr/bin/env 
# -*- coding: utf-8 -*-

import urllib2
import simplejson
import time, re

class RandomWord():
	def __init__(self):
		self.url="http://randomword.setgetgo.com/get.php"
		self.json = urllib2.urlopen(self.url).read()

	def getWord(self):
		time.sleep(1)
		self.url="http://randomword.setgetgo.com/get.php"
		self.json = urllib2.urlopen(self.url).read()
		return self.json	
	
	def getFixedLengthWord(self, length):
		self.url="http://randomword.setgetgo.com/get.php"
		self.json = urllib2.urlopen(self.url).read()		
		while(len(self.json)> length) :
			self.json = urllib2.urlopen(self.url).read()
		
		return re.sub('[^A-Za-z0-9]+', '', self.json)
			
					