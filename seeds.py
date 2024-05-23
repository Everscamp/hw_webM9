from models import Author, Quote
from connect import connect
import json

f = open('quotes_spyder/authors.json')
authors = json.load(f)

authors_list = []
for i in authors:
    author = Author(fullname=i.get('fullname'), 
    born_date=i.get('born_date'), 
    born_location=i.get('born_location'), 
    description=i.get('description')).save()
    authors_list.append(author)

f = open('quotes_spyder/quotes.json')
quotes = json.load(f)

for i in quotes:
    Quote(tags=i.get('tags'), 
    author=authors_list[0] if i.get('author') == 'Albert Einstein' else authors_list[1], 
    quote=i.get('quote')).save()

if __name__ == "__main__":
    ...