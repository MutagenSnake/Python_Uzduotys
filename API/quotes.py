from bs4 import BeautifulSoup
import requests
import random

site = requests.get(f"http://quotes.toscrape.com/")
site_html = site.text
soup = BeautifulSoup(site_html, "html.parser")

quotes = soup.find_all(class_='text')

authors = soup.find_all(class_='author')

authors_href = soup.find_all('a', attrs={'class': None})

quote_list = []
authors_list = []
authors_href_list = []

for quote in quotes:
    quote_list.append(quote.getText())

for author in authors:
    authors_list.append(author.getText())

for author in authors_href:
    authors_href_list.append(author['href'])

del authors_href_list[0:2] # Nemoku gražiai išrinkti, tai reikia šalinti papildomus...

def get_author_info(author_number):
    url = f'http://quotes.toscrape.com{authors_href_list[author_number]}/'
    author_site = requests.get(url)
    author_site_html = author_site.text
    soup = BeautifulSoup(author_site_html, "html.parser")
    date_of_birth_html = soup.find(class_="author-born-date")
    birth_location_html = soup.find(class_="author-born-location")
    print(f' Author date of birth: {date_of_birth_html.getText()}')
    print(f' Author birth location: {birth_location_html.getText()}')


def guess_author():
    len_quote_list = len(quote_list)
    randon_number = random.randint(0, len_quote_list)
    print(quote_list[randon_number])
    while True:
        guess = input("Guess the author:\n")
        if guess == authors_list[randon_number]:
            print('Correct')
            break
        else:
            author = authors_list[randon_number]
            author_listed = author.split(" ")
            print(f'Initials: {author_listed[0][0]} {author_listed[1][0]}')
            guess2 = input("Guess the author:\n")
            if author == guess2:
                print('Correct')
                break
            else:
                get_author_info(randon_number)
                guess3 = input("Guess the author:\n")
                if author == guess3:
                    print('Correct')
                    break
                else:
                    print('Incorrect')
                    break

guess_author()