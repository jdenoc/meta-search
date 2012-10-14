#!/usr/bin/python
##
## Filename:	result_mod.py
## Version:		4.1
##
import urllib
import re

def link_to_dict(dict, link_list, weight, weight_limiter):
# adds not already present links to a dictionary of links
	for link_set in link_list:
		link = link_set[0]
		if link_set[0] not in dict:
			score = 1*(weight-weight_limiter)
			dict[link] = (score, link_set[1])
		else:
			items = dict[link]
			score = items[0]
			score = score + 1
			dict[link] = (score, items[1])
	
	return dict

def show_links(dict):
# splits dictionary into two separate dictionarys. One for links & rank, & the other for links & title
# sorts links by highest score/weight & then prints them in that order
# prints a title that is related to that link
	link_dict = {}
	title_dict = {}
	
	for url in dict.keys():
		set = dict[url]
		title = set[1]
		score = set[0]
		link_dict[url] = score
		title_dict[url] = title
	
	links = sorted(link_dict, key=link_dict.get, reverse=True)	# Code Source: http://stackoverflow.com/questions/3417760/how-to-sort-a-python-dict-by-value
	i = 1
	for url in links:
		print '<tr><td>', i, '</td>', '<td><a href="'+url+'">'+title_dict[url]+'</a></td></tr>'
		print '<tr><td>&nbsp;</td><td><span class="blue_link">'+url+'</span></td></tr>'
		i = i+1
		
def column_results(ddgo_dict, bing_dict, yahoo_dict):
	print """
	<tr>
		<td colspan="6">&nbsp;</td>
	</tr><tr>
		<td><strong>DuckDuckGo Results</strong></td>
		<td><strong>Bing Results</strong></td>
		<td><strong>Yahoo Results</strong></td>
	</tr><tr>
		<td colspan="6"><hr/></td>
	</tr><tr><td valign="top"><table border="0">
	"""
	show_links(ddgo_dict)
	print '</table></td><td valign="top"><table border = "0">'
	show_links(bing_dict)
	print '</table></td><td valign="top"><table border="0">'
	show_links(yahoo_dict)
	print '</table></td></tr>'
		
def result_option(option, dict, ddgo_dict, bing_dict, yahoo_dict):
	if option == 'all':
		show_links(dict)
	elif option == 'col':
		column_results(ddgo_dict, bing_dict, yahoo_dict)
	elif option == 'yahoo':
		print 'Yahoo! Results'
		show_links(yahoo_dict)
	elif option == 'bing':
		print 'Bing Results'
		show_links(bing_dict)
	elif option == 'ddgo':
		print 'DuckDuckGo Results'
		show_links(ddgo_dict)