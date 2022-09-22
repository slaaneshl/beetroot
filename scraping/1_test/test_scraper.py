import json
from pprint import pprint
from requests import Session
from bs4 import BeautifulSoup


def main():
    url = 'https://www.goodreads.com/book/show/6043781'

    with Session() as session:

        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'bad response'
        print(response.status_code)

    soup = BeautifulSoup(response.content, 'lxml')

    title = soup.select('#bookTitle')
    author = soup.select('#bookAuthors span div a span')
    rating = soup.select('#coverImage')
    text = soup.select('#description span')
    img_url = soup.select('#coverImage')
    reviews = [review.text.strip() for review
               in soup.select('.reviewText span span')]

    data = {
        'title': title[0].text.strip(),
        'author': author[0].text.strip(),
        'rating': rating[0].text.strip(),
        'text': text[1].text.strip(),
        'img_url': img_url[0]['src'],
        'reviews': reviews
    }

    pprint(data)

    with open('book.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
