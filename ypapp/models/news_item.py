__all__ = ['NewsItem']


class NewsItem(object):
    def __init__(self, title, url, date=None):
        self.title = title
        self.url = url
        self.date = date
