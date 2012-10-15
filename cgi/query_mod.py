#!/usr/bin/python
##
## Filename:	query_mod.py
## Version:		6.2
##
import urllib
import re

def tokeniser(search_entry):
# Basic search entry edit
# Tokenises the words in search entry by replacing ' ' with '+' 					
	fix = search_entry		# allows for easier code writing/editing
	fix = fix.split()		# splits all words
	fix = '+'.join(fix)		# rejoins words together with a '+'
	search_entry = fix		# returns altered search entry to search_entry variable

	return search_entry
# END tokeniser

def search_entry_editor(entry):
# Edit search entry to try & improve search performance
	boolean_list = ['and', 'or', 'not']						# creates a list of boolean key words
	punct_list = [',', '?', '.', '!', '"', "'", ';', '`']	# creates a list of punctuation marks that would be removed from query
	fixed_entry = []										# new list created to store edited search words
	entry = entry.lower()									# convert entry to lowercase
	entry = entry.split()									# splits all words

	for word in entry:
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

	fixed_entry = '+'.join(fixed_entry)		# rejoins words together with a '+'

	return fixed_entry

"""	
def cluster(to_cluster):
	stopword_file = open('..\\etc\\stopwordList.txt', 'r')
	word_read = word_file.read()
	word_list = re.findall(r'\w+', word_read)
	
	if (to_cluster in word_list):
		
"""