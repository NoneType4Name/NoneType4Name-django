from django import template 
import requests
register = template.Library()

@register.filter(name='exec')
def exec_replace(val, args):
    return eval(f'val{args}')


@register.simple_tag(name='set')
def set(val):
    return val
