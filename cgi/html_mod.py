#!/usr/bin/python
##
## Filename:	html_mod.py
## Version:		6.5.1
## This file prints the general HTML code found on all result pages to browser.
## This file contains functions that:
##		prints the HTML head section code to browser
##		prints search box and pre-processing option to browser
##		prints the display change option to the browser
##		prints current advanced settings to browser
##
import urllib
import re

def page_head(search_entry):
# prints the HTML head section code to browser
	print """
	<html><head>
		<link rel="stylesheet" href="../css/design.css" />
		<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />
		<script type="text/javascript" src="../js/alerts.js"></script>
	"""
	print '	<title>'+search_entry+' : Meta-Search Results</title>'
	print '</head>'

def search_area(search_entry, query_edit):
# prints search box and pre-processing option to browser
	print '<body><div id="container">'
	##### Re-SEARCH #####
	print """
	<div id="re-search">
	<form action="search.cgi" method="get" id="search-form" name="engine" onsubmit="return valid_search()">
	<table align="center" border="0" width="490px"><tr>
		<td colspan="2">
			<h1>Meta-Search Engine</h1>
		</td>
	</tr><tr>
	<!-- SEARCH -->
	"""
	print '	<td align="right" width="80%"><input type="text" name="search" id="search-box" value="'+search_entry+'" /></td>'
	print """
		<td>&nbsp;&nbsp;&nbsp;<input type="submit" id="search-button" value="Search!" onclick="return too_many()"/></td>
	</tr><tr>
		<td colspan="2" align="right">
			Pre-process Query: <input type="radio" name="process" value="bfsdjkfbsj" """,
	if query_edit:
		print 'checked',
	print ' />On&nbsp;&nbsp;'
	print '		<input type="radio" name="process" value="" ',
	if not query_edit:
		print 'checked',
	print ' />Off'
	print """	</td>
	<!-- END SEARCH -->
	</tr><tr>
		<td><a href="../feedback.php" target="_blank" title="Please Give Feedback!" class="related_search"><strong>Leave Feedback</strong></a></td>
	</tr></table>
	</div><br/>
	"""
	
def result_display_change():
# prints the display change option to the browser
	print """
	<div id="adv_sys"><table border="0" width="225px">
	<!-- ADVANCED SETTINGS -->
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
		</tr>
	"""	
				
def adv_sets(stat, agr, clus):
# prints current advanced settings to browser
	print """
		<tr>
			<td>&nbsp;</td>
		</tr><tr>
			<td><div id="adv_sets_off" style="display:block">
				<a href="#" title="Show/Hide Advanced Settings" onclick="showStuff('adv_sets_on');hideStuff('adv_sets_off')"><strong>Advanced Settings &#9660;</strong></a>
			</div><div id="adv_sets_on" style="display:none">
				<a href="#" title="Show/Hide Advanced Settings" onclick="showStuff('adv_sets_off');hideStuff('adv_sets_on')"><strong>Advanced Settings &#9650;</strong></a>
				<table border="0"><tr>
					<td align="right">Stats:&nbsp;&nbsp;&nbsp;</td>
					<td width="50%">
						<input type="radio" name="stat" value="on" """,
	if stat in ['on', 'error']:
		print 'checked',
	print ' />ON<br/>'
	print '					<input type="radio" name="stat" value="off" ',
	if stat not in ['on', 'error']:
		print 'checked',
	print ' />OFF'
	print """				</td>
				</tr><tr>
					<td align="right">Aggrigation:</td>
					<td>
						<input type="radio" name="agr" value="on" """,
	if agr == 'on':
		print 'checked',
	print ' />ON<br/>'
	print '					<input type="radio" name="agr" value="off" ',
	if agr != 'on':
		print 'checked',
	print '/>OFF'
	print """				</td>
				</tr><tr>
					<td align="right">Alternative Searches:</td>
					<td>
						<input type="radio" name="clus" value="yes" """,
	if clus == 'yes':
		print 'checked',
	print '	/>ON<br/>'
	print '					<input type="radio" name="clus" value="" '
	if clus !='yes':
		print 'checked',
	print ' />OFF'
	print """				</td>
				</tr></table>
			</div></td>
		</tr><tr>
			<td>&nbsp;</td>
		</tr>
	"""
	
def stat_display_error():
# prints an error message if there was an error while statistical analysis was being processes.
	print """
	<tr>
		<td>&nbsp;</td>
	</tr><tr>
	<td colspan="2"><!-- DISPLAY STATISTICS -->
		<div id="hide" style="display:block">
			<a href="#" title="Show/Hide Statistical Analysis" onclick="showStuff('show');hideStuff('hide')"><strong>Statistical Analysis &#9660;</strong></a>
		</div>
		<div id="show" style="display:none"><table>
		<tr><td>
			<a href="#" title="Show/Hide Statistical Analysis" onclick="showStuff('hide');hideStuff('show')"><strong>Statistical Analysis &#9650;</strong></a>
		</td></tr>
		<tr><td>&nbsp;</td></tr>
		<tr>
			<td>
				An error has occurred while trying to retrieving statistical data.<br/>
				Possible causes may include:<ul>
					<li>Daily Statistical Query limit has been reached</li>
					<li>Server difficulty communicating with Google</li>
				</ul>
			</td>
	</tr></table></div></td></tr>
	"""