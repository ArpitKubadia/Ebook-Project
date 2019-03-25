import cx_Oracle
import pprint

#con = cx_Oracle.connect("ARPIT/arpit123@localhost/xe")
#cur = con.cursor()

def push(id,title,md5,isbn,cur):
	string="INSERT INTO BOOKS (ID, TITLE, MD5, ISBN) values("+id+",'"+title+"','"+md5+"',"+isbn+")"
	#print(string)
	cur.execute("INSERT INTO BOOKS (DATAID, TITLE, MD5, ISBN)\
		values("+id\
		+",'"+title\
		+"',"+"'"+md5\
		+"',"+isbn+")")

	cur.execute("commit")
