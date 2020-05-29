#this defines all the routes to our api
from flask import request, abort, Response
from json import dumps
from . import app
from .scrapper import scrapMe

#the only route we accept
@app.route('/api/news', methods=['POST'])
def hello_world():
	# we get the request body
	body = request.json
	# we validate the format of the request
	if (body is not None) and ('keywords' in body) and (type(body['keywords']) is list) and len(body['keywords']) > 0:
		# we call the function scapMe and then format the result to be responded in a proper json 
		return Response(dumps(scrapMe(body['keywords'])),  mimetype='application/json')
	else:
		#if the format is wrong, we let know the user using the proper http code of error
		abort(422, 'Wrong body format. https://http.cat/422')
