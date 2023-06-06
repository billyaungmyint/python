import os
from lxml import etree

os.chdir(r'D:\Temp\python\python\udemy\webscrapping')
tree = etree.parse("fundamentals/src/web_page.html")
print(tree)