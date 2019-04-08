import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "https://mtg-jp.com/products/card-gallery/0000001/423668"

#get html
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

h2_tag = soup.h2 

card_name = h2_tag.string

print(h2_tag)

print(card_name)
