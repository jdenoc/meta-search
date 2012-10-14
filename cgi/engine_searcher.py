#!/usr/bin/python
##
## Filename:	engine_searcher.py
## Version:		6.0
##
import urllib
import re

def open_doc(link):
# opens sites, retrieves site code, closes site & then returns site code
	site = urllib.urlopen(link)		# opens url to search through
	read_file = site.read()			# reads url (file) text
	site.close()					# done with url (file), so close it
	return read_file
# END open_doc

def link_trimmer(site_links):
# recieves the strings found in the sites & then trims them down to just the urls
	trimmed_links = []
	
	for link in site_links:
		url = link[1]
		title = link[3]
		trimmed_links.append((url, title))		# appends a tuple containing the site address & title to a list

	return trimmed_links
# END link_trimmer

###################  individual search engine link finders  ###################
link_criterion = "[+',\s$=;@?!%&:\w./_()#-]+"

def link_finder_ddgo(code):
# searches through DuckDuckGo site for usable url links
	url_match_ddgo = re.findall(r'(<a rel="nofollow" class="l le" href=")('+link_criterion+')(">)(.+)(</a>)', code)
	ddgo_links = link_trimmer(url_match_ddgo)
	return ddgo_links
# END link_finder_ddgo

def link_finder_bing(code):
# searches through Bing site for usable url links
	url_match_bing = re.findall(r'(<h3><a href=")('+link_criterion+')(" onmousedown="return si_T.+?">)(.+?)(</a>)', code)	# (.+?)		This indicates 1 or more of any character, but in a non-greedy form
	if url_match_bing:
		bing_links = link_trimmer(url_match_bing)
		return bing_links
# END link_finder_bing
	
def link_finder_yahoo(code):
# searches through Yahoo site for usable links
	url_match_yahoo = re.findall(r'(<a class="yschttl spt" href=")('+link_criterion+')(" data-.+?>)(.+?)(</a>)', code)
	if url_match_yahoo:
		yahoo_links = link_trimmer(url_match_yahoo)
		return yahoo_links
# END link_finder_yahoo


def next_page_ddgo(code):
# searches HTML code of DuckDuckGo site for a link to next page of results
	url_match_next = re.search(r'(<!-- <a rel="next" href=".html.+q=)('+link_criterion+')(">Next Page &gt;</a> //-->)', code)
	if url_match_next:
		next_page = 'http://duckduckgo.com/html/?q=' + url_match_next.group(2)
		return next_page
# END next_page_ddgo

def next_page_bing(search, page_num):
# produces links for next page of results in Bing
	num = str(page_num+1)
	next_page = 'http://www.bing.com/search?q='+search+'&first='+num+'1&FORM=PORE'
	return next_page
# END next_page_bing

def next_page_yahoo(code):
# searches HTML code of Yahoo site for a link to next page of results
	url_match_next = re.search(r'(<a id="pg-next" href=")('+link_criterion+')(">Next &gt;</a>)', code)
	if url_match_next:
		next_page = url_match_next.group(2)
		return next_page
# END next_page_yahoo
###################  END of individual search engine link finders  ###################
