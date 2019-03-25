import database_pusher as db
import cx_Oracle
import glob
import os
import json
import pprint

path="C:/Users/Arpit/Documents/6th Sem/FWT/Ebook Project/Dont Touch This/Data Dumps/"

'''
for txt_file in glob.glob(path+"*.txt"):
	txt_file=txt_file.replace("\\","/")
	print(txt_file)
	#print(os.path.basename(txt_file))
'''

file=open("C:/Users/Arpit/Documents/6th Sem/FWT/Ebook Project/Dont Touch This/Data Dumps/1-10001.txt","r")
file=file.read()
file=json.loads(file)
for main_arr in file:
	print(main_arr["id"])
	print(main_arr["title"])
	print(main_arr["md5"])
	print(main_arr["isbn"])

#pprint.pprint (file,indent=4)
