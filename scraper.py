import requests
from bs4 import BeautifulSoup

# quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
# page = requests.get(quote_page)
# c = page.content
# soup = BeautifulSoup(c, "html.parser")
# name_box = soup.find('h1', attrs={'class':'name'})
# name = name_box.text.strip()
# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text.strip()
# print(name)
# print(price)

sitemap = 'https://www.weebly.com/sitemap.xml'
req = requests.get(sitemap)
html = req.content