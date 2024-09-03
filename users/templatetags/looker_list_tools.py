from django import template

register = template.Library()


@register.filter
def list_names(value):
    item_list = []
    for item in value:
        item_list.append(item.name)
    return item_list
