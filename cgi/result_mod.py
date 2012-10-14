#!/usr/bin/python
##
## Filename:	result_mod.py
## Version:		3.1
##
import urllib
import re

def link_to_dict(dict, link_list, weight, weight_limiter):
# adds not already present links to a dictionary of links
	for link in link_list:
		if link not in dict:
			dict[link] = 1*(weight-weight_limiter)
		else:
			j = dict[link]
			j = j + 1
			dict[link] = j
	
	return dict
	
def link_checker(link):
# checks to make sure the link provided is valid
	try:
		site = urllib.urlopen(link)		# opens url to search through
		read_file = site.read()			# reads url (file) text
		site.close()					# done with url (file), so close it

		href = link+'"><strong>'+site_title(read_file)+'</strong>'
	
	except:
		href = link+'" onclick="return dead_link();"><strong> 404 ERROR </strong>'
				
	return href
	
def site_title(read_file):
# searches a site for a title or heading
	title_match1 = re.search(r'(<title.*>)(.+)(</title>)', read_file, re.DOTALL)
	title_match2 = re.search(r'(<TITLE.*>)(.+)(</TITLE>)', read_file, re.DOTALL)
	h1_match1 = re.search(r'(<h1.*>)(.+)(/h1>)', read_file)
	h1_match2 = re.search(r'(<H1.*>)(.+)(/H1>)', read_file)
		
	if title_match1:
		heading = title_match1.group(2)
	elif h1_match1:
		heading = h1_match1.group(2)
	elif title_match2:
		heading = title_match2.group(2)
	elif h1_match2:
		heading = h1_match2.group(2)
	else:
		heading = link
		
	if len(heading) > 30:
		heading = heading[:30]
		heading = heading + ' . . .'
		
	return heading
	
def show_links(dict):
# sorts links by highest amount retrieved & then prints them in that order
# solution was found here: http://stackoverflow.com/questions/3417760/how-to-sort-a-python-dict-by-value
	links = sorted(dict, key=dict.get, reverse=True)
	i = 1
	for url in links:
		print '<tr><td>', i, '</td>', '<td><a href="'+link_checker(url)+'</a></td></tr>'
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