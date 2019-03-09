import libgenapi
import json
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup

def findMirrors(name):
	lg=libgenapi.Libgenapi(["http://libgen.io/"])
	output=lg.search("python",1)
	json_output=json.dumps (output, sort_keys=True,indent=4)
	print(json_output)

	loaded_data=json.loads(json_output)

	result=[]
	for data in loaded_data:
		if(data['mirrors']!=None):
			for mirror in data['mirrors']:
				print(mirror)

if __name__ == "__main__":
	findMirrors("Harry Potter and the Order of the Phoenix")