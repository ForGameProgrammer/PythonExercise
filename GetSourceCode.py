import requests
from bs4 import BeautifulSoup

def get_html_source(url):
    source = requests.get(url) # Response olarak Dönüş yapıyor
    return source.text # Response dan Plain Text'e çevirip yolluyoruz

def get_links_from_html(html):
    soup = BeautifulSoup(html, "html.parser") # Yardımcı Library HTML i ayrıştırabiliyor
    tags = soup.find_all('a') # <a href=''></a> gibi link taglerini alıyor
    # soup.find_all('a', {'class' : 'bir class'}) class ları bir class olanları alır
    links = []
    for link in tags:
        links.append(link.get('href')) # href='' içindeki linki alıyor
        # link.string yazarsak Değerini alırız yani <a href=''>Yazı</a> Yazı'yı alır
    return links

print(get_links_from_html(get_html_source("https://www.youtube.com"))) # Youtube'daki linkleri al :)

