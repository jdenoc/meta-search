#!/usr/bin/python
##
## Filename:	html_mod.py
## Version:		6.3
##
import urllib
import re

def page_head(original_search_entry):
# 	
	print """
	<html><head>
		<link rel="stylesheet" href="../css/design.css" />
		<link rel="icon" href="../imgs/icons/meta.ico" type="image/x-icon" />
		<script type="text/javascript" src="../js/alerts.js"></script>
	"""
	print '	<title>'+original_search_entry+' : Meta-Search Results</title>'
	print '</head>'

def search_area(original_search_entry):
	print '<body><div id="container">'
	##### Re-SEARCH #####
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
	"""
	
def result_display_change():
##### ADVANCED SETTINGS #####
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
				
def adv_sets():		
	print """
		<tr>
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
				</tr><tr>
					<td align="right">Related Searches:</td>
					<td>
						<input type="radio" name="clus" value="yes" checked />ON<br/>
						<input type="radio" name="clus" value="" />OFF
					</td>
				</tr></table>
			</div></td>
		</tr><tr>
			<td>&nbsp;</td>
		</tr>
	"""