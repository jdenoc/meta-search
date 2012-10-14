#!/usr/bin/python
##
## Filename:	result_mod.py
## Version:		2.0
##
import urllib
import re

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