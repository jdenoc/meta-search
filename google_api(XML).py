import urllib
import re

search = 'hello'
api_key = 'AIzaSyAGhoWG_wP5xAEM7ifG41F7XnIcT2-Fnlg'
results=10
search_id = '012733187811704490272:leikl3-kfa0'

link = 'https://www.googleapis.com/customsearch/v1?key='+api_key+'&cx='+search_id+'&q='+search+'&start=1&alt=atom'
site = urllib.urlopen(link)		# opens url to search through
read_file = site.read()			# reads url (file) text
site.close()					# done with url (file), so close it


url_find = re.findall(r'(<link href=")(.+?)(" title=")', read_file)
i=1
for url in url_find:
	print i, url[1]
	i = i+1