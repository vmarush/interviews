import requests
import json
url = "https://www.franksonnenbergonline.com/blog/are-you-grateful/"
response = requests.get(url=url)
content = response.text
# print(content)
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "html.parser")
href_list = soup.find_all("ul", {'class': 'menu genesis-nav-menu menu-primary'})
for el in href_list:
    print(el.text)


response = requests.get(
        url="https://fakerapi.it/api/v1/credit_cards?_quantity=2/")
desc = response.json()['data'][0]
for i in desc:
    print(i)

print(desc)