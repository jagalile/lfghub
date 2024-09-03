from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Game, Platform, SocialMedia, Looker, LookerSocial, GameType

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(SocialMedia)
admin.site.register(Looker)
admin.site.register(LookerSocial)
admin.site.register(GameType)
