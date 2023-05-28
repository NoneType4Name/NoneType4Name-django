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
    acts = json.loads(requests.get('https://api.lanyard.rest/v1/users/645530866663161856').text)
    vscode = tuple(a for a in acts['data']['activities'] if 'assets' in a)
    vscode = vscode[0] if vscode else None
    
    langs_page = bs(requests.get('https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Nonetype4name').text, 'html.parser').find('g', {'data-testid':'main-card-body'})
    # langs = dict([l.text, l.findNextSibling().text] for l in langs_page.find_all('text', {'data-testid':'lang-name'}))
    
    return render(req, 'main/main.jinja', {'pins':data,
                                           'activity':json.loads(requests.get('https://api.lanyard.rest/v1/users/645530866663161856').text),
                                           'vscode':vscode,
                                           'most_lang':dict([l.text, [(l.findNextSibling().text), str(float(l.findNextSibling().text[:-1])+2).replace(',','.'), l.parent.find('rect', {'data-testid':'lang-progress'}).attrs['fill']]] for l in langs_page.find_all('text', {'data-testid':'lang-name'}))})
