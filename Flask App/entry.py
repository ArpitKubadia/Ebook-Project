from flask import Flask, render_template, flash, redirect, request, session, abort
import search
import dl

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
	download_link=dl.getLink(md5)

	return render_template('bookpage.html',title=title,link=download_link,isbn=isbn)

if __name__ == "__main__":
    app.run()