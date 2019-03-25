import requests
import json
import pprint
from urllib.request import urlopen as uReq
import time
import random

p1="http://libgen.io/json.php?lg_topic=fiction&id_start="
p2="&fields=id,title,md5,isbn"
#index= 4000001


def extract(index):
	try:
		
		while(index<22000000):
			name=str(index)+"-"+str(index+10000)
			file=open(name+".txt","wb")
			url=p1+str(index)+p2
			uClient=uReq(url)
			json_response=uClient.read()
			uClient.close()
			#json_response=json.loads(json_response)
			file.write(json_response)
			#pprint.pprint(json_response,indent=4)
			index=index+10000
			print("Starting ",index)
			#if (index%50000 == 1):
			x=random.randint(250, 1000)/1000.0
			print("Sleeping for: ",x)
			time.sleep(x)

		print("done")
	except:
		print("Waiting for 300s")
		time.sleep(300)
		extract(index)

if __name__ == '__main__':
	index=int(input("Enter Index: "))
	extract(index)