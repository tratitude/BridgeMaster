from django import template
import math
register = template.Library()

@register.filter
def modulo(num, val):
    return num % val