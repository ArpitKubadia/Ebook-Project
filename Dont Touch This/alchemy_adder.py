from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from alchemy_creator import Book,Base

import database_pusher as db
import glob
import os
import json
import pprint

engine = create_engine('sqlite:///bookdatabase.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

path="C:/Users/Arpit/Documents/6th Sem/FWT/Ebook Project/Dont Touch This/Data Dumps/"

for txt_file in glob.glob(path+"*.txt"):
	txt_file=txt_file.replace("\\","/")
	print(txt_file)
	file=open(txt_file,"r")
	file=file.read()
	file=json.loads(file)
	for main_arr in file:
		tid=main_arr["id"]
		ttitle=main_arr["title"]
		tmd5=main_arr["md5"]
		tisbn=main_arr["isbn"]
		new_book=Book(id=tid,title=ttitle,md5=tmd5,isbn=tisbn)
		session.add(new_book)

	session.commit()
	print("Commited: ",txt_file)