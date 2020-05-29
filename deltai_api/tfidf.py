
# calculates the tf from the content and the searching keywords
def calculate_tf(content, keywords):

	# an aux variable to store the tf per word
	tf_list = []

	# we iterate all the keywords
	for keyword in keywords:
		# number of times keyword appears in document
		# we count how many times does the keyword appers in the content
		t = (content.upper()).count(keyword.upper()) 
		# total number of word in document
		# we count all the words in the content
		td = len(content.split(' ')) 
		# we calculate the tf dividing t with td and then push the result to tf_list
		tf_list.append(t/td)

	# we calcuate the average tf of the document and return it
	return (sum(tf_list)/len(tf_list))
