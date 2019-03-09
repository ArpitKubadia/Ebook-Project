from alchemy_creator import Book, Base
from sqlalchemy import create_engine
engine = create_engine('sqlite:///bookdatabase.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Make a query to find all Persons in the database
out=session.query(Book).all()
print(out.fetchall())