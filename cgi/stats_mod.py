#!/usr/bin/python
##
## Filename:	stats.py
## Version:		6.5.1
## This file contains functions that:
##		retrieves results from the Google CustomSearch API
##		calculates the precision score
##		calculates the recall score
##		calculates the average precision score
##		displays the statistical analysis
##
import urllib
import re


def google_api(search, result_num):	
# Retrieve results from Google Custom Web Search API in an XML format
# Source:	http://www.google.com/support/forum/p/customsearch/thread?tid=56c0bd92dda351b7&hl=en
# Source:	http://code.google.com/apis/customsearch/v1/using_rest.html#query-params
	g_dict = {}
	api_key = 'AIzaSyAGhoWG_wP5xAEM7ifG41F7XnIcT2-Fnlg'
	results = float(result_num)/float(10)		# for tesing we will only obtain 10% (min 10) from google of the amount of results from the other search engines
	search_id = '012733187811704490272:leikl3-kfa0'

	start_num=1
	while start_num<results:
		link = 'https://www.googleapis.com/customsearch/v1?key='+api_key+'&cx='+search_id+'&q='+search+'&start='+str(start_num)+'&alt=atom'
		site = urllib.urlopen(link)		# opens url to search through
		read_file = site.read()			# reads url (file) text
		site.close()					# done with url (file), so close it
		
		url_find = re.findall(r'(<link href=")(.+?)(" title=")', read_file)
		link_num=1
		for url in url_find:
			g_link = url[1]
			g_dict[g_link] = link_num			
			link_num = link_num+1

		start_num = start_num+10

	return g_dict
	
def Precision(other_engine, google):
# Calculates the precision of a search
# i.e.: (number of relevant documments retrieved)/(total number of documents retrieved)
		
	rel_score = 0
# Get relevance scores
# Checks to make sure that the links retrieved by the meta search are relevant, w.r.t. Google
	for item in other_engine:
		if item in google:
			rel_score = rel_score + 1

# Get Precision Scores
	Precesion = float(rel_score)/float(len(other_engine))
	return Precesion
		
def Recall(other_engine, google):
# Calculates the recall of a search
# i.e.: (number of relevant documents retrieved)/(total number of relevant documents)
	
	rel_score = 0
# Get relevance scores
# Checks to make sure that the links retrieved by the meta search are relevant, w.r.t. Google
	for item in other_engine:
		if item in google:
			rel_score = rel_score + 1

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

def stat_display(option, Precision_Scores, Recall_Scores, AP_scores):
# Retrieves statistical scores & then dsiplays them
# Precision Score Retrieval
	meta_pr = re.search(r'(\w+:)(\d+\.*\d*)', Precision_Scores[0])
	bing_pr = re.search(r'(\w+:)(\d+\.*\d*)', Precision_Scores[1])
	yahoo_pr = re.search(r'(\w+:)(\d+\.*\d*)', Precision_Scores[2])
	ddgo_pr = re.search(r'(\w+:)(\d+\.*\d*)', Precision_Scores[3])
	
# Recall Score Retrieval
	meta_re = re.search(r'(\w+:)(\d+\.*\d*)', Recall_Scores[0])
	bing_re = re.search(r'(\w+:)(\d+\.*\d*)', Recall_Scores[1])
	yahoo_re = re.search(r'(\w+:)(\d+\.*\d*)', Recall_Scores[2])
	ddgo_re = re.search(r'(\w+:)(\d+\.*\d*)', Recall_Scores[3])

# Average Precision Scores
	meta_ap = re.search(r'(\w+:)(\d+\.*\d*)', AP_scores[0])
	bing_ap = re.search(r'(\w+:)(\d+\.*\d*)', AP_scores[1])
	yahoo_ap = re.search(r'(\w+:)(\d+\.*\d*)', AP_scores[2])
	ddgo_ap = re.search(r'(\w+:)(\d+\.*\d*)', AP_scores[3])

