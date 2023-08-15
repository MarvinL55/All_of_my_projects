from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

numbers = soup.findAll("span", attrs={"field_numbers":"numbers-ball"})
authors = soup.findAll("small", attrs={"class":"author"})

for num in numbers:
    print(num.text)
for author in authors:
    print(author.text)