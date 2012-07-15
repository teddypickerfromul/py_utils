#!/usr/bin/python3

# -*- coding: utf-8 -*-

import urllib.request,datetime
import codecs

url = "http://digibest.ru/administrator/info.php?status=s&id=107"
subscribers_amount = -1
orders_amount = 0
id_list = []

def currentDate():
	tmp = str(datetime.datetime.now())
	return tmp[0:tmp.find(" ")]

def correctPhone(line):
	pass

def genInfoString(line):
	global orders_amount
	result = ""
	cursor = line.find("<td>")+4
	border = line.find("</td>")
	result = result + line[cursor:border]+";"
	#print ("Имя Фамилия : "+line[cursor:border])
	name = line[cursor:border]
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor+4)
	result = result + line[cursor:border]+";"
	phone = line[cursor:border]
	#print (" Телефон : "+line[cursor:border])
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + line[cursor:border]+";"
	orders = line[cursor:border]
	#print ("Заказов : "+line[cursor:border])
	orders_amount = orders_amount + int(line[cursor:border])
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + line[cursor:border]+";"
	onid = line[cursor:border]
	#print ("Код купона : "+line[cursor:border])
	id_list.append(line[cursor:border])
	cursor = line.find("<td>",border+5)+4
	border = line.find("</td>",cursor)
	result = result + "Не указан" + ";" + ";" + "\n" # ???
	return result


page = urllib.request.urlopen(url)
html = str(page.read().decode("cp1251"))
#print (lines)
html = html.rstrip("\n")
html = html.rstrip("\r")

global_left_index = html.find("<table border=\"1\">")+18
global_right_index = html.find("</table>")

cursor = html.find("<tr>",global_left_index,global_right_index)
border = html.find("</tr>",cursor,global_right_index)

filename = "/home/teddy/info/Продажи купонов на "+currentDate()+".csv"
f = codecs.open(filename,"w","cp1251")

f.write(" ; ; ; ; ;\n")
f.write(";;Продажи купонов на "+currentDate()+";;\n")
f.write(" ; ; ; ; ;\n")
f.write("Имя и Фамилия покупателя;Телефон;Кол-во;Код купона;Вариант;E-mail;Время;\n")

while (border < global_right_index) and (cursor != 4):
	cursor = html.find("<tr>",cursor,global_right_index)
	if (cursor == -1):
		break
	else:
		subscribers_amount = subscribers_amount + 1
		border = html.find("</tr>",cursor,global_right_index)
		#print (html[cursor+4:border].strip("\n"))
		line = html[cursor+4:border].strip("\n")
		if(subscribers_amount > 0):
			#genInfoString(line)
			f.write(genInfoString(line))
		cursor = border + 5	

print (currentDate())
print ("Всего заказчиков : "+str(subscribers_amount))
print ("Всего заказов : "+str(orders_amount))
f.write(" ; ; ; ; ;\n")
f.write("Всего покупателей ;"+str(subscribers_amount)+";"+"\n")
f.write("Всего купонов ;"+str(orders_amount)+";"+"\n")
f.close()

