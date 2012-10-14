#!/usr/bin/python
##
## Filename:	search.cgi
## Version:		4.2.2
##
import cgi
print "Content-type: text/html\n"

# variables to contain the locations of additional NECCESSARY files
engine_searcher = '.\\engine_searcher.py'
query_mod = '.\\query_mod.py'
result_mod = '.\\result_mod.py'

# import NECCESSARY functions from files
import engine_searcher	# allow the meta-search engine to search other search engines.
import query_mod		# edit the search enquiry so the meta-search engine may get better results.
import result_mod		# functions to add links to link_dict & displays them

# retrieves information sent from home/front page
form = cgi.FieldStorage()
search_entry = form.getvalue("search")		# stores the entry the user wishes to search for
text_edit = form.getvalue("process")		# stores a value from main page indicating if search entry will be edited
option = form.getvalue("adv_dis")			# stores a value that indicates how the user would like to view the results
#
total_count = form.getvalue("total")		# stores a value for the amount of pages that must be processde from the search engines
test = ''		# this variable is use for testing only. all related if statements are for testing


##### TESTING & ERROR CHECKING #####
option_list = ['all', 'col', 'bing', 'ddgo', 'yahoo']
if not search_entry:
	search_entry = 'HeLlO wOrLd!'
if option not in option_list:
	option = 'col'
if not total_count:		# if user doesn't specify a value, engine will produce up to results found
	total_count = 100
	max_page_count = 1
else:
	total_count = int(total_count)	# converts a numberical value from a string to an integer
	if total_count > 100:
		total_count = 100
		max_page_count = 10
	elif total_count <= 0:
		total_count = 1
		max_page_count = 1
	else:
		max_page_count = total_count/10
if test:	
	print '**************************end test**************************'
##### END TESTING & ERROR CHECKING#####

original_search_entry = search_entry		# stores original search entry in its unedited form

##### SEARCH ENTRY TEXT EDITOR #####
if text_edit:
# Edit search entry to try & improve search performance
	search_entry = query_mod.search_entry_editor(search_entry)
else:
# basic edit of search entry. REQUIRED!
	search_entry = query_mod.tokeniser(search_entry)
if test:	
	print '**************************entry edited**************************'
##### END SEARCH ENTRY TEXT EDITOR #####

# search engine search links
google_link = "http://www.google.ie/#hl=en&q=" + search_entry
ddgo_link = "http://duckduckgo.com/html/?q=" + search_entry
bing_link = "http://www.bing.com/search?q=" + search_entry
yahoo_link = "http://search.yahoo.com/search?p=" + search_entry


# external dictionary to hold:
link_dict = {}		# all links gathered from search engines
ddgo_dict = {}		# all links gathered from DuckDuckGo
bing_dict = {}		# all links gathered from Bing
yahoo_dict = {}		# all links gathered from Yahoo

##### RETRIEVE LINKS FROM SEARCH ENGINES #####
page_count = 0

while page_count < max_page_count:
	
# DuckDuckGo
	if (option == 'all' or option == 'col' or option == 'ddgo') and ddgo_link:
	# if statement done to cut down on unnecessary processing
		ddgo_read = engine_searcher.open_doc(ddgo_link)
		url_ddgo = engine_searcher.link_finder_ddgo(ddgo_read)
		ddgo_dict = result_mod.link_to_dict(ddgo_dict, url_ddgo, max_page_count, page_count)
		link_dict = result_mod.link_to_dict(link_dict, url_ddgo, max_page_count, page_count)
		ddgo_link = engine_searcher.next_page_ddgo(ddgo_read)
		if test:	
			print '**************************ddgo done**************************', page_count
	
# Bing
	if (option == 'all' or option == 'col' or option == 'bing') and bing_link:
	# if statement done to cut down on unnecessary processing
		bing_read = engine_searcher.open_doc(bing_link)
		url_bing = engine_searcher.link_finder_bing(bing_read)
		bing_dict = result_mod.link_to_dict(bing_dict, url_bing, max_page_count, page_count)
		link_dict = result_mod.link_to_dict(link_dict, url_bing, max_page_count, page_count)
		bing_link = engine_searcher.next_page_bing(search_entry, page_count)
		if test:	
			print '**************************bing done**************************', page_count
	
# Yahoo
	if (option == 'all' or option == 'col' or option == 'yahoo') and yahoo_link:
	# if statement done to cut down on unnecessary processing
		yahoo_read = engine_searcher.open_doc(yahoo_link)
		url_yahoo = engine_searcher.link_finder_yahoo(yahoo_read)
		yahoo_dict = result_mod.link_to_dict(yahoo_dict, url_yahoo, max_page_count, page_count)
		link_dict = result_mod.link_to_dict(link_dict, url_yahoo, max_page_count, page_count)
		yahoo_link = engine_searcher.next_page_yahoo(yahoo_read)
		if test:	
			print '**************************yahoo done**************************', page_count
	
	page_count = page_count + 1		# increment page number
if test:	
	print '**************************links retrieved**************************'
##### END RETRIEVE LINKS FROM SEARCH ENGINES #####

##### HTML CODE #####
##### PAGE HEAD #####
print """
<html><head>
<link rel="stylesheet" href="../css/results.css" />
<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />
<script type="text/javascript" src="js/alerts.js"></script>
"""
print '<title>'+original_search_entry+' : Meta-Search Results</title>'
print '</head>'
##### END PAGE HEAD #####
##### PAGE BODY #####
print '<body><div id="container">'
print '	<div id="re-search"></div>'
##### Search Results #####
print '	<div id="results">'
print '		<h2><u>Search Results</u></h2>'
print '		Your search<em><strong>', original_search_entry, '</strong></em>yielded these results:<br/>'
print '		<table border="0">'
result_mod.result_option(option, link_dict, ddgo_dict, bing_dict, yahoo_dict, total_count)
print '		</table>'
##### END Search Results #####
print '	</div>'
print '</div></body></html>'
##### END PAGE BODY #####
##### END HTML CODE #####