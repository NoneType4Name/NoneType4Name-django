import json
import requests
from bs4 import BeautifulSoup as bs
from django.shortcuts import render


def _GetCount(page: bs, svg_name):
    s = page.find('svg', {'class': svg_name})
    return (int(s.find_parent('a').text.replace('\n', '').replace(' ', '')) if s else 0)
    

def index(req):
    page = bs(requests.get('https://github.com/NoneType4Name').content, 'html.parser')
    pins = page.find_all('div', {'class':'pinned-item-list-item-content'})
    data = list(map(lambda r: {
            'name': r.find('span', {'class':'repo'}).text,
            'description':r.find('p', {'class':'pinned-item-desc'}).text.replace('\n        ', '').replace('\n      ', ''),
            'url':'https://github.com'+r.find('a').attrs['href'],
            'language':r.find('span', {'itemprop':'programmingLanguage'}).text,
            'language_color': r.find('span', {'class':'repo-language-color'}).attrs['style'].split()[1],
            'stars': _GetCount(r, 'octicon-star'),
            'forks': _GetCount(r, 'octicon-repo-forked'),
                   }, pins))
    return render(req, 'main/main.jinja', {'pins':data,
                                           'activity':json.loads(requests.get('https://api.lanyard.rest/v1/users/645530866663161856').text)})
