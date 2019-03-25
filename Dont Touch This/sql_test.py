import sqlite3
conn = sqlite3.connect('bookdatabase.db')
 
c = conn.cursor()
c.execute('SELECT count(id) FROM Bookdatabase')


print (c.fetchall()[0][0])
conn.close()
