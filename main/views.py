from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def index(req):
    page = bs(requests.get('https://github.com/Taiga74164').content, 'html.parser')
    repos = page.find_all('span', {'class':'repo'})
    stars = tuple(map(lambda d: int(d.text.replace('\n', '').replace(' ', '')) ,page.find_all('a', {'class':'pinned-item-meta'})))
    print(stars)

    # data = dict(repos, {'description':'',
                        # 'stared':0,
                        # 'forks':0,
                        # 'programmingLanguage':'text',
                        # })
    # data = {}
    # for r in repos:
        # data[r] = {'description':'',
                        # 'stared':0,
                        # 'forks':0,
                        # 'programmingLanguage':'text',
                        # }
    return render(req, 'main/main.html')
