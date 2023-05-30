"""
WSGI config for NoneType4Name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/nonetype4name')
# sys.path.append('/home/nonetype4name/venv/lib/python3.11/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NoneType4Name.settings')
from bs4 import BeautifulSoup as bs

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
