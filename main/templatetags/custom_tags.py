from django import template 
import time
import datetime
register = template.Library()

@register.filter(name='eval')
def exec_replace(val, args):
    return eval(f'val{args}')


@register.simple_tag(name='set')
def set(val):
    return val

@register.filter('to_strtime')
def to_strtime(t):
    t = datetime.timedelta(seconds=time.time()-int(t)/1000)
    return (f'days:{t.days}') if t.days else ''+'{}:{}:{}'.format(t.seconds//3600, (t.seconds//60)%60, t.seconds%60)
