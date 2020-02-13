# coding=utf-8

from ypapp.schools._base_school import BaseSchool

__all__ = ['Szsy']


class Szsy(BaseSchool):
    def __init__(self):
        BaseSchool.__init__(self)
        self.title = u'深圳实验学校'
        self.home_page_url = 'http://www.szsy.cn/'

    def news_list(self):
        # TODO
        pass
