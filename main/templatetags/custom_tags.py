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
    return ((f'{t.days} day{"s" if t.days-1 else ""} ') if t.days else '')+" ".join(
                        (("0" if not (t.seconds//3600//10) else "") +(str(t.seconds//3600)+"h") if t.seconds//3600 else "",
                        (("0" if not (t.seconds//60)%60//10 else "")+str((t.seconds//60)%60)+"m") if (t.seconds//60)%60 else "",
                        ("0" if not t.seconds%60//10 else "")+str(t.seconds%60)+"s"))
