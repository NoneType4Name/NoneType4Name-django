from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

class DATA(dict):
    """
    Custom dictionary.
    """

    def __init__(self, data):
        for name, value in data.items():
            setattr(self, str(name), self._wrap(value))
        super().__init__(data)

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return DATA(value) if isinstance(value, dict) else value

    def __repr__(self):
        return '{%s}' % str(', '.join("'%s': %s" % (k, repr(v)) for (k, v) in self.__dict__.items()))


def _GetCount(page: bs, svg_name):
    s = page.find('svg', {'class': svg_name})
    return (int(s.find_parent('a').text.replace('\n', '').replace(' ', '')) if s else 0)
    

def index(req):
    # page = bs(requests.get('https://github.com/Taiga74164').content, 'html.parser')
    page = bs(requests.get('https://github.com/NoneType4Name').content, 'html.parser')
    data = []
    # repos = tuple(map(lambda r: r.text,page.find_all('span', {'class':'repo'})))
    # repos = page.find_all('span', {'class':'repo'})
    pins = page.find_all('div', {'class':'pinned-item-list-item-content'})
    # stars = tuple(map(lambda d: int(d.text.replace('\n', '').replace(' ', '')) ,page.find_all('a', {'class':'pinned-item-meta'})))
    for r in pins:
        data.append(DATA({
            'name': r.find('span', {'class':'repo'}).text,
            'description':r.find('p', {'class':'pinned-item-desc'}).text.replace('\n        ', '').replace('\n      ', ''),
            'url':'https://github.com'+r.find('a').attrs['href'],
            'language':r.find('span', {'itemprop':'programmingLanguage'}).text,
            'language_color': r.find('span', {'class':'repo-language-color'}).attrs['style'].split()[1],
            'stars': _GetCount(r, 'octicon-star'),
            'forks': _GetCount(r, 'octicon-repo-forked'),
                   }))
    return render(req, 'main/main.html', {'pins':data})
