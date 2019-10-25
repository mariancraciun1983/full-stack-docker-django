
import datetime
from django import template
register = template.Library()

@register.inclusion_tag('cart/tags/small_btn.html')
def small_btn(movie):
    return {"movie": movie}

@register.inclusion_tag('cart/tags/large_btn.html')
def large_btn(movie):
    return {"movie": movie}
