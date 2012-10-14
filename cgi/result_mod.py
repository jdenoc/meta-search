#!/usr/bin/python
##
## Filename:	result_mod.py
## Version:		5.1
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

def show_links(dict, total_count):
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
	
	links = sorted(link_dict, key=link_dict.get, reverse=True)		# Code Source: http://stackoverflow.com/questions/3417760/how-to-sort-a-python-dict-by-value
	i = 1
	
	if links:
		for url in links:
			if i <= total_count:
				print '<tr><td>', i, '</td>', '<td><a href="'+url+'" target="_blank">'+title_dict[url]+'</a></td></tr>'
				print '<tr><td>&nbsp;</td><td><span class="blue_link">'+url+'</span></td></tr>'
			i = i+1
	else:
		print '<tr><td>&nbsp;</td></tr>'
		print '<tr><td colspan="2" align="center"><strong>NO RESULTS FOUND!</strong></td></tr>'
		print '<tr><td>&nbsp;</td></tr>'
		
def column_results(ddgo_dict, bing_dict, yahoo_dict, total_count):
	print """
	<tr>
		<td colspan="6">&nbsp;</td>
	</tr><tr>
		<td width="33%"><strong>DuckDuckGo Results</strong></td>
		<td width="33%"><strong>Bing Results</strong></td>
		<td width="33%"><strong>Yahoo Results</strong></td>
	</tr><tr>
		<td colspan="6"><hr/></td>
	</tr><tr><td valign="top"><table border="0" class="results">
	"""
	show_links(ddgo_dict, total_count)
	print '</table></td><td valign="top"><table border = "0" class="results">'
	show_links(bing_dict, total_count)
	print '</table></td><td valign="top"><table border="0" class="results">'
	show_links(yahoo_dict, total_count)
	print '</table></td></tr>'
		
def result_option(option, dict, ddgo_dict, bing_dict, yahoo_dict, total_count):
	if option == 'all':
		show_links(dict, total_count)
	elif option == 'col':
		column_results(ddgo_dict, bing_dict, yahoo_dict, total_count)
	elif option == 'yahoo':
		print 'Yahoo! Results'
		show_links(yahoo_dict, total_count)
	elif option == 'bing':
		print 'Bing Results'
		show_links(bing_dict, total_count)
	elif option == 'ddgo':
		print 'DuckDuckGo Results'
		show_links(ddgo_dict, total_count)