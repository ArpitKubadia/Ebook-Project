import cx_Oracle
import pprint

con = cx_Oracle.connect("ARPIT/arpit123@localhost/xe")
cur = con.cursor()

cur.execute("DROP TABLE BOOKS")

cur.execute("CREATE TABLE BOOKS(DATAID NUMBER(10) PRIMARY KEY,\
	TITLE VARCHAR(100),\
  ISBN NUMBER(20),\
   MD5 VARCHAR(50))")
