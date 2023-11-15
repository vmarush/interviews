import requests

from bs4 import BeautifulSoup
import csv

my_list = []

count = 1
while count < 11:
    url = "http://quotes.toscrape.com/page/" + str(count)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    for i in range(0, len(quotes)):

        my_list.append({"text": quotes[i].text})
        my_list.append({"autor": authors[i].text})
        tagsforquote = tags[i].find_all('a', class_='tag')
        for tagforquote in tagsforquote:
            my_list.append({"tags": tagforquote.text})
    count += 1

with open('123.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        my_list
    )


# Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15
#headers выше строчка