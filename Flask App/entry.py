from flask import Flask, render_template, flash, redirect, request, session, abort
import search
import dl
import metadata_book
import wget
import urllib.parse as urlparse
import os
from datetime import datetime

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True



@app.route("/")
def hello():
    return render_template('input.html')


@app.route('/search/<name>', methods=['GET'])
def api_id(name):
	out=search.findValues(name)
	return render_template('second.html',result=out)

@app.route('/details',methods=['GET'])
def get_details():
	title=request.args.get('title',None)
	md5=request.args.get('md5',None)
	isbn=request.args.get('isbn',None)
	print(md5)
	if (len(isbn)==10 or len(isbn)==13):
		isbn=isbn
	else:
		isbn=0

	start=datetime.now()

	#Sends MD5 to dl.py to get Download link
	download_link=dl.getLink(md5)

	#Sends title and isbn to google books api to get book details
	meta_data=metadata_book.meta1(title,isbn)

	#To measure performance
	end=datetime.now()
	time=end-start
	time=time.total_seconds()
	print("TIME: ",time)

	#Getting book's extension from the download link
	path = urlparse.urlparse(download_link).path
	ext = os.path.splitext(path)[1]
	print (ext)
	print(meta_data)
	return render_template('bookpage.html',title=title,link=download_link,isbn=isbn,metadata=meta_data,extension=ext)

@app.route('/download',methods=['GET'])
def downloading():
	link=request.args.get('link',None)
	print("Link Received")
	wget.download(link)
	print("Downloading")
	return render_template('download.html')

if __name__ == "__main__":
    app.run()