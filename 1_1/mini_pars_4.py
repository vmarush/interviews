import requests
from bs4 import BeautifulSoup

# #class="col-md-4 tags-box"
# url = "http://quotes.toscrape.com/"
# response = requests.get(url)
# resp_text = response.text
# bs = BeautifulSoup(response.content, "html.parser")
# tags = bs.find_all("span", {'class': 'tag-item'})
# for tag in tags:
#     print(tag.text.strip())


# url = "http://quotes.toscrape.com/"
# response = requests.get(url)
# resp_text = response.text
# bs = BeautifulSoup(response.content, "html.parser")
# autor = bs.find_all("small", {'class': 'author'})
# for tag in autor:
#     print(tag.text.strip())

# class="text"
    

# url = "http://quotes.toscrape.com/"
# response = requests.get(url)
# resp_text = response.text
# bs = BeautifulSoup(response.content, "html.parser")
# citata = bs.find_all("span", {'class': "text"})
# autor1 = []
# citata1 = []
# tagi = []
# tag_norm = []
# for tag in citata:
#     citata1.append(tag.text.strip())
#
# va1 = bs.find_all("div", {'class': "tags"})
# for tag in va1:
#     tagi.append(tag.text.split())
# autor = bs.find_all("small", {'class': 'author'})
# for tag in autor:
#     autor1.append(tag.text.strip())
# for i in tagi:
#     # print(i[1:])
#     tag_norm.append(i[1:])
# a1 = f"{autor1[0]} - {citata1[0]} - {tag_norm[0]}"
# a2 = f"{autor1[2]} - {citata1[2]} - {tag_norm[2]}"
# a3 = f"{autor1[3]} - {citata1[3]} - {tag_norm[3]}"
# a4 = f"{autor1[4]} - {citata1[4]} - {tag_norm[5]}"
# a5 = f"{autor1[6]} - {citata1[6]} - {tag_norm[7]}"
# a6 = f"{autor1[7]} - {citata1[7]} - {tag_norm[7]}"
# a7 = f"{autor1[8]} - {citata1[8]} - {tag_norm[8]}"
# a8 = f"{autor1[1]} - {citata1[1]} - {tag_norm[1]}"
# a9 = f"{autor1[9]} - {citata1[9]} - {tag_norm[9]}"
# print(f"{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}\n{a8}\n{a9}")
# with open('index.html',encoding="utf-9")as file:
#     text = file.read()
#
# bs = BeautifulSoup(text,"html.parser")