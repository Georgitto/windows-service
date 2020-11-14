from bs4 import BeautifulSoup
import requests


class Parser():

    def __init__(self):
        self.news = [[], []]

    def get_html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        return requests.get('https://habr.com/ru/news/', headers=headers).text

    def get_news(self):
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.findAll("a", {"class": "post__title_link"})
        for tag in tags:
            self.news[0].append(tag.string)
            self.news[1].append(tag.get('href'))


if __name__ == '__main__':
    obj = Parser()
    obj.get_news()

    print(obj.news)