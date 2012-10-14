import urllib
import json

search = 'hello'
api_key = 'AIzaSyAGhoWG_wP5xAEM7ifG41F7XnIcT2-Fnlg'
results=10
search_id = '012733187811704490272:leikl3-kfa0'

i=1
while i<results:
	link = 'https://www.googleapis.com/customsearch/v1?key='+api_key+'&cx='+search_id+'&q='+search+'&start='+str(i)
	site = urllib.urlopen(link)		# opens url to search through
	read_file = site.read()			# reads url (file) text
	site.close()					# done with url (file), so close it


	print link
	
	data = json.loads(read_file)
	hits = data['items']
	j=1
	for h in hits:
		print j,' ', h['link'], '-', h['title']
		j=j+1
	
	i=i+10

# Source:	http://www.google.com/support/forum/p/customsearch/thread?tid=56c0bd92dda351b7&hl=en
# Source:	http://code.google.com/apis/customsearch/v1/using_rest.html#query-params