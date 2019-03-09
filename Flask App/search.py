import sqlite3
import pprint

def getJSON(output_dump):
	json_output=[]
	for book in output_dump:
		#for book in entries:
		#print(book)
		book_dict={}
		book_dict["id"]=book[0]
		book_dict["title"]=book[1]
		book_dict["isbn"]=book[2]
		book_dict["md5"]=book[3]
		json_output.append(book_dict)
	return(json_output)

def findValues(name):
	name=" "+name+" "
	name=name.replace(" ","%")
	conn = sqlite3.connect('bookdatabase.db') 
	c = conn.cursor()
	query='SELECT * FROM Bookdatabase where title like '+"'"+name+"'"
	#print(query)
	c.execute(query)
	output_dump=c.fetchall()
	conn.close()
	#print (output_dump)
	json_output=getJSON(output_dump)
	pprint.pprint(json_output)
	return json_output
	

if __name__ == '__main__':
	findValues("Harry Potter")