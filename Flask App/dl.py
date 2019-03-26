import requests
from urllib.request import urlopen as uReq
import json
from bs4 import BeautifulSoup as soup

import pprint

p1="http://lib1.org/fiction/"
def getLink(md5):
	url=p1+str(md5)
	uClient=uReq(url)
	page_html=uClient.read()
	uClient.close()
	page_soup=soup(page_html,"html.parser")
	#pprint.pprint(page_soup,indent=4)
	containers=page_soup.find(id="info")
	link=containers.find('h2').find('a').get("href")
	print(link)
	return(link)

if __name__ == '__main__':
 	getLink("b65ce3b9bd242fdaa188468df9a727ef") 
 	#Dummy Harry Potter MD5