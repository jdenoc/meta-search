#!/usr/bin/python
##
## Filename:	query_mod.py
## Version:		2.1
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

def search_entry_editor(search_entry):
# Edit search entry to try & improve search performance
	
	fixed = []				# new list created to store edited search words
	fix = search_entry		# allows for easier code writing/editing
	fix = fix.lower()		# convert entry to lowercase
	fix = fix.split()		# splits all words

	for word in fix:
	# searches through each word & removes unwanted characters
		i = 0
		while i < len(word):
			if word[i] == ',' or word[i] == '?' or word[i] == "'" or word[i] == '"' or word[i] == '!':
				remove = word[i]
				word = word.replace(remove, '')
			else:
				i = i + 1
		fixed.append(word)

	fixed = '+'.join(fixed)		# rejoins words together with a '+'
	search_entry = fixed		# returns altered search entry to search_entry variable

	return search_entry

