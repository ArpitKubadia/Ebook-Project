import requests
import json
import pprint
from urllib.request import urlopen as uReq
import database_pusher as db
import cx_Oracle

p1="http://libgen.io/json.php?lg_topic=fiction&id_start=1&limit1=100"
p2="&fields=id,title,md5,isbn"

con = cx_Oracle.connect("ARPIT/arpit123@localhost/xe")
cur = con.cursor()

index=1

url=p1+p2
uClient=uReq(url)
json_response=uClient.read()
uClient.close()
pprint.pprint(json_response,indent=4)
json_response=json.loads(json_response)



for titles in json_response:
	if(titles["title"]==""):
		titles["title"]="NA"
	if(titles["isbn"]==""):
		titles["isbn"]="0"

	db.push(titles["id"],titles["title"],titles["md5"],titles["isbn"],cur)

con.close()
print("done")