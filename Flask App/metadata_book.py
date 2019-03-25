import pprint
import sys
from googleapiclient.discovery import build
import urllib.request
import json
import fetch_reviews
api_key='AIzaSyAMHyrWXEE4YmI-ppBxDFRPTr06R-6sgO4'
data={}
def meta1(title,isbn):
    if isbn!=0:
        q_req=isbn
    else:
        q_req=title
    service = build('books', 'v1', developerKey=api_key)
    request = service.volumes().list(source='public', q=q_req)
    response = request.execute()
    book=response['items'][0]
    try:
        title=book['volumeInfo']['title']
        data['title']=title
    except Exception:
        pass
    try:
        authors=book['volumeInfo']['authors']
        data['authors']=authors
    except Exception:
        pass
    try:
        description=book['volumeInfo']['description']
        data['description']=description
    except Exception:
        pass
    try:
        average_rating=book['volumeInfo']['averageRating']
        data['average_rating']=average_rating
    except Exception:
        pass
    try:
        rating_count=book['volumeInfo']['ratingsCount']
        data['rating_count']=rating_count
    except Exception:
        pass
    try:
        page_count=book['volumeInfo']['pageCount']
        data['page_count']=page_count
    except Exception:
        pass
    try:
        publisher_name=book['volumeInfo']['publisher']
        data['publisher_name']=publisher_name
    except Exception:
        pass
    try:
        book_image=book['volumeInfo']['imageLinks']['thumbnail']
        data['book_image']=book_image
    except Exception:
        pass
    try:
        review_fetch_link=book['volumeInfo']['canonicalVolumeLink']
        data['review_fetch_link']=review_fetch_link
        review=fetch_reviews.fetch_rev(review_fetch_link)
        data['reviews']=review
    except Exception:
        pass
    #with open("meta_data_file.json", "w") as write_file:
    #    json.dump(data, write_file)
    #jason_data=json.dumps(data)
    return(data)
'''
if __name__ == '__main__':
   print('main called')
   meta1('harry potter and the order of the phoenix',1408855674)
'''