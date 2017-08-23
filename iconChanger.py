#! python
import requests
import urllib
import bs4 
from os.path  import basename
#var=input('Please enter the name of the T.V show ')
var = "How I Met Your Mother"
url1="https://fanart.tv/tv-fanart/"
url1=url1 +var[0]
url2="https://fanart.tv"
r=requests.get(url1)
soup=bs4.BeautifulSoup(r.text)
#print(soup.prettify())
for link in soup.find_all(text =var, href=True):
    url2=url2+link['href']
    print(url2)
r2=requests.get(url2)
soup2=bs4.BeautifulSoup(r2.content)

elem=soup2.select('img')
i=0
for title in elem:
	if title.get('title')==var+" tv poster image":
		link=title.get('src')
		i=i+1
		if(i==1):
			break
#for link in soup2.find_all('bigger_image', href=True):
#   print(link['href'])
	#print(link)
file_name = var
url2="https://fanart.tv"
print(url2+link)
urllib.request.urlretrieve(url2+link, file_name)


