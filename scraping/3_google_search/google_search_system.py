from requests import Session
from bs4 import BeautifulSoup
import json


def response_from_site(url):
    with Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'bad response'
    return response


def scraping(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    search = soup.select('')
    breakpoint()
    # return


def json_file(items):
    with open('google_search_items.json', 'w') as file:
        json.dump(items, file, indent=4)


def main():
    url = 'https://www.google.com.ua/'
    response = response_from_site(url)
    items = scraping(response)
    json_file(items)


if __name__ == "__main__":
    main()
