#!/usr/bin/python
##
## Filename:	search.cgi
## Version:		2.2
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

##### TESTING USE ONLY #####
if not search_entry:
	search_entry = 'HeLlO wOrLd!'
##### END TESTING #####

original_search_entry = search_entry		# stores original search entry in its unedited form

##### SEARCH ENTRY TEXT EDITOR #####
if text_edit:
# Edit search entry to try & improve search performance
	search_entry = query_mod.search_entry_editor(search_entry)
else:
# basic edit of search entry. REQUIRED!
	search_entry = query_mod.tokeniser(search_entry)
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
max_page_count = 3
while page_count < max_page_count:
	
# DuckDuckGo
	ddgo_read = engine_searcher.open_doc(ddgo_link)
	url_ddgo = engine_searcher.link_finder_ddgo(ddgo_read)
	ddgo_dict = result_mod.link_to_dict(ddgo_dict, url_ddgo, max_page_count, page_count)
	link_dict = result_mod.link_to_dict(link_dict, url_ddgo, max_page_count, page_count)
	ddgo_link = engine_searcher.next_page_ddgo(ddgo_read)
	
# Bing
	bing_read = engine_searcher.open_doc(bing_link)
	url_bing = engine_searcher.link_finder_bing(bing_read)
	bing_dict = result_mod.link_to_dict(bing_dict, url_bing, max_page_count, page_count)
	link_dict = result_mod.link_to_dict(link_dict, url_bing, max_page_count, page_count)
	bing_link = engine_searcher.next_page_bing(search_entry, page_count)
	
# Yahoo
	yahoo_read = engine_searcher.open_doc(yahoo_link)
	url_yahoo = engine_searcher.link_finder_yahoo(yahoo_read)
	yahoo_dict = result_mod.link_to_dict(yahoo_dict, url_yahoo, max_page_count, page_count)
	link_dict = result_mod.link_to_dict(link_dict, url_yahoo, max_page_count, page_count)
	yahoo_link = engine_searcher.next_page_yahoo(yahoo_read)
	
	page_count = page_count + 1		# increment page number
##### END RETRIEVE LINKS FROM SEARCH ENGINES #####

##### HTML CODE #####
##### PAGE HEAD #####
print """
<html><head>
<link rel="stylesheet" href="../css/results.css" />
<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />
<script type="text/javascript">
<!-- This script prompts a user to confirm that they wish to continue to a webpage that they have been warned that the webpage may bot exist -->
	var link_warn = "WARNING!!!\\nAn error occured when validating the page you are about to access. It may no longer be active.\\nClick OK to continue anyway or Cancel to remain.";
	function dead_link(){
		var answer = confirm(link_warn);
		if (answer){
			alert("You were warned!");
		}else{
			return false;
		}
	}
</script>
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
print '		Your search<em>', original_search_entry, '</em>yielded these results:<br/>'
print '		<table>'
result_mod.show_links(link_dict)
print '		</table>'
##### END Search Results #####
print '	</div>'
print '</div></body></html>'
##### END PAGE BODY #####
##### END HTML CODE #####