#! python
import requests
import urllib
import bs4 
import os
from os.path import basename

print(os.getcwd())

urlBase="https://fanart.tv"
url1="https://fanart.tv/tv-fanart/"
#loops through all folder names in current directory and downloads image.
for fileName in os.listdir(os.getcwd()):
	
	if os.path.isdir(fileName):

		url1=urlBase+"/tv-fanart/"+fileName[0]
		r=requests.get(url1)
		soup=bs4.BeautifulSoup(r.text,"lxml")
		for link in soup.find_all(text =fileName, href=True):
			url2=urlBase+link['href']
			print(url2)
			break
		r=requests.get(url2)
		soup=bs4.BeautifulSoup(r.content,"lxml")
		images=soup.select('img')
		for title in images:
			if title.get('title')==fileName+" tv poster image":
				link=title.get('src')
				print(urlBase+link)
				if link:
					break
				else:
					continue

		
		if(not isinstance(link, str)):
			continue
		urllib.request.urlretrieve(urlBase+link,os.path.join(os.path.join(os.getcwd(),fileName),fileName))
		
		os.system("gvfs-set-attribute -t string \""+ os.path.join(os.getcwd(),fileName) +"\" metadata::custom-icon file://\""+os.path.join(os.path.join(os.getcwd(),fileName),fileName)+"\"")

