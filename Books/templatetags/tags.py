from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def get_all_attrs(var):
    return dir(var)


@register.simple_tag
def tagger(text):
    return list(text)
