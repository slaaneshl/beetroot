import json
from bs4 import BeautifulSoup
from pprint import pprint
from requests import Session


def main():
    url = 'https://www.netflix.com/browse/genre/34399'

    with Session() as session:

        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'bad response'
        print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    films_list = soup.select('.nm-collections-title-name')
    films_img = soup.select('')

    data = {
        'films_list': films_list[0].text,
        'films_img': films_img
    }
    pprint(data)

    with open('NetFlix.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()