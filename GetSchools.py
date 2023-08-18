import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the list of schools
url = "https://www.usnews.com/best-colleges/rankings/engineering-doctorate-computer"

# Send a GET request to the URL
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements containing school information
    schools = soup.find_all("div", class_="block-normal")

    for school in schools:
        # Extract relevant data
        school_name = school.find("h3", class_="block-flush").text.strip()
        sat_score = school.find("p", class_="block-normal-admit-info").text.strip()
        acceptance_rate = school.find("p", class_="block-normal-admit-info").find_next("p").text.strip()

        print("School:", school_name)
        print("SAT Score:", sat_score)
        print("Acceptance Rate:", acceptance_rate)
        print("-" * 20)
else:
    print("Failed to retrieve the webpage.")
