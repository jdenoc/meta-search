#!/usr/bin/python
##
## Filename:	query_mod.py
## Version:		4.2.2
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
	
	fixed_entry = []			# new list created to store edited search words
	entry = entry.lower()		# convert entry to lowercase
	entry = entry.split()		# splits all words

	for word in entry:
	# searches through each word & removes unwanted characters
		i = 0
		while i < len(word):
			if word[i] == ',' or word[i] == '?' or word[i] == "'" or word[i] == '"' or word[i] == '!':
				remove = word[i]
				word = word.replace(remove, '')
			else:
				i = i + 1
		fixed_entry.append(word)

	fixed_entry = '+'.join(fixed_entry)		# rejoins words together with a '+'

	return fixed_entry

def and_or_not(entry):
# Edits search entry in such a way that the boolean operators 'AND' 'OR' & 'NOT' work
	return 0