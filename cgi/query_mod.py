#!/usr/bin/python
##
## Filename:	query_mod.py
## Version:		6.5.1
## This file processes the query and produces clustering (alterantive search) results.
## This file contains functions that:
##		edit the search entry to improve search performance
##		obtains the search query & then finds related words & synonyms that could potentially be searched by user to get better search results
##		displays the clustering words so they can searched
##
import urllib
import re

def search_entry_editor(entry):
# Edit search entry to try & improve search performance
	boolean_list = ['and', 'or', 'not']							# creates a list of boolean key words
	punct_list = [',', '?', '.', '!', '"', "'", ';', '`', '#']	# creates a list of punctuation marks that would be removed from query
	fixed_entry = []											# new list created to store edited search words
	
	
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
# obtains the search query & then finds related words & synonyms that could potentially be searched by user to get better search results
# results are obtained from: http://www.merriam-webster.com/thesaurus/
	cluster_dict = {}
		
	file = open('stopwordList.txt')		# opens file that contains a list of stop-words
	file_read = file.read()				# extracts text
	file.close()						# closes file
	
	stop_word_list = re.findall(r'\w+', file_read)	# obtains a list of stop-words
		
	for cluster_word in entry:
		related = []		# list to store related words & synonyms
		if cluster_word not in stop_word_list:	# makes sure each word un the query is not a stop-word
			thesaurus = 'http://www.merriam-webster.com/thesaurus/' + cluster_word
			site = urllib.urlopen(thesaurus)
			site_code = site.read()
			site.close()		
			
			# retrieves synomyms
			syn_links = re.findall(r'(<div><strong>Synonyms</strong>)(.+?)(</a></div>)', site_code)
			if syn_links:		# makes sure variable doesn't have NULL/NONE value
				for div in syn_links:
					syn_words = re.findall(r'(<a href=".+?">)(\w+)(<)', div[1])
					for word in syn_words:
						related.append(word[1])
			
			# retrieves related words
			rel_links = re.findall(r'(<div><strong>Related Words</strong>)(.+?)(/a></div>)', site_code)
			if rel_links:		# makes sure variable doesn't have NULL/NONE value
				for div in rel_links:
					rel_words = re.findall(r'(<a href=".+?">)(\w+)(<)', div[1])
					for word in rel_words:
						related.append(word[1])
		
			cluster_dict[cluster_word] = related
			
	return cluster_dict
		
def cluster_display(cluster_dict):
# displays the words obtained for the clustering
	cluster_keys = cluster_dict.keys()
	alt_search = 'http://csserver.ucd.ie/~10972081/cgi/search.cgi?search='
	
	print """
	<!--- cluster -->
	<tr id="cluster_results"><td>
	"""
	
	for word in cluster_keys:
		related_words = cluster_dict[word]
		
		if related_words:		# makes sure variable doesn't have NULL/NONE value
			print '	<table border="0"><tr>'
			print '		<td colspan="3"><strong>Alternative search ideas for : <u><em>'+word+'</em></u></strong></td>'
			print '	</tr><tr id="rel_'+word+'1" style="display:block">'
			print '		<td><a href="#" title="Show more alternative searches" onclick="hideStuff(\'rel_'+word+'1\');showStuff(\'rel_'+word+'_more1\');showStuff(\'rel_'+word+'_more2\');showStuff(\'rel_'+word+'\')">Show...</a></td>'
			i=3
			j=1
			for alt_word in related_words[0:12]:	# only goes up to first 12 related words, otherwise the user would be overwhelmed by the choice, and too much space on the results page would be taken up
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