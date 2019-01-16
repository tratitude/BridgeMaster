from django import template
import math
register = template.Library()

@register.filter
def divide(num, val):
    return math.floor(num / val)