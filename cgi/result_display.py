#!/usr/bin/python
##
## Filename:	result_display.py
## Version:		3.0
##
result_mod = './/result_mod.py'

import urllib
import re
import result_mod

def column_results(ddgo_dict, bing_dict, yahoo_dict):
	print """
	<tr>
		<td colspan="6">&nbsp;</td>
	</tr><tr>
		<td><strong>DuckDuckGo Resuls</strong></td>
		<td><strong>Bing Resuls</strong></td>
		<td><strong>Yahoo Resuls</strong></td>
	</tr><tr>
		<td colspan="6"><hr/></td>
	</tr><tr><td valign="top"><table border="0">
	"""
	result_mod.show_links(ddgo_dict)
	print '</table></td><td valign="top"><table border = "0">'
	result_mod.show_links(bing_dict)
	print '</table></td><td valign="top"><table border="0">'
	result_mod.show_links(yahoo_dict)
	print '</table></td></tr>'
		
def results(dict):
	result_mod.show_links(dict)
	
def result_option(option, dict, ddgo_dict, bing_dict, yahoo_dict):
	if option == 'all':
		results(dict)
	elif option == 'col':
		column_results(ddgo_dict, bing_dict, yahoo_dict)
	elif option == 'yahoo':
		print 'Yahoo! Results'
		results(yahoo_dict)
	elif option == 'bing':
		print 'Bing Results'
		results(bing_dict)
	elif option == 'ddgo':
		print 'DuckDuckGo Results'
		results(ddgo_dict)