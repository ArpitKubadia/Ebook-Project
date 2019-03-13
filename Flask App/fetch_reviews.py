from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def fetch_rev(url1):
	my_url=url1
	uClient=uReq(my_url)
	page_html=uClient.read()
	uClient.close()
	review=[]
	#htmlparser
	page_soup=soup(page_html,"html.parser")

	#getting each product on the page
	containers = page_soup.findAll("a",{"class":"secondary"})

	for container in containers:
		#print(container.contents[0])
	    if "All" in container.contents[0]:
	        rev_link=container['href']
	        #print(rev_link)
	my_url=rev_link
	uClient=uReq(my_url)
	page_html=uClient.read()
	uClient.close()

	page_soup=soup(page_html,"html.parser")

	container2 = page_soup.findAll("div",{"class":"single-review"})

	for container in container2:
	    try:
	        review_a=container.find("span",{"dir":"ltr"}).text
	        review.append(review_a)
	        #print(review_a)
	        #print("********END************")
	    except AttributeError:
	        print("****Error Occured******")
	#print(review)
	return(review)


#if __name__ == '__main__':
    #print('main called')
#    fetch_rev('https://books.google.com/books/about/Harry_Potter_and_the_Order_of_the_Phoeni.html?hl=&id=jk87_y-ubE0C')


