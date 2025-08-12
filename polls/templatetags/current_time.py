from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def time_now():
    time = timezone.now()
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"
