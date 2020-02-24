# coding=utf-8
import requests
from requests.exceptions import ChunkedEncodingError

from ypapp.schools._base_school import BaseSchool

__all__ = ['Szsy']


class Szsy(BaseSchool):
    def __init__(self):
        BaseSchool.__init__(self)
        self.title = u'深圳实验学校'
        self.home_page_url = 'http://www.szsy.cn/'

    def news_list(self):
        headers = {'Referer': 'http://www.szsy.cn/',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/80.0.3987.116 Safari/537.36'}
        url = 'http://www.szsy.cn/category/more/40288176573b2cfd01573b3400aa0002.shtm'
        with requests.get(url, stream=True, headers=headers) as response:
            try:
                for chunk in response.iter_content(chunk_size=256):
                    if chunk:
                        print 'abc'
            except ChunkedEncodingError:
                print 'error'
                pass
        return []
