from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cookie(context, name, default=""):
    request = context["request"]
    return request.COOKIES.get(name, default)
