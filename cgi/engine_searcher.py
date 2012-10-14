#!/usr/bin/python
##
## Filename: engine_searcher.py
##
import urllib
import re

def open_doc(link):
# opens sites, retrieves site code, closes site & then returns site code
	site = urllib.urlopen(link)	# opens url to search through
	read_file = site.read()				# reads url (file) text
	site.close()						# done with url (file), so close it
	return read_file
# END open_doc


def link_trimmer(site_links):
# recieves the strings found on the sites & then trims them down to just the urls
	trimmed_links = []
	i=0		# counter
	
	for link in site_links:
		if link[1] not in trimmed_links and i < 10:		
			trimmed_links.append(link[1])
			i = i + 1
	return trimmed_links
# END link_trimmer

###################  individual search engine link finders  ###################
link_criterion = '[+,\s$=;@?!%&:\w./_()#-]+'

def link_finder_ddgo(ddgo_read):
# searches through DuckDuckGo site for usable url links
	url_match_ddgo = re.findall(r'(<a rel="nofollow" href=")('+link_criterion+')(")', ddgo_read)
	ddgo_links = link_trimmer(url_match_ddgo)
	return ddgo_links
#END link_finder_ddgo

def link_finder_bing(bing_read):
# searches through Bing site for usable url links
	url_match_bing = re.findall(r'(<h3><a href=")('+link_criterion+')(" onmousedown="return)', bing_read)
	bing_links = link_trimmer(url_match_bing)
	return bing_links
#END link_finder_bing
	
def link_finder_yahoo(yahoo_read):
# searches through Yahoo site for usable links
	url_match_yahoo = re.findall(r'(<a class="yschttl spt" href=")('+link_criterion+')', yahoo_read)
	yahoo_links = link_trimmer(url_match_yahoo)
	return yahoo_links
#END link_finder_yahoo

def next_page_ddgo(ddgo_read):
# searches HTML code of DuckDuckGo site for a link to next page of results
	url_match_next = re.search(r'(<!-- <a rel="next" href=".html.+q=)('+link_criterion+')(">Next Page &gt;</a> //-->)', ddgo_read)
	return url_match_next.group(2)
#END next_page_ddgo

def next_page_bing(bing_read):
# searches HTML code for a link to next page of results
	url_match_next = re.search(r'', bing_read)
#END next_page_bing

def next_page_yahoo(yahoo_read):
# searches HTML code for a link to next page of results
	url_match_next = re.search(r'(<a id="pg-next" href=")('+link_criterion+')(">Next &gt;</a>)', yahoo_read)
	return url_match_next.group(2)
#END next_page_yahoo

###################  END of individual search engine link finders  ###################