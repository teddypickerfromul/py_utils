#!/usr/bin/python

# -*- coding: utf-8 -*-

import urllib
import lxml.html
import time

page = urllib.urlopen("http://2ip.ru")
doc = lxml.html.document_fromstring(page.read())
ipadr = doc.xpath(".//*[@id='content']/div[1]/div/div/big/text()")
cur_time = time.strftime("%a, %d %b %Y %H:%M")
info = {cur_time : ipadr}
data = str(cur_time) + " : " + str(ipadr)
file = open("/home/teddy/ip.txt","w")
file.write(data)
file.close()



