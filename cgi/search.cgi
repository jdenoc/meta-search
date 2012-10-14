#!/usr/bin/python
##
## Filename:	search.cgi
## Version:		6.1
##
import cgi
print "Content-type: text/html\n"

# variables to contain the locations of additional NECCESSARY files
engine_searcher = '.\\engine_searcher.py'
query_mod = '.\\query_mod.py'
result_mod = '.\\result_mod.py'
stats_mod = '.\\stats_mod.py'

# import NECCESSARY functions from files
import engine_searcher	# allow the meta-search engine to search other search engines.
import query_mod		# edit the search enquiry so the meta-search engine may get better results.
import result_mod		# functions to add links to link_dict & displays them
import stats_mod		# used to find statistical comparisons between this engine & google

# retrieves information sent from home/front page
form = cgi.FieldStorage()
search_entry = form.getvalue("search")		# stores the entry the user wishes to search for
text_edit = form.getvalue("process")		# stores a value from main page indicating if search entry will be edited
option = form.getvalue("adv_dis")			# stores a value that indicates how the user would like to view the results
stat = form.getvalue("stat")
agr = form.getvalue("agr")
total_count = form.getvalue("total")		# stores a value for the amount of pages that must be processde from the search engines
test = ''									# this variable is use for testing only. all related if statements are for testing

##### TESTING & ERROR CHECKING #####
option_list = ['all', 'col', 'bing', 'ddgo', 'yahoo']
if not search_entry:
	search_entry = 'HeLlO wOrLd!'
if option not in option_list:
	option = 'all'
if not total_count:		# if user doesn't specify a value, engine will produce all results found
	total_count = 30
	max_page_count = 1
else:
	total_count = int(total_count)	# converts a numberical value from a string to an integer
	if total_count > 100:
		total_count = 100
		max_page_count = 10
	elif total_count <= 0:
		total_count = 30
		max_page_count = 1
	else:
		max_page_count = total_count/10
if not agr:
	agr = 'on'		
if test:
	print '**************************end error check**************************'
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
ddgo_link = "http://duckduckgo.com/html/?q=" + search_entry
bing_link = "http://www.bing.com/search?q=" + search_entry
yahoo_link = "http://search.yahoo.com/search?p=" + search_entry


# external dictionary to hold:
link_dict = {}		# all links gathered from search engines
ddgo_dict = {}		# all links gathered from DuckDuckGo
bing_dict = {}		# all links gathered from Bing
yahoo_dict = {}		# all links gathered from Yahoo
google_dict = {}	# all links gathered from google

##### RETRIEVE LINKS FROM SEARCH ENGINES #####
page_count = 0

while page_count < max_page_count:
	
# DuckDuckGo
	if (option == 'all' or option == 'col' or option == 'ddgo') and ddgo_link:
	# if statement done to cut down on unnecessary processing
		ddgo_read = engine_searcher.open_doc(ddgo_link)
		url_ddgo = engine_searcher.link_finder_ddgo(ddgo_read)
		ddgo_dict = result_mod.link_to_dict(ddgo_dict, url_ddgo, max_page_count, page_count, agr)
		link_dict = result_mod.link_to_dict(link_dict, url_ddgo, max_page_count, page_count, agr)
		ddgo_link = engine_searcher.next_page_ddgo(ddgo_read)
		if test:	
			print '**************************ddgo done**************************', page_count
	
# Bing
	if (option == 'all' or option == 'col' or option == 'bing') and bing_link:
	# if statement done to cut down on unnecessary processing
		bing_read = engine_searcher.open_doc(bing_link)
		url_bing = engine_searcher.link_finder_bing(bing_read)
		bing_dict = result_mod.link_to_dict(bing_dict, url_bing, max_page_count, page_count, agr)
		link_dict = result_mod.link_to_dict(link_dict, url_bing, max_page_count, page_count, agr)
		bing_link = engine_searcher.next_page_bing(search_entry, page_count)
		if test:	
			print '**************************bing done**************************', page_count
	
