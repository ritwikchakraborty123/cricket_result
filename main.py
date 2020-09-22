import requests as rq
import bs4
URL='https://www.cricbuzz.com/'
res=rq.get(URL)
# print(res.content)
soup=bs4.BeautifulSoup(res.text,'lxml')
title=soup.find("div",{"id":"match_menu_container"})
k=title.find_all('li')
for i in k:
    print(i.get_text())