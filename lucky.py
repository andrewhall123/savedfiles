# python 3

import requests,sys,webbrowser, bs4

print('Googling...')
res=requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

#retrive top search request
soup=bs4.BeautifulSoup(res.text)

#open a browser fo each result
linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))
