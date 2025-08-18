from django import template
from django.utils import timezone
from django.utils.timezone import localtime

register = template.Library()

@register.simple_tag
def time_now():
    time = localtime(timezone.now())
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"
