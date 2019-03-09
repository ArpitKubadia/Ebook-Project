import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pprint


def search(name):
	name=name.replace(" ","+")
	url="http://libgen.io/search.php?req="+name+"&res=50"
	uClient=uReq(url)
	page_html=uClient.read()
	uClient.close()
	page_soup=soup(page_html,"html.parser")
	pprint.pprint(page_soup,indent=4)


if __name__ == '__main__':
	search("Harry Potter")