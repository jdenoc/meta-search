#!/usr/bin/python
##
## Filename:	stats.py
## Version:		5.4.1
##
import json
import urllib
import re


def google_api(search, result_num):	
# Retrieve results from Google Custom Web Search API
# Source:	http://www.google.com/support/forum/p/customsearch/thread?tid=56c0bd92dda351b7&hl=en
# Source:	http://code.google.com/apis/customsearch/v1/using_rest.html#query-params
	g_dict = {}
	api_key = 'AIzaSyAGhoWG_wP5xAEM7ifG41F7XnIcT2-Fnlg'
	results = result_num/10		# for tesing we will only obtain 10% (min 10) from google of the amount of results from the other search engines
	search_id = '012733187811704490272:leikl3-kfa0'

	i=1
	while i<results:
		link = 'https://www.googleapis.com/customsearch/v1?key='+api_key+'&cx='+search_id+'&q='+search+'&start='+str(i)
		site = urllib.urlopen(link)		# opens url to search through
		read_file = site.read()			# reads url (file) text
		site.close()					# done with url (file), so close it
		
		data = json.loads(read_file)
		hits = data['items']
		j=1
		for h in hits:
			#print j,' ', h['link'], '-', h['title']
			link = h['link']
			g_dict[link] = j
			j=j+1
		
		i=i+10

	return g_dict
	
def Precision(other_engine, google):
# Calculates the precision of a search
# i.e.: (number of relevant documments retrieved)/(total number of documents retrieved)
		
# Get relevance scores
# Checks to make sure that the links retrieved by the meta search are relevant, w.r.t. Google
	rel_score = 0
	for item in other_engine:
		#print item
		if item in google:
			rel_score = rel_score + 1
			#print rel_score

	# Get Precision Scores
	Precesion = float(rel_score)/float(len(other_engine))
	return Precesion
	
	
def Recall(other_engine, google):
# Calculates the recall of a search
# i.e.: (number of relevant documents retrieved)/(total number of relevant documents)
	
# Get relevance scores
# Checks to make sure that the links retrieved by the meta search are relevant, w.r.t. Google
	rel_score = 0
	for item in other_engine:
		#print item
		if item in google:
			rel_score = rel_score + 1
			#print rel_score

# Get Recall Scores
	Recall = float(rel_score)/float(len(google))
	return Recall

def Average_Precision(other_engine, google):
# Calculates the Average Precision Score
# Average Precision = (sum of precision at each recall point)/(No. of relevant documents Retrieved)

	r = 0				# number of relevant documents
	index = 1			# index number of the rank of a link
	PR_scores = []		# a list to store all the scores recorded
	top_10_links = []	# stores a list of top 10 ranked links retrieved
	google_top_10 = []	# stores a list of top 10 ranked links from google
	
	links = sorted(other_engine, key=other_engine.get)
	google_sorted = sorted(google, key=google.get)
	
	for url in links:
		top_10_links.append(url)
	for url in google_sorted:
		google_top_10.append(url)
		
	for url in top_10_links:
		if url in google:
			PR = float(r)/float(index)	# Precision/Recall score
			PR_scores.append(PR)
			r = r+1
		index = index + 1
	
	sum = 0
	for score in PR_scores:	# gets the sum of the Prec scores
		sum = sum + score
	if len(PR_scores) > 0:
		AP_score = float(sum)/float(len(PR_scores))
	else:
		AP_score = 0
	
	return AP_score
