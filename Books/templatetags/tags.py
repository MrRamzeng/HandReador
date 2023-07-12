from django import template

register = template.Library()


@register.simple_tag
def get_all_attrs(var):
    return dir(var)


@register.simple_tag
def splice(text):
    return text.replace('&para;', '\n')
