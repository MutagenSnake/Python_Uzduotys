from bs4 import BeautifulSoup
import requests
import random

delfi = requests.get(f"https://delfi.lt/")
delfi_html = delfi.text
soup = BeautifulSoup(delfi_html, "html.parser")

articles = soup.find_all(class_='CBarticleTitle')

article_list = []
bad_words = ['covid','Covid', 'vakc', 'Vakc', 'koro', 'Koro', 'mirt', 'Mirt']

for item in articles:
    if not any(word in item for word in bad_words):
        article_list.append(item.getText())

first = []
second = []

for article in article_list:
    if ':' in article:
        split_list = article.split(':')
        first.append(split_list[0])
        second.append(split_list[1])

def connect_random():
    number_1_max = len(first)
    number_2_max = len(second)
    random_1 = random.randint(0,number_1_max)
    random_2 = random.randint(0,number_2_max)
    first_part = first[random_1]
    second_part = second[random_2]

    return f'{first_part}:{second_part}'

print(connect_random())

