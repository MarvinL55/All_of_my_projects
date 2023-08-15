import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news/world-middle-east-64618187"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="article")

for article in articles:
    headline = article.find("h2").text
    summary = article.find("p", class_="summary").text

    print(f"Headline: {headline} | Summary: {summary}")