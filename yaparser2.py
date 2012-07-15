#!/usr/bin/python3

# -*- coding: utf-8 -*-

import urllib.request,glob,os
import lxml.html
import datetime
import time

start_pid = 6120686
end_pid = 6120699
max_score = 5
its_magick = 9
url_list = []

def currentTime():
	tmp = str(datetime.datetime.now())
	return tmp[0:tmp.find(" ")]

def getLinks():
	url_base = open("./url_base.txt","w+")
	link_files = glob.glob("./links*.html")
	for link_file in link_files:
		filename = os.path.basename(link_file)
		#print (filename)
		f = open(filename,"r")
		html = f.read()
		glob_left_index = html.find("<div class=\"page__b-offers__guru\">")+35
		#print (html[glob_left_index:glob_left_index+15])
		glob_right_index = html.find("<div class=\"b-offers b-offers_type_guru\">",glob_left_index)
		cursor = html.find("class=\"b-offers b-offers_type_guru\"",glob_left_index,glob_right_index)
		#print (html[cursor+39:cursor+47])
		cursor = cursor+10

		while (cursor < glob_right_index) and (cursor != its_magick):
			cursor = html.find("class=\"b-offers b-offers_type_guru\"",cursor,glob_right_index)
			#print ("Еще :")
			pid = (html[cursor+39:cursor+47])
			pid = pid.replace("\"","")
			#print ("http://market.yandex.ru/model.xml?hid=90578&modelid="+pid)
			cursor = cursor+10
			url_list.append(pid)
			url_base.write("http://market.yandex.ru/model.xml?hid=90578&modelid="+pid+"\n")

		url_list.pop()		
	url_base.close()
			#print (filename + " : "+(str(glob_left_index)+" : "+str(glob_right_index)+" : "+str((glob_right_index - glob_left_index)))+" : "+str(cursor) + " : "+html[cursor-9:cursor-2])
			#print (html[cursor:cursor+45])

def getProductName(lines):
	mst1 = lines.find("<h1 class=\"b-page-title b-page-title_type_model\">")+49
	return lines[mst1:lines.find("</h1>",mst1)]

def getAveragePrice(lines):
	return lines[lines.find("<span class=\"b-prices__num\">")+28:lines.find("</span>",lines.find("<span class=\"b-prices__num\">")+28)]

def getMinPrice(lines):
	return lines[lines.find("<span class=\"b-prices b-prices__range\">")+67:lines.find("</span>",lines.find("<span class=\"b-prices b-prices__range\">")+68)]

def getMaxPrice(lines):
	ind1 = lines.find("<span class=\"b-prices b-prices__range\">")+67
	return lines[(lines.find("<span class=\"b-prices__num\">",ind1))+28:lines.find("</span>",(lines.find("<span class=\"b-prices__num\">",ind1))+29)]

def getYandexVoices(lines):
	t_index1 = lines.find("<span class=\"b-rating b-rating_type_15 b-rating_type_model\" title=\"рейтинг товара\">")
	if(t_index1 == -1):
		return ("Voices not founded")
	else:
		t_indexr = lines.find("<div",t_index1+83)-11 # ???
		t_indexl = lines.rfind("alt=\"*\"",t_index1,t_indexr)+23
		return lines[t_indexl:t_indexr]

def getYandexScore(lines):
	t_index1 = lines.find("<span class=\"b-rating b-rating_type_15 b-rating_type_model\" title=\"рейтинг товара\">")
	if(t_index1 == -1):
		return ("Score not founded")
	else:
		t_indexr = lines.find("<div",t_index1+83)
		score = 5 - lines.count("<span title=\"\" class=\"b-rating__star\">",t_index1,t_indexr)
		return str(score)


getLinks()
		
#for pid in range(start_pid,start_pid+1):
for pid in url_list:
	print ("-------------------------------\n")
	print (pid)
	print ("Loading...\n")
	print ("-------------------------------\n")
	print ("\n")
	ya_url = "http://market.yandex.ru/model.xml?hid=90578&modelid="+str(pid)
	print (ya_url)
	page = urllib.request.urlopen(ya_url)
	lines = str(page.read().decode("utf-8"))
	#print (lines)
	print ("Processed :")
	lines = lines.rstrip("\n")
	lines = lines.rstrip("\r")
	lines = lines.rstrip("\r\n")
	print (getProductName(lines))
	print (getAveragePrice(lines))
	print (getMinPrice(lines))
	print (getMaxPrice(lines))
	print (getYandexVoices(lines).strip())
	print (getYandexScore(lines))
	time.sleep(5)
	#print (CurrentTime())
	#print (url_list)