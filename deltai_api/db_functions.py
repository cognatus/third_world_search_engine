# in this file we have all the db operations for the project
from deltai_api import db
from .models import Searches, Content

# this functions triggers the inserts of our search
# we receive the search param and the 3 contents of the search
def insertSearchResults(search, contents):
	#with this funtion we insert the search as a kind of index
	insertSearch(search)
	# iterate all the contents to be inserted one by one
	for content in contents:
		insertContent(search, content)

#inserts info into searches
# we recive the search param
def insertSearch(search):
	# call the model and prepare the insert into searches table
	query = Searches(id=search)
	# add the query to be inserted
	db.session.add(query)
	# excecute the query
	db.session.commit()

#inserts info into content
# we recive the search param and the content
def insertContent(search, content):
	# call the model and prepare the insert into content table
	query = Content(
		ranking=content['ranking'],
		content=content['content'],
		reference=content['reference'],
		search_id=search #remember this is the foreign key to searches
	)
	# add the query to be inserted
	db.session.add(query)
	# excecute the query
	db.session.commit()

# looks for the search to see if it exist
def getSearch(search):
	# get the search from the table searches
	search_result = Searches.query.get(search)
	# returns the result of the search
	result = []

	# if there is a row, we enter the if
	if search_result is not None:
		# get all the contents of the search from the table content
		contents = Content.query.filter_by(search_id = search).all()
		# iterate the results of the table
		for c in contents:
			# we insert each result to our varible and format it to the response we want
			result.append({
				"ranking": c.ranking,
				"content": c.content,
				"reference": c.reference
			})

	# returns the result of the search
	return result
