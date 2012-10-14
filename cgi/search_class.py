#!/usr/bin/python
##
## Filename: search_class.cgi
##
import urllib
import re

def search_entry_editor(search_entry):
# Edit search entry to try & improve search performance
	fixed = []				# new list created to store edited search words
	fix = search_entry		# allows for easier code writing/editing
	fix = fix.lower()		# convert entry to lowercase
	fix = fix.split()		# splits all words

	for word in fix:
	# searches through each word & removes unwanted characters
		i = 0
		while i < len(word):
			if word[i] == ',' or word[i] == '?' or word[i] == "'" or word[i] == '"' or word[i] == '(' or word[i] == ')' or word[i] == '!':
				remove = word[i]
				word = word.replace(remove, '')
			else:
				i = i + 1
		fixed.append(word)

	fixed = '+'.join(fixed)		# rejoins words together with a '+'
	search_entry = fixed		# returns altered search entry to search_entry variable

	return search_entry
	
	
class search_cl:
	def __init__(self, search_entry):
	# class constructor that obtains urls to search for links
		self.link = search_entry
		
	def open_doc(self):
	# opens sites, retrieves site code, closes site & then returns site code
		site = urllib.urlopen(self.link)	# opens url to search through
		read_file = site.read()				# reads url (file) text
		site.close()						# done with url (file), so close it
		return read_file


def link_to_dict(dict, link_list):
# adds not already present links to a dictionary of links
	for link in link_list:
		if link not in dict:
			dict[link] = 1
		else:
			j = dict[link]
			j = j + 1
			dict[link] = j
	
	return dict

def link_trimmer(site_links):
# recieves the strings found on the sites & then trims them down to just the urls
	trimmed_links = []
	i=0		# counter
	
	for link in site_links:
		if link[1] not in trimmed_links and i < 10:		
			trimmed_links.append(link[1])
			i = i + 1
	return trimmed_links
			
def link_finder_ddgo(ddgo_read):
# searches through DuckDuckGo site for usable url links
	url_match_ddgo = re.findall(r'(<a rel="nofollow" href=")([\s$=;@?!%:\w./_()#-]+)(")', ddgo_read)
	ddgo_links = link_trimmer(url_match_ddgo)
	return ddgo_links

def link_finder_bing(bing_read):
# searches through Bing site for usable url links
	url_match_bing = re.findall(r'(<h3><a href=")([\s$=;@?!%:\w./_()#-]+)(" onmousedown="return)', bing_read)
	bing_links = link_trimmer(url_match_bing)
	return bing_links
	
def link_finder_yahoo(yahoo_read):
# searches through Yahoo site for usable links
	url_match_yahoo = re.findall(r'(<a class="yschttl spt" href=")([\s$=;@?!%:\w./_()#-]+)', yahoo_read)
	yahoo_links = link_trimmer(url_match_yahoo)
	return yahoo_links
	
def site_title(link):
# searches a site for a title
	site = urllib.urlopen(link)		# opens url to search through
	read_file = site.read()			# reads url (file) text
	site.close()					# done with url (file), so close it
	title = re.search(r'(<title>)(.+)(</title>)', read_file)
	if title:
		title = title.group(2)
	else:
		title = link
	if len(title) > 40:
		title = title[:40]
		title = title + ' . . .'
	return title
	
def show_links(dict):
# sorts links by highest amount retrieved & then prints them in that order
# solution was found here: http://stackoverflow.com/questions/3417760/how-to-sort-a-python-dict-by-value
	links = sorted(dict, key=dict.get, reverse=True)
	i = 1
	for url in links:
		print '<tr><td>', i, '</td>', '<td><a href="'+url+'"><strong>'+site_title(url)+'</strong></a></tr>'
		print '<tr><td>&nbsp;</td><td><span class="blue_link">'+url+'</span></td></tr>'
		i = i+1