# in this file we define our insert tables
from deltai_api import db
from sqlalchemy.dialects.mysql import LONGTEXT, TEXT

# this table is going to store only the search param 
class Searches(db.Model):
	id = db.Column(db.String(255), primary_key=True)

	def __repr__(self):
		return '<Searches {}>'.format(self.id)

# this table is going to store the pages of our search 
class Content(db.Model):
	id = db.Column(db.Integer, primary_key=True) #autoincrement id
	ranking = db.Column(db.FLOAT, unique=False, nullable=False) # the ranking
	content = db.Column(LONGTEXT, unique=False, nullable=False) # the content of the page we found
	reference = db.Column(TEXT(65535), unique=False, nullable=False) # the url of the page 
	search_id = db.Column(db.String(255), db.ForeignKey('searches.id')) # this is the foreign key to our search param

	def __repr__(self):
		return '<Content {}>'.format(self.id)

