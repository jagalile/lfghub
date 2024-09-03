import datetime
import json
import ast
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from multiselectfield import MultiSelectField

from users.constants import Country, Languages

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)
    url = models.URLField(default="")

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class LookerSocial(models.Model):
    social_looker = models.ForeignKey("Looker", on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    username = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.social_looker.username + " - " + self.social_media.name


class GameType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Looker(AbstractUser):
    PRONOUNS = (
        ("M", "He/Him/His"),
        ("F", "She/Her/Hers"),
        ("O", "They/Them/Theirs"),
    )

    avatar = models.ImageField(blank=True, upload_to="images/avatar")
    pronouns = models.CharField(
        max_length=1,
        choices=PRONOUNS,
        blank=True,
    )
    bio = models.TextField(blank=True)
    country = models.CharField(null=True, blank=True, max_length=200, choices=Country.countries())
    languages = models.CharField(null=True, blank=True, max_length=200)
    is_gm = models.BooleanField(default=False)
    lfg_gm = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    lfg_player = models.BooleanField(default=False)
    gm_games = models.ManyToManyField(
        Game, null=True, blank=True, related_name="gm_games"
    )
    fav_gm_game = models.ForeignKey(
        Game,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="fav_gm_game",
    )
    player_games = models.ManyToManyField(
        Game, null=True, blank=True, related_name="player_games"
    )
    fav_player_game = models.ForeignKey(
        Game,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="fav_player_game",
    )
    game_types = models.ManyToManyField(
        GameType, null=True, blank=True, related_name="play_types"
    )
    fav_game_type = models.ForeignKey(
        GameType, null=True, blank=True, on_delete=models.CASCADE, related_name="fav_game_type"
    )
    platforms = models.ManyToManyField(
        Platform, null=True, blank=True, related_name="platforms"
    )
    fav_platform = models.ForeignKey(
        Platform,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="fav_platform",
    )
    socials = models.ManyToManyField(
        LookerSocial, null=True, blank=True
    )
    dark_theme = models.BooleanField(default=False)
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username

    def get_languages(self):
        if self.languages is None:
            return []
        return ast.literal_eval(self.languages)

    def get_country_code(self):
        return Country[self.country].name.lower()

    def get_country_name(self):
        return Country[self.country].value

    def get_language_code(self):
        return Languages[self.languages].name.lower()

    def get_language_name(self):
        return Languages[self.languages].value
