#!/usr/bin/python
##
## Filename:	query_mod.py
## Version:		6.3
##
import urllib
import re

def search_entry_editor(entry):
# Edit search entry to try & improve search performance
	boolean_list = ['and', 'or', 'not']						# creates a list of boolean key words
	punct_list = [',', '?', '.', '!', '"', "'", ';', '`']	# creates a list of punctuation marks that would be removed from query
	fixed_entry = []										# new list created to store edited search words
	
	
	# SOURCE:	http://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
	edited_entry = [x.lower() for x in entry]	# convert entry to lowercase

	for word in edited_entry:
		i = 0
		while i < len(word):	# searches through each word & removes unwanted characters
			if word[i] in punct_list:
				remove = word[i]
				word = word.replace(remove, '')
			else:
				i = i + 1
		# checks to see if a word is in a list of boolean keywords.
		if word in boolean_list:
			word = word.upper()		# This makes the word UPPER case so that search engines will recognise them.
			
		fixed_entry.append(word)

	return fixed_entry

def cluster(entry):
	cluster_dict = {}
		
	file = open('stopwordList.txt')
	file_read = file.read()
	file.close()
	
	stop_word_list = re.findall(r'\w+', file_read)
		
	for cluster_word in entry:
		related = []	
		if cluster_word not in stop_word_list:
			thesaurus = 'http://www.merriam-webster.com/thesaurus/' + cluster_word
			site = urllib.urlopen(thesaurus)
			site_code = site.read()
			site.close()		
			
			syn_links = re.findall(r'(<div><strong>Synonyms</strong>)(.+?)(</a></div>)', site_code)
			if syn_links:
				for div in syn_links:
					syn_words = re.findall(r'(<a href=".+?">)(\w+)(<)', div[1])
					for word in syn_words:
						related.append(word[1])
			
			rel_links = re.findall(r'(<div><strong>Related Words</strong>)(.+?)(/a></div>)', site_code)
			if rel_links:
				for div in rel_links:
					rel_words = re.findall(r'(<a href=".+?">)(\w+)(<)', div[1])
					for word in rel_words:
						related.append(word[1])
		
			cluster_dict[cluster_word] = related
			
	return cluster_dict
		
def cluster_display(cluster_dict):
	cluster_keys = cluster_dict.keys()
	alt_search = 'http://csserver.ucd.ie/~10972081/cgi/search.cgi?search='
	
	print """
	<!--- cluster -->
	<tr id="cluster_results"><td>
	"""
	
	for word in cluster_keys:
		related_words = cluster_dict[word]
		
		if related_words:
			print '	<table border="0"><tr>'
			print '		<td colspan="3"><strong>Alternative search ideas for : <u><em>'+word+'</em></u></strong></td>'
			print '	</tr><tr id="rel_'+word+'1" style="display:block">'
			print '		<td><a href="#" title="Show more alternative searches" onclick="hideStuff(\'rel_'+word+'1\');showStuff(\'rel_'+word+'_more1\');showStuff(\'rel_'+word+'_more2\');showStuff(\'rel_'+word+'\')">Show...</a></td>'
			i=3
			j=1
			for alt_word in related_words[0:12]:
				if i<3:
					i=i+1
				else:
					i=1
					print '	</tr><tr id="rel_'+word+'_more'+str(j)+'" style="display:none">'
					j=j+1
				print '		<td><a href="'+alt_search+alt_word+'" class="related_search">'+alt_word+'</a></td>'
				if ((j%3) == 0) and (i==3):
					print '	</tr><tr id="rel_'+word+'2" style="display:none">'
					print '		<td><a href="#" title="Show more alternative searches" onclick="hideStuff(\'rel_'+word+'2\');showStuff(\'rel_'+word+'_more3\');showStuff(\'rel_'+word+'_more4\')">More...</a></td>'
			print '</tr></table><br/>'
	print """	</td></tr>
		<tr><td>&nbsp;</td></tr>
	<!-- END cluster -->
	"""