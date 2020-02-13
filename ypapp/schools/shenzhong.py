# coding=utf-8
import requests
from bs4 import BeautifulSoup

from ypapp.models import NewsItem
from ypapp.schools._base_school import BaseSchool

__all__ = ['Shenzhong']


class Shenzhong(BaseSchool):
    def __init__(self):
        BaseSchool.__init__(self)
        self.title = u'深圳中学'
        self.home_page_url = 'https://www.shenzhong.net'

    def news_list(self):
        html_doc = requests.get('https://www.shenzhong.net/textnewslist_52.html').content
        soup = BeautifulSoup(html_doc, 'html.parser')
        news_lis = soup.find_all('li', class_='clearfix')
        news_items = []
        for news_li in news_lis:
            a = news_li.find('a')
            title = a.get_text()
            url = 'https://www.shenzhong.net{}'.format(a['href'])
            date = news_li.find('span').get_text()
            news_items.append(NewsItem(title, url, date))
        return news_items
