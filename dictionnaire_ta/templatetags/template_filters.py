from django import template

register = template.Library()

@register.filter
def index(value, nom):
    return value.index(nom)+1

