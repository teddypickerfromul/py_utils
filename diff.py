#!/usr/bin/python3

# -*- coding: utf-8 -*-

import urllib.request,datetime
import codecs

def currentDate():
	tmp = str(datetime.datetime.now())
	return tmp[0:tmp.find(" ")]

url = "http://digibest.ru/administrator/info.php?status=s&id=107"
input_filename = "./Продажи купонов на "+currentDate()+".csv"
diff_filename = "./Новые для "+currentDate()+".csv"
#output_filename	= "./Продажи купонов на "+сurrentDate()+"(Обновлено).csv"
new_customers_list = []

phones_list = []
updated_phone_list = []
id_list = []
updated_id_list = []

def genInfoString(line):
	result = ""
	cursor = line.find("<td>")+4
	border = line.find("</td>")
	result = result + line[cursor:border]+";"
	name = line[cursor:border]
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor+4)
	result = result + line[cursor:border]+";"
	phone = line[cursor:border]
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + line[cursor:border]+";"
	orders = line[cursor:border]
	#orders_amount = orders_amount + int(line[cursor:border])
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + line[cursor:border]+";"
	onid = line[cursor:border]
	#id_list.append(line[cursor:border])
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + "Не указан" + ";" + ";" + "\n" # ???
	return result

def extractPhone(result):
	cursor = result.find(";")+1
	border = result.find(";",cursor)
	return result[cursor:border]

def extractId(result):
	cursor = result.find(";")+1
	border = result.find(";",cursor)
	cursor = border+1
	cursor = result.find(";",cursor)+1
	border = result.find(";",cursor)
	return result[cursor:border]

def generateOldLists():
	temp = 1
	f = codecs.open(input_filename,"r","cp1251")
	while True:
		line = f.readline()
		temp = temp + 1
		if not line:
			break
		if temp	> 4:
			phone = extractPhone(line)
			c_id = extractId(line)
			phones_list.append(phone)
			id_list.append(c_id)
	f.close()

def searchForRemoved():
	temp = 1
	f = codecs.open(input_filename,"r","cp1251")
	while True:
		line = f.readline()
		temp = temp + 1
		if not line:
			break
		if temp	> 4:
			phone = extractPhone(line)
			c_id = extractId(line)
			if not(searchForId(c_id,"r")) and not(searchForPhone(phone,"r")):
				print ("Удалены : "+line)
			#phones_list.append(phone)
			#id_list.append(c_id)
	f.close()	
	
							
def searchForPhone(phone,mode):
	if (mode  == "a"):
		if (phone in phones_list):
			return True
		else:
			return False
	if (mode == "r"):
		if (phone in updated_phone_list):
			return True
		else:
			return False
		
def searchForId(id,mode):
	if (mode == "a"):
		if (id in id_list):
			return True
		else:
			return False
	if (mode == "r"):
		if (id in updated_id_list):
			return True
		else:
			return False			
			
page = urllib.request.urlopen(url)
html = str(page.read().decode("cp1251"))
html = html.rstrip("\n")
html = html.rstrip("\r")

global_left_index = html.find("<table border=\"1\">")+18
global_right_index = html.find("</table>")

cursor = html.find("<tr>",global_left_index,global_right_index)
border = html.find("</tr>",cursor,global_right_index)

generateOldLists()

while (border < global_right_index) and (cursor != 4):
	cursor = html.find("<tr>",cursor,global_right_index)
	if (cursor == -1):
		break
	else:
		border = html.find("</tr>",cursor,global_right_index)
		line = html[cursor+4:border].strip("\n")
		result = genInfoString(line)
		phone = extractPhone(result)
		c_id = extractId(result)
		updated_id_list.append(c_id)
		updated_phone_list.append(phone)
		if not(searchForId(c_id,"a")) and not(searchForPhone(phone,"a")):
			print ("Новая запись : "+result)		
	cursor = border + 5	

searchForRemoved()

#print (id_list) 
#print (updated_id_list)
	