# Display Statistics
	print """
	<tr>
		<td>&nbsp;</td>
	</tr><tr>
	<td colspan="2"><!-- DISPLAY STATISTICS -->
		<div id="hide" style="display:block">
			<a href="#" title="Show/Hide Statistical Analysis" onclick="showStuff('show');hideStuff('hide')"><strong>Statistical Analysis &#9660;</strong></a>
		</div>
		<div id="show" style="display:none"><table>
		<tr><td>
			<a href="#" title="Show/Hide Statistical Analysis" onclick="showStuff('hide');hideStuff('show')"><strong>Statistical Analysis &#9650;</strong></a>
		</td></tr>
		<tr><td>&nbsp;</td></tr>
		<tr>
			<td><div id="stat1_off">
				&nbsp;&nbsp;<a href="#" title="Show/Hide Precision Scores" onclick="showStuff('stat1_on');hideStuff('stat1_off')"><strong>Precision Scores &#9660;</strong></a>
			</div><div id="stat1_on" style="display:none">
				&nbsp;&nbsp;<a href="#" title="Show/Hide Precision Scores" onclick="showStuff('stat1_off');hideStuff('stat1_on')"><strong>Precision Scores &#9650;</strong></a>
				<table><tr>
					<td>&nbsp;<img src="../imgs/icons/meta.ico" title="Meta-Search"" alt="Meta-Search" /></td>
					<td>&nbsp;</td>
	"""
	print '	<td>'+meta_pr.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/bing.ico" title="Bing" alt="Bing"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+bing_pr.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/yahoo.ico" title="Yahoo!" alt="Yahoo!"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+yahoo_pr.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/ddgo.ico" title="DuckDuckGo" alt="DuckDuckGo"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+ddgo_pr.group(2)+'</td>'
	print """
			</tr></table>
		</div></td>
	</tr><tr>
		<td><div id="stat2_off">
			&nbsp;&nbsp;<a href="#" title="Show/Hide Recall Scores" onclick="showStuff('stat2_on');hideStuff('stat2_off')"><strong>Recall Scores &#9660;</strong></a>
		</div><div id="stat2_on" style="display:none">
			&nbsp;&nbsp;<a href="#" title="Show/Hide Recall Scores" onclick="showStuff('stat2_off');hideStuff('stat2_on')"><strong>Recall Scores &#9650;</strong></a>
			<table><tr>
				<td>&nbsp;<img src="../imgs/icons/meta.ico" title="Meta-Search"" alt="Meta-Search" /></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+meta_re.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/bing.ico" title="Bing" alt="Bing"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+bing_re.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/yahoo.ico" title="Yahoo!" alt="Yahoo!"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+yahoo_re.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/ddgo.ico" title="DuckDuckGo" alt="DuckDuckGo"/></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+ddgo_re.group(2)+'</td>'
	print """
			</tr></table>
		</div></td>
	</tr><tr>
		<td><div id="stat3_off">
			&nbsp;&nbsp;<a href="#" title="Show/Hide Average Precision Scores" onclick="showStuff('stat3_on');hideStuff('stat3_off')"><strong>Average Precision Scores &#9660;</strong></a>
		</div><div id="stat3_on" style="display:none">
			&nbsp;&nbsp;<a href="#" title="Show/Hide Average Precision Scores" onclick="showStuff('stat3_off');hideStuff('stat3_on')"><strong>Average Precision Scores &#9650;</strong></a>
			<table><tr>
				<td>&nbsp;<img src="../imgs/icons/meta.ico" title="Meta-Search" alt="Meta-Search" /></td>
				<td>&nbsp;</td>
	"""
	print '	<td>'+meta_ap.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/bing.ico" title="Bing" alt="Bing"/></td>
				<td>&nbsp;</td>
	"""
	print '<td>'+bing_ap.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/yahoo.ico" title="Yahoo!" alt="Yahoo!"/></td>
				<td>&nbsp;</td>
	"""
	print '<td>'+yahoo_ap.group(2)+'</td>'
	print """
			</tr><tr>
				<td>&nbsp;<img src="../imgs/icons/ddgo.ico" title="DuckDuckGo" alt="DuckDuckGo"/></td>
				<td>&nbsp;</td>
	"""
	print '<td>'+ddgo_ap.group(2)+'</td>'
	print """
			</tr></table>
		</div></td>
	</tr></table></div></td></tr>
	"""