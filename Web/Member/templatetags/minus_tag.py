from django import template
import math
register = template.Library()

@register.filter
def minus(num, val):
    return num - val