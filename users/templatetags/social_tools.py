from django import template

from users.models import LookerSocial

register = template.Library()


@register.simple_tag
def get_social_url(user_username, social_name):
    for social in LookerSocial.objects.all():
        if social.social_looker.username == user_username and social.social_media.name == social_name:
            return social.username
    
    return ""