# Yahoo
	if (option == 'all' or option == 'col' or option == 'yahoo') and yahoo_link:
	# if statement done to cut down on unnecessary processing
		yahoo_read = engine_searcher.open_doc(yahoo_link)
		url_yahoo = engine_searcher.link_finder_yahoo(yahoo_read)
		yahoo_dict = result_mod.link_to_dict(yahoo_dict, url_yahoo, max_page_count, page_count, agr)
		link_dict = result_mod.link_to_dict(link_dict, url_yahoo, max_page_count, page_count, agr)
		yahoo_link = engine_searcher.next_page_yahoo(yahoo_read)
		if test:	
			print '**************************yahoo done**************************', page_count
	
	page_count = page_count + 1		# increment page number
if test:	
	print '**************************links retrieved**************************'
##### END RETRIEVE LINKS FROM SEARCH ENGINES #####

##### Google Statistical comparison #####
if stat == 'on' and (option == 'all' or option == 'col'):
	try:		# if there are any errors between here and 'except:', then 'except:' is run and 'stat' variable is given a value of 'off'
# Google results
		google_dict = stats_mod.google_api(search_entry, total_count)
		if test:	
			print '**************************google done**************************'

# Precision Scores
		Prec_meta = stats_mod.Precision(link_dict.keys(), google_dict.keys())
		Prec_bing = stats_mod.Precision(bing_dict.keys(), ddgo_dict.keys())
		Prec_yahoo = stats_mod.Precision(yahoo_dict.keys(), google_dict.keys())
		Prec_ddgo = stats_mod.Precision(ddgo_dict.keys(), google_dict.keys())
		Precision_Scores = ['meta:'+str(Prec_meta), 'bing:'+str(Prec_bing), 'yahoo:'+str(Prec_yahoo), 'duckDuckGo:'+str(Prec_ddgo)]
		if test:
			print '**************************Precision done**************************'
		
# Recall Scores
		rec_meta = stats_mod.Recall(link_dict.keys(), google_dict.keys())
		rec_bing = stats_mod.Recall(bing_dict.keys(), google_dict.keys())
		rec_yahoo = stats_mod.Recall(yahoo_dict.keys(), google_dict.keys())
		rec_ddgo = stats_mod.Recall(ddgo_dict.keys(), google_dict.keys())
		Recall_Scores = ['meta:'+str(rec_meta), 'bing:'+str(rec_bing), 'yahoo:'+str(rec_yahoo), 'duckduckgo:'+str(rec_ddgo)]
		if test:
			print '**************************Recall done**************************'
		
# Average Precision Score
		AP_score_ddgo = stats_mod.Average_Precision(ddgo_dict, google_dict)
		AP_score_bing = stats_mod.Average_Precision(bing_dict, google_dict)
		AP_score_meta = stats_mod.Average_Precision(link_dict, google_dict)
		AP_score_yahoo = stats_mod.Average_Precision(yahoo_dict, google_dict)
		AP_scores = ['meta:'+str(AP_score_meta), 'bing:'+str(AP_score_bing), 'yahoo:'+str(AP_score_yahoo), 'duckduckgo:'+str(AP_score_ddgo)]
		if test:	
			print '**************************Average Precision done**************************'
	except:
		stat = 'off'
if test:	
	print '**************************stats done**************************'
##### END Google Statistical comparison #####

##### HTML CODE #####
##### PAGE HEAD #####
print """
<html><head>
<link rel="stylesheet" href="../css/design.css" />
<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />
<script type="text/javascript" src="../js/alerts.js"></script>
"""
print '<title>'+original_search_entry+' : Meta-Search Results</title>'
print '</head>'
##### END PAGE HEAD #####
##### PAGE BODY #####
print '<body><div id="container">'
##### Re-SEARCH & ADVANCED SETTINGS #####
print """
<div id="re-search">
<form action="search.cgi" method="get" id="search-form" name="engine" onsubmit="valid_search();return too_many()">
<table align="center" border="0" width="490px"><tr>
	<td colspan="2">
		<h1>Meta-Search Engine</h1>
	</td>
</tr><tr>
<!-- SEARCH -->
"""
print '	<td align="right" width="80%"><input type="text" name="search" id="search-box" value="'+original_search_entry+'" /></td>'
print """
	<td>&nbsp;&nbsp;&nbsp;<input type="submit" id="search-button" value="Search!" /></td>
</tr><tr>
	<td colspan="2" align="right">
		Pre-process Query: <input type="radio" name="process" value="bfsdjkfbsj" checked />On&nbsp;&nbsp;
		<input type="radio" name="process" value="" />Off
	</td>
<!-- END SEARCH -->
</tr></table>
</div><br/>
<div id="adv_sys"><table border="0" width="225px">
<!-- ADVANCED SETTINGS -->
	<tr><td align="center" colspan="2"><strong><u>Display</u></strong></td></tr>
	<tr><td>&nbsp;</td></tr>
	<tr>
		<td>Standard: </td>

		<td align="center"><input type="radio" name="adv_dis" value="all" onclick="change_display()" /></td>
	</tr><tr>
		<td>Columned: </td>
		<td align="center"><input type="radio" name="adv_dis" value="col" onclick="change_display()" /></td>
	</tr><tr>
		<td>Bing Results Only: </td>
		<td align="center"><input type="radio" name="adv_dis" value="bing" onclick="change_display()" /></td>
	</tr><tr>
		<td>DuckDuckGo Results Only: </td>
		<td align="center"><input type="radio" name="adv_dis" value="ddgo" onclick="change_display()" /></td>
	</tr><tr>
		<td>Yahoo! Results Only: </td>
		<td align="center"><input type="radio" name="adv_dis" value="yahoo" onclick="change_display()" /></td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td align="center" colspan="2"><strong>Maximum Results: </strong></td>
	<tr></tr>
		<td align="center" colspan="2"><input type="text" name="total" /></td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td><div id="adv_sets_off" style="display:block">
			<a href="#" title="Show/Hide Advanced Settings" onclick="showStuff('adv_sets_on');hideStuff('adv_sets_off')"><strong>Advanced Settings &#9660;</strong></a>
		</div><div id="adv_sets_on" style="display:none">
			<a href="#" title="Show/Hide Advanced Settings" onclick="showStuff('adv_sets_off');hideStuff('adv_sets_on')"><strong>Advanced Settings &#9650;</strong></a>
			<table><tr>
				<td align="right">Stats:&nbsp;&nbsp;&nbsp;</td>
				<td>
					<input type="radio" name="stat" value="on" />ON<br/>
					<input type="radio" name="stat" value="off" checked />OFF
				</td>
			</tr><tr>
				<td align="right">Aggrigation:</td>
				<td>
					<input type="radio" name="agr" value="on" checked />ON<br/>
					<input type="radio" name="agr" value="off" />OFF
				</td>
			</tr></table>
		</div></td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr>
"""
if stat == 'on':
	stats_mod.stat_display(option, Precision_Scores, Recall_Scores, AP_scores)
print '<!-- END ADVANCED SETTINGS -->'
print '</table></form></div>'
##### END Re-SEARCH & ADVANCED SETTINGS #####
##### Search Results #####
print '	<div id="results">'
print '		<h2><u>Search Results</u></h2>'
print '		Your search<em><strong>', original_search_entry, '</strong></em>yielded these results:<br/><br/>'
print '		<div id="scroll-area"><table border="0">'
result_mod.result_option(option, link_dict, ddgo_dict, bing_dict, yahoo_dict, total_count)
print '		</table></div>'
##### END Search Results #####
print '	</div>'
print '</div></body></html>'
##### END PAGE BODY #####
##### END HTML CODE #####
