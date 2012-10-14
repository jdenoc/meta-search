# TESTING SCRIPT

stats_mod = '.\\stats_mod.py'
import stats_mod		# used to find statistical comparisons between this engine & google
import re
import urllib

search_entry = 'hello'
stage = 'y'		# 'd' = ddgo link, 'y' = yahoo link, 'b' = bing link

#link = "http://duckduckgo.com/html/?q=" + search_entry
#link = "http://www.bing.com/search?q=" + search_entry
link = "http://search.yahoo.com/search?p=" + search_entry



site = urllib.urlopen(link)		# opens url to search through
read_file = site.read()			# reads url (file) text
site.close()					# done with url (file), so close it

link_criterion = "[+',\s$=;@?!%&:\w./_()#-]+"

if stage == 'd':
	url_match = re.findall(r'(<a rel="nofollow" class="l le" href=")('+link_criterion+')(">)(.+)(</a>)', read_file)
elif stage == 'b':
	url_match = re.findall(r'(<h3><a href=")('+link_criterion+')(" onmousedown="return si_T.+?">)(.+?)(</a>)', read_file)	# (.+?)		This indicates 1 or more of any character, but in a non-greedy form
elif stage == 'y':
	url_match = re.findall(r'(<a class="yschttl spt" href=")('+link_criterion+')(" data-.+?>)(.+?)(</a>)', read_file)
	
site_links = []
	
for link in url_match:
	url = link[1]
	title = link[3]
	site_links.append((url, title))


dict1 = {}
for link_set in site_links:
	link = link_set[0]
	if link not in dict1:
		score = 1
		dict1[link] = (score, link_set[1])
	else:
		items = dict[link]
		score = items[0]
		score = score + 1
		dict1[link] = (score, items[1])

google_dict = stats_mod.google_api(search_entry, 30)


Precision = stats_mod.Precision(dict1.keys(), google_dict.keys())
Recall = stats_mod.Recall(dict1.keys(), google_dict.keys())

AP_score = stats_mod.Average_Precision(dict1, google_dict)

print ' PRECSION:   ', Precision
print ' RECALL:     ', Recall
print ' AVERAGE PRECISION:   ', AP_score
