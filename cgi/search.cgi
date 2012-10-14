#!/usr/bin/python
##
## Filename:	search.cgi
## Version:		2.0
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
if not search_entry:
	search_entry = 'HeLlO wOrLd!'
### END TESTING ###

original_search_entry = search_entry		# stores original search entry in its unedited form

if text_edit:
# Edit search entry to try & improve search performance
	search_entry = query_mod.search_entry_editor(search_entry)
else:
# basic edit of search entry. REQUIRED!
	search_entry = query_mod.tokeniser(search_entry)

# search engine search links
google_link = "http://www.google.ie/#hl=en&q=" + search_entry
ddgo_link = "http://duckduckgo.com/html/?q=" + search_entry
bing_link = "http://www.bing.com/search?q=" + search_entry
yahoo_link = "http://search.yahoo.com/search?p=" + search_entry


link_dict = {}		# external dictionary to hold all links gathered from search engines


page_count = 0
while page_count < 3:
	
# DuckDuckGo
	ddgo_read = engine_searcher.open_doc(ddgo_link)
	url_ddgo = engine_searcher.link_finder_ddgo(ddgo_read)
	link_dict = result_mod.link_to_dict(link_dict, url_ddgo)
	next_page = engine_searcher.next_page_ddgo(ddgo_read)
	ddgo_link = "http://duckduckgo.com/html/?q=" + next_page

# Bing
	bing_read = engine_searcher.open_doc(bing_link)
	url_bing = engine_searcher.link_finder_bing(bing_read)
	link_dict = result_mod.link_to_dict(link_dict, url_bing)
	next_page = engine_searcher.next_page_bing(search_entry, page_count)
	bing_link = "http://www.bing.com/search?q=" + next_page

# Yahoo
	yahoo_read = engine_searcher.open_doc(yahoo_link)
	url_yahoo = engine_searcher.link_finder_yahoo(yahoo_read)
	link_dict = result_mod.link_to_dict(link_dict, url_yahoo)
	yahoo_link = engine_searcher.next_page_yahoo(yahoo_read)
	
	page_count = page_count + 1

##### HTML CODE #####
print '<html><head>'
print '<title>'+original_search_entry+' : Meta-Search Results</title>'
print '<link rel="stylesheet" href="../css/design.css" />'
print '<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />'
print '</head><body><h2><u>Search Results</u></h2>'
# Search Results
print 'Your search<em>', original_search_entry, '</em>yielded these results:<br/>'
print '<table>'
result_mod.show_links(link_dict)
print '</table></body></html>'
# END Search Results
##### END HTML CODE #####