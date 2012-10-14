#!/usr/bin/python
##
## Filename: search.cgi
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
import result_mod		# 

# retrieves information sent from home/front page
form = cgi.FieldStorage()
search_entry = form.getvalue("search")		# stores the entry the user wishes to search for
text_edit = form.getvalue("process")		# stores a value from main page indicating if search entry will be edited

### TESTING ONLY ###
search_entry = 'HeLlO wOrLd!'
### END TESING ###


original_search_entry = search_entry				# stores original search entry in its unedited form
search_entry = query_mod.tokeniser(search_entry)	# basic edit of search entry. REQUIRED!

if text_edit:
# Edit search entry to try & improve search performance
	search_entry = query_mod.search_entry_editor(search_entry)

# search engine search links

google_link = "http://www.google.ie/#hl=en&q=" + search_entry
ddgo_link = "http://duckduckgo.com/html/?q=" + search_entry
bing_link = "http://www.bing.com/search?q=" + search_entry
yahoo_link = "http://search.yahoo.com/search?p=" + search_entry


link_dict = {}		# external dictionary to hold all links gathered from search engines


# DuckDuckGo
page_count = 0
while page_count < 10:
	ddgo_read = engine_searcher.open_doc(ddgo_link)
	url_ddgo = engine_searcher.link_finder_ddgo(ddgo_read)
	link_dict = result_mod.link_to_dict(link_dict, url_ddgo)
	next_page = engine_searcher.next_page_ddgo(ddgo_read)
	ddgo_link = "http://duckduckgo.com/html/?q=" + next_page
	page_count = page_count + 1

# Bing
bing_read = engine_searcher.open_doc(bing_link)
url_bing = engine_searcher.link_finder_bing(bing_read)
link_dict = result_mod.link_to_dict(link_dict, url_bing)

# Yahoo
yahoo_read = engine_searcher.open_doc(yahoo_link)
url_yahoo = engine_searcher.link_finder_yahoo(yahoo_read)
link_dict = result_mod.link_to_dict(link_dict, url_yahoo)

##### HTML CODE #####
print """<html><head>
<title>'+original_search_entry+' : Meta-Search Results</title>'
<link rel="stylesheet" href="../css/design.css" />'
<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />'
</head><body><h2><u>Search Results</u></h2>"""
# Search Results
print """Your search<em>', original_search_entry, '</em>yielded these results:<br/>'
<table>"""
result_mod.show_links(link_dict)
print '</table></body></html>'
##### END HTML CODE #####