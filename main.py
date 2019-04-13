import settings
import os
import urllib.request, urllib.error
from bs4 import BeautifulSoup

print('カードセットを入力')
version = input();

garally_url = os.getenv('GALLERY_URL')
url = garally_url + "/" + version + "/423668"

#get html
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

h2_tag = soup.h2 

card_name = h2_tag.string

print(h2_tag)

print(card_name)
