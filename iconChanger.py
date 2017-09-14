#!/usr/bin/env python3
import requests
import urllib
import bs4 
import os
from os.path import basename

urlBase="https://fanart.tv"
url1="https://fanart.tv/tv-fanart/"
#loops through all folder names in current directory and downloads image.
for fileName in os.listdir(os.getcwd()):

    if os.path.isdir(fileName):
        link=5 #this line helps prevent extra folders from being changed
        url1=urlBase+"/tv-fanart/"+fileName[0]
        r=requests.get(url1)
        soup=bs4.BeautifulSoup(r.text,"lxml")

        for link in soup.find_all(text =fileName, href=True):
            url2=urlBase+link['href']
            print(url2)
            r2=requests.get(url2)
            soup2=bs4.BeautifulSoup(r2.content,"lxml")
            images=soup2.select('img')

            for title in images:
                if(not isinstance(title.get('title'), str)):
                    continue
                if " tv poster image" in title.get('title'):
                    link=title.get('src')
                    print(urlBase+link)
                    break

                

            #checks if image exists on webpage,if not ignore the folder.
            if(not isinstance(link, str)):
                continue
            else:
                break
        if(not isinstance(link, str)):
            continue
        print('downloaded')
        urllib.request.urlretrieve(urlBase+link,os.path.join(os.path.join(os.getcwd(),fileName),fileName))
        #opens up system shell to change icons
        os.system("gvfs-set-attribute -t string \""+ os.path.join(os.getcwd(),fileName) +"\" metadata::custom-icon file://\""+os.path.join(os.path.join(os.getcwd(),fileName),fileName)+"\"")
        