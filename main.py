from bs4 import BeautifulSoup
import requests
import re
import codecs


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

"""
list_url = "https://novelbin.englishnovel.net/novel-book/versatile-mage#tab-chapters-title"
base_url = "https://novelbin.englishnovel.net/novel-book/versatile-mage"
resp = requests.get(list_url, headers=headers)
soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
links = [link.get('href') for link in soup.find_all("a", title=re.compile("^Chapter"))]
links = links[1:]
print(links)
"""


url = "https://novelbin.englishnovel.net/novel-book/versatile-mage/chapter-1"
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')

title = soup.find("a", class_="novel-title").get("title")
print(title)
chapter = soup.find("a", class_="chr-title").get("title")
print(chapter)
content = soup.find_all(id="chr-content")
content2 = ''
for a in content:
    content2 += a.text.strip()
#print(content2)

file = codecs.open("{}.txt".format(chapter), "w", "utf-8-sig")
file.write(content2)
file.close()
print("Finished writing the chapter text file!")
