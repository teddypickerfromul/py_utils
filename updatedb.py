#!/usr/bin/python3

# -*- coding: utf-8 -*-

import urllib.request,datetime
import codecs
import os

url = "http://digibest.ru/administrator/info.php?status=s&id=107"
db_filename = "/home/teddy/info/DB/Common/commondb.csv"
stat_filename = "/home/teddy/info/DB/Common/stat.txt"

def currentDate(mode):
	if (mode == "date"):
		tmp = str(datetime.datetime.now())
		return tmp[0:tmp.find(" ")]
	if (mode == "full"):
		tmp = str(datetime.datetime.now())
		return tmp[0:tmp.find(".")]	

def ifDbExist(db_filename):
	if os.path.exists(db_filename):
		return True
	else:
		return False

def ifStatFileExist(stat_filename):
	if os.path.exists(stat_filename):
		return True
	else:
		return False

def genInfoString(line,mode):
	if (mode == "c"):
		global orders_amount
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
		orders_amount = orders_amount + int(line[cursor:border])
		cursor = line.find("<td>",border+5)+4
		border = line.find("</td>",cursor)
		result = result + line[cursor:border]+";"
		onid = line[cursor:border]
		id_list.append(line[cursor:border])
		cursor = line.find("<td>",border+5)+4
		border = line.find("</td>",cursor)
		result = result + "Не указан" + ";" + ";" + "\n" # ???
		return result
	if(mode == "u"):
		#global orders_amount
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
		#orders_amount = orders_amount + int(line[cursor:border]) ### доделать
		result = result + line[cursor:border]+";"
		orders = line[cursor:border]
		cursor = line.find("<td>",border+5)+4
		border = line.find("</td>",cursor)
		result = result + line[cursor:border]+";"
		onid = line[cursor:border]
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

def generateOldLists(): # баг с построчным чтением - читает все подряд!
	temp = 1
	f = codecs.open(db_filename,"r","cp1251")
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
	f = codecs.open(db_filename,"r","cp1251")
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

print ("Проверяю наличие бд...")
if not(ifDbExist(db_filename)):
	
	subscribers_amount = -1
	orders_amount = 0
	phones_list = []
	updated_phone_list = []
	id_list = []
	updated_id_list = []

	print ("Файл бд не найден.")
	print ("Создаю новый файл бд.\nДата создания :"+currentDate("date"))
	print ("Время "+currentDate("full"))
	page = urllib.request.urlopen(url)
	html = str(page.read().decode("cp1251"))
	html = html.rstrip("\n")
	html = html.rstrip("\r")

	db = codecs.open(db_filename,"w","cp1251")
	stat = codecs.open(stat_filename,"w","cp1251")
	stat.write("Файл создан "+str(currentDate("full"))+" \n")

	global_left_index = html.find("<table border=\"1\">")+18
	global_right_index = html.find("</table>")

	cursor = html.find("<tr>",global_left_index,global_right_index)
	border = html.find("</tr>",cursor,global_right_index)

	db.write(" ; ; ; ; ;\n")
	db.write(";;Продажи на "+str(currentDate("full"))+";;\n")
	db.write(" ; ; ; ; ;\n")
	db.write("Имя и Фамилия покупателя;Телефон;Кол-во;Код купона;Вариант;E-mail;Время;\n")

	while (border < global_right_index) and (cursor != 4):
		cursor = html.find("<tr>",cursor,global_right_index)
		if (cursor == -1):
			break
		else:
			subscribers_amount = subscribers_amount + 1
			border = html.find("</tr>",cursor,global_right_index)
			line = html[cursor+4:border].strip("\n")
			if(subscribers_amount > 0):
				db.write(genInfoString(line,"c"))
			cursor = border + 5
			
	stat.write("На "+currentDate("full")+" статистика :\n")
	stat.write("Всего покупателей :"+str(subscribers_amount)+"\n")
	stat.write("Всего купонов :"+str(orders_amount)+"\n")
	stat.close()

else:
# обновление бд
#if (ifDbExist(db_filename)):
	subscribers_amount = -1
	orders_amount = 0
	phones_list = []
	updated_phone_list = []
	id_list = []
	updated_id_list = []

	str_cnt = 1

	print ("Файл найден.")
	print ("Обновление базы данных.")
	print ("Время обновления : "+currentDate("full"))

	page = urllib.request.urlopen(url)
	html = str(page.read().decode("cp1251"))
	html = html.rstrip("\n")
	html = html.rstrip("\r")

	global_left_index = html.find("<table border=\"1\">")+18
	global_right_index = html.find("</table>")

	cursor = html.find("<tr>",global_left_index,global_right_index)
	border = html.find("</tr>",cursor,global_right_index)

	generateOldLists()
	db = codecs.open(db_filename,"a","cp1251")
	stat = codecs.open(stat_filename,"a","cp1251")
	stat.write("[ "+str(currentDate("full"))+" ] Обновление : { ")

	while (border < global_right_index) and (cursor != 4):
		cursor = html.find("<tr>",cursor,global_right_index)
		if (cursor == -1):
			break
		else:
			subscribers_amount = subscribers_amount + 1
			border = html.find("</tr>",cursor,global_right_index)
			line = html[cursor+4:border].strip("\n")
			result = genInfoString(line,"u")
			phone = extractPhone(result)
			c_id = extractId(result)
			updated_id_list.append(c_id)
			updated_phone_list.append(phone)
			if not(searchForId(c_id,"a")) and not(searchForPhone(phone,"a")):
				#print ("Новая запись : "+result)
				db.write(result)
				stat.write("Добавлен покупатель c кодом купона = "+c_id+" и телефоном = "+phone+"\n")						
			cursor = border + 5
				
	#stat.write("Всего покупателей ;"+str(subscribers_amount)+"\n")
	#stat.write("Всего купонов ;"+str(orders_amount)+"\n")
	stat.write("}\n")
	db.close()
	stat.close()