# this file have the main logic of the api
# we basically do 3 things here (or 2 and a half)
# the first one is have the control and logic of how to we retrieve the information of our search engine
# the second one is is scrap the information from the pages given the params of the request
# and third one we are calculating the idf for our ranking
# why I didn't make this a litle more dry speceally with the idf calculation?
# because I felt if we merged some stuff here, we could avoid call again some variables or make more stores of variables
# also to avoid loops trying to improve the complexity
# and ofcourse there should be a better solution out there
from bs4 import BeautifulSoup
from requests import get
from math import log
from urllib.parse import quote
from .tfidf import calculate_tf
from .db_functions import insertSearchResults, getSearch

# the main function we call to scarp and prepare our response
def scrapMe(keywords):

	# we format our keyword to make it a readable param to search in our pages
	search_word = quote(str(" ".join(keywords)))
	# and aux variable where we verify if we already searched this search word and return the results if we did
	return_content = getSearch(search_word)

	# if there is not a result for our search word, then we proceed
	if len(return_content) == 0:

		#we prepare our pages to search
		urls = [
			'https://www.nytimes.com/search?query=' + search_word,
			'https://edition.cnn.com/search?q=' + search_word,
			'https://www.bbc.co.uk/search?q=' + search_word
		]

		# an aux variable to store all our scrap results with the correct format
		results = []
		# an aux variable to store our semi raw results from our scrap
		aux_results = []
		# this variable we use it to calculate the idf
		# is the number of documents(or pages) with keywords in it
		sum_d = 0 

		# iterate our urls to scrap
		for url in urls:
			# we get the page
			response = get(url)
			# we format the page to a more readable variable
			html = BeautifulSoup(response.text, 'html.parser')
			# this will return the semi raw format of our scrap and a new sum_d
			formato, sum_d = formatHtml(html, url, keywords, sum_d)
			# we merge it with our aux_results list
			aux_results += formato

		# this variable we use it to calculate the idf
		# total number of documents(or pages)
		d = len(aux_results)

		# we calculate the idf here
		idf = log(d/sum_d)
		
		# we iterate all the semi raw results from our scra process
		for r in aux_results:
			# we calculate all the tf_idf per page
			tf_idf = r['tf']*idf
			# we format the result of each page and push it into results
			results.append({"content": r['content'], "reference": r['reference'], "ranking": tf_idf})

		# we sort the results by ranking in descending, making the ones with better ranking first
		results = sorted(results, key = lambda i: i['ranking'],reverse=True) 

		# select only the best 3 results from all our scraping
		return_content = [results[0], results[1], results[2]]
		
		# we insert all the results and search of the scraping
		insertSearchResults(search_word, return_content)

	# return the content of the database or our scrapping process
	return return_content

# this function format the result of the scrap to something we can work more with
# html is the full page in a readable format
# url is the full page where we use to scrap
# keywords are the search params we used to scrap
# sum_d is the number of documents(or pages) with keywords in it, and it will be changing each time
def formatHtml(html, url, keywords, sum_d):
	
	#an aux variable to store our results
	results = []
	# for this kind of scrapping, we are only getting the titles that goes under the
	# a tag of the articles we found per page
	documents = html.find_all('a')
	
	# we iterate the documents(or pages)
	for document in documents:
		# we get the reference of our page, in some cases this could be incomplete, so if that happens
		# it's filled with the origin of the url
		reference = document['href'] if 'http' in document['href'] else (url.split('/search')[0]+document['href'])
		# we get the text from our tag that represents the content
		content = document.get_text()
		# call the function to calculate the tf
		tf = calculate_tf(content, keywords)
		# if the tf is bigger than 0, that means that we found a coincidence in the document
		# therefore we sum 1 to our sum_d variable
		sum_d += 1 if tf > 0 else 0
		# we give a more readable format to our scrapping using the info we only want 
		results.append({"content": content, "reference": reference, "tf": tf})
	
	# we return all the scrapp results and the sum_d
	return [results, sum_d]
