from __future__ import unicode_literals

import urllib
import urllib2
import mechanize
from bs4 import BeautifulSoup#proxy support for browser and id3 metadata

br=mechanize.Browser()

br.addheaders=[('User-Agent','Mozilla/12.0(x11; Kali Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

br.set_handle_robots(False)

search_text=str(raw_input("enter term to search:"))

query=urllib.quote(search_text)

url="https://www.google.com/search?q=" + query

#req=urllib2.Request(url)


#req.add_header('User-Agent','Mozilla/5.0(x11; Fedora;Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')

#r=urllib2.urlopen(req)




#html=r.read()

page=br.open(url)
html=page.read()

#print html


l=list()

soup=BeautifulSoup(html,"html.parser")

for term in  soup.find_all('h3', {'class': ['r']}):
    link= 'https://www.google.com' + term['href']
    l.append(link)

print l
