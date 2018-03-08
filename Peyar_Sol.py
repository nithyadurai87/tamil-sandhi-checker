# -*- coding: UTF-8 -*-
from wikitools import wiki
from wikitools import category

file = open('nit.txt', 'w')


site = wiki.Wiki("https://ta.wiktionary.org/w/api.php") 
site.login("NithyaDuraisamy", "Nithu@143")
cat = category.Category(site, "பெயர்ச்சொற்கள்")
# iterate through all the pages in ns 0
for article in cat.getAllMembers(namespaces=[0]):
	file.write(article.title.encode("utf-8")+'\n') 