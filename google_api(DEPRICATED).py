import urllib
import json

search = 'hello'
key = 'AIzaSyAGhoWG_wP5xAEM7ifG41F7XnIcT2-Fnlg'
page=0
while page<2:
	link = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+search+'&key='+key+'&rsz=8&start='+str(page)
	site = urllib.urlopen(link)		# opens url to search through
	read_file = site.read()			# reads url (file) text
	site.close()					# done with url (file), so close it


	print link
	results = json.loads(read_file)
	data = results['responseData']
	hits = data['results']
	j=1
	for h in hits:
		print j,' ', h['url'], '-', h['title']
		j=j+1
	page = page+1
	
# Source:	http://stackoverflow.com/questions/1657570/google-search-from-a-python-app
# Source:	http://groups.google.com/group/Google-AJAX-Search-API/browse_thread/thread/407a1bf2a2219117?pli=1
