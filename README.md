# The Tree of Knowledge 

### Built for FWT Project

Uses sqllite database to store Title, ID, ISBN and MD5 of 2.2M Libgen books and Flask to serve the HTML files

The data has been fetched using Libgen's internal API for all the ID's present in its database

To run the project - run ```python entry.py```
```pip install -r "requirements.txt"```

Project Flow:

* Entry Point - input.html. Enter Search query here

* ```search.py``` called. Searches for the query in sqlite database

* Returns a JSON object containing Title, ISBN and MD5 of the books which is displayed using Second.html

* On the book user clicks on - two things happen

  * ```dl.py``` is called. MD5 passed to it which is appended to lib1.org's url. The resulting page is scraped to get the direct download link of the book.

  * ```metadata_book.py``` is called and Title, ISBN is passed. It gets the book metadata using Google Books API. Then it scrapes Google Reviews for the book reviews.

* The result is displayed in bookpage.html

* After user clicks on download button, since cross-origin downloads are disabled by Chrome, the book is downloaded directly from python using wget.

