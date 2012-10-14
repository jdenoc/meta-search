#!/usr/bin/python
##
## Filename: search.cgi
##
import cgi
print "Content-type: text/html\n"
search_class = '.\\search_class.py'
import search_class

# retrieves information sent from front page
form = cgi.FieldStorage()
search_entry = form.getvalue("search")			# stores the entry the user wishes to search for
text_edit = form.getvalue("process")			# stores a value from main page indicating if search entry will be edited

original_search_entry = search_entry			# stores original search entry in its unedited form

if text_edit:
# Edit search entry to try & improve search performance
	search_entry = search_class.search_entry_editor(search_entry)

# search engine search links
google_link = "http://www.google.ie/#hl=en&q=" + search_entry
ddgo_link = "http://duckduckgo.com/html/?q=" + search_entry
bing_link = "http://www.bing.com/search?q=" + search_entry
yahoo_link = "http://search.yahoo.com/search?p=" + search_entry

link_dict = {}		# external dictionary to hold all links gathered from search engines

# site class objects
ddgo = search_class.search_cl(ddgo_link)
bing = search_class.search_cl(bing_link)
yahoo = search_class.search_cl(yahoo_link)

# DuckDuckGo 
ddgo_read = ddgo.open_doc()
url_ddgo = search_class.link_finder_ddgo(ddgo_read)
link_dict = search_class.link_to_dict(link_dict, url_ddgo)

# Bing
bing_read = bing.open_doc()
url_bing = search_class.link_finder_bing(bing_read)
link_dict = search_class.link_to_dict(link_dict, url_bing)

# Yahoo
yahoo_read = yahoo.open_doc()
url_yahoo = search_class.link_finder_yahoo(yahoo_read)
link_dict = search_class.link_to_dict(link_dict, url_yahoo)

##### HTML CODE #####
print """<html><head>
<title>'+original_search_entry+' : Meta-Search Results</title>'
<link rel="stylesheet" href="../css/design.css" />'
<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />'
</head><body><h2><u>Search Results</u></h2>"""
# Search Results
print """Your search<em>', original_search_entry, '</em>yielded these results:<br/>'
<table>"""
search_class.show_links(link_dict)
print '</table></body></html>'
##### END HTML CODE #####