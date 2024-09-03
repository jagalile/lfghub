from django import template

register = template.Library()


@register.simple_tag
def active(request, url):
    return "active" if request.path == url else ""
