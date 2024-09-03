import json
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse

from users.constants import Country, Languages
from .models import Looker, GameType, Game, Platform, SocialMedia
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator


# Create your views here.
def lookers_list(request):
    context = {
        "game_types": GameType.objects.all().order_by("name"),
        "games": Game.objects.all().order_by("name"),
        "platforms": Platform.objects.all().order_by("name"),
    }

    if request.method == "POST":
        open_to = request.POST.get("open_to")
        game = request.POST.get("game")
        platform = request.POST.get("platform")
        game_type = request.POST.get("game_type")
        lookers = Looker.objects.filter(
            platforms__name=platform, game_types__name=game_type
        )
        context["lookers"] = lookers
    else:
        lookers = Looker.objects.all().filter(is_active=1)
    template = loader.get_template("users/lookers_list.html")
    paginator = Paginator(lookers, 5)
    page_number = request.GET.get("page")
    context["page_obj"] = paginator.get_page(page_number)
    context["lookers"] = lookers
    return HttpResponse(template.render(context, request))


def looker_detail_view(request, looker_id):
    if not request.user.is_authenticated:
        template = loader.get_template("users/login.html")
        context = {"info": True}
        return HttpResponse(template.render(context, request))
    if request.user.id == int(looker_id):
        return redirect("users:looker_profile_view", looker_id=looker_id)
    looker = Looker.objects.get(pk=looker_id)
    gm_games = looker.gm_games.all()
    template = loader.get_template("users/looker_detail_view.html")
    context = {
        "looker": looker,
        "gm_games": gm_games,
    }
    return HttpResponse(template.render(context, request))


@login_required
def looker_profile_view(request, looker_id):
    template = loader.get_template("users/looker_profile_view.html")
    context = {
        "looker": Looker.objects.get(pk=looker_id),
    }
    return HttpResponse(template.render(context, request))


@login_required
def edit_looker_profile_view(request, looker_id):
    template = loader.get_template("users/edit_looker_profile_view.html")
    context = {
        "pronouns": Looker.pronouns.field.choices,
        "games": Game.objects.all().order_by("name"),
        "looker_gm_games": Looker.objects.get(pk=looker_id)
        .gm_games.all()
        .order_by("name"),
        "looker_player_games": Looker.objects.get(pk=looker_id)
        .player_games.all()
        .order_by("name"),
        "platforms": Platform.objects.all().order_by("name"),
        "looker_platforms": Looker.objects.get(pk=looker_id)
        .platforms.all()
        .order_by("name"),
        "game_types": GameType.objects.all().order_by("name"),
        "looker_game_types": Looker.objects.get(pk=looker_id)
        .game_types.all()
        .order_by("name"),
        "countries": Country.countries_names(),
        "languages": Languages.languages_codes(),
        "social_media_list": SocialMedia.objects.all().order_by("name"),
    }
    if request.method == "POST":
        update_looker_profile(request=request, looker_id=looker_id)
        return redirect("users:edit_looker_profile_view", looker_id=looker_id)

    return HttpResponse(template.render(context, request))


def lookers_statistics(request):
    template = loader.get_template("users/lookers_statistics_view.html")
    games_frequency = build_games_frequency_data(get_games_frequency())
    context = {
        "total_lookers": Looker.objects.all().count(),
        "gm_lookers": Looker.objects.filter(is_gm=True, is_player=False).count(),
        "player_lookers": Looker.objects.filter(is_player=True, is_gm=False).count(),
        "gm_and_player_lookers": Looker.objects.filter(
            is_gm=True, is_player=True
        ).count(),
        "games_frequency": games_frequency,
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    context = {
        "wrong_username": False,
        "wrong_password_or_deactivated": False,
    }
    if request.method == "POST":
        template = loader.get_template("users/login.html")
        username = request.POST["username"]
        password = request.POST["password"]
        looker_logining = Looker.objects.filter(username=username)
        user = authenticate(request, username=username, password=password)
        if looker_logining and user is None:
            context["wrong_password_or_deactivated"] = True
            return HttpResponse(template.render(context, request))
        if user is not None:
            login(request, user)
            return redirect("users:lookers_list")
        context = {"wrong_username": True}
        return HttpResponse(template.render(context, request))
    if not request.user.is_authenticated:
        template = loader.get_template("users/login.html")
        return HttpResponse(template.render(context, request))
    else:
        return redirect("users:lookers_list")


def logout_view(request):
    logout(request)
    template = loader.get_template("users/login.html")
    context = {"logout": True}
    return HttpResponse(template.render(context, request))


def signup(request):
    context = {
        "username_error": False,
        "confirm_password_error": False,
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password != confirm_password:
            context["confirm_password_error"] = True
        else:
            try:
                new_looker = Looker.objects.create_user(
                    username=username, password=password
                )
                new_looker.save()
                login(request, new_looker)
                return redirect("users:looker_profile_view", looker_id=new_looker.id)
            except IntegrityError:
                context["username_error"] = True
        # return redirect("users:looker_profile", looker_id=new_looker.id)
    template = loader.get_template("users/signup.html")
    return HttpResponse(template.render(context, request))


def terms_and_conditions(request):
    template = loader.get_template("users/terms_and_conditions.html")
    context = {}
    return HttpResponse(template.render(context, request))


def update_looker_profile(request, looker_id):
    pronouns = request.POST.get("pronouns")
    role = request.POST.getlist("role")
    country = request.POST.get("country")
    languages = request.POST.getlist("languages")
    fav_gm_game = request.POST.get("fav_gm_game")
    gm_games = request.POST.getlist("gm_games")
    fav_player_game = request.POST.get("fav_player_game")
    player_games = request.POST.getlist("player_games")
    fav_platform = request.POST.get("fav_platform")
    platforms = request.POST.getlist("platforms")
    fav_game_type = request.POST.get("fav_game_type")
    game_types = request.POST.getlist("game_types")
    dark_theme = request.POST.get("dark_theme")

    looker = Looker.objects.get(pk=looker_id)

    looker.pronouns = get_single_choice_key(Looker.pronouns.field.choices, pronouns)
    if role is None:
        looker.is_gm = False
        looker.is_player = False
    elif len(role) == 2:
        looker.is_gm = True
        looker.is_player = True
    else:
        if "Game Master" in role:
            looker.is_gm = True
            looker.is_player = False
        if "Player" in role:
            looker.is_player = True
            looker.is_gm = False
    looker.country = get_single_choice_key(Country.countries(), country)
    looker.languages = get_multiple_choice_key(Languages.languages(), languages)
    looker.fav_gm_game = Game.objects.filter(name=fav_gm_game).first()
    looker.gm_games.set(Game.objects.filter(name__in=gm_games))
    looker.fav_player_game = Game.objects.filter(name=fav_player_game).first()
    looker.player_games.set(Game.objects.filter(name__in=player_games))
    looker.fav_platform = Platform.objects.filter(name=fav_platform).first()
    looker.platforms.set(Platform.objects.filter(name__in=platforms))
    looker.fav_game_type = GameType.objects.filter(name=fav_game_type).first()
    looker.game_types.set(GameType.objects.filter(name__in=game_types))
    if dark_theme:
        looker.dark_theme = True
    else:
        looker.dark_theme = False
    looker.save()


def get_single_choice_key(choices, value):
    for key, val in choices:
        if val == value:
            return key
    return None


def get_multiple_choice_key(choices, values):
    keys = []
    for value in values:
        for key, val in choices:
            if val == value:
                keys.append(key)
    return keys


def get_games_frequency():
    games = Game.objects.all()
    frequency = {}
    for game in games:
        frequency[game.name] = {}
        frequency[game.name]["gm"] = Looker.objects.filter(
            gm_games__name=game.name
        ).count()
        frequency[game.name]["players"] = Looker.objects.filter(
            player_games__name=game.name
        ).count()
    return frequency


def build_games_frequency_data(games_frequency):
    data = {
        "labels": [],
        "datasets": [],
    }
    for game, frequency in games_frequency.items():
        data["labels"].append(game)
        gm_dataset = {
            "label": "GMs",
            "data": [frequency["gm"]],
            "backgroundColor": "rgba(255, 99, 132, 0.2)",
            "stack": "Stack 0",
        }
        data["datasets"].append(gm_dataset)
        players_dataset = {
            "label": "Players",
            "data": [frequency["players"]],
            "backgroundColor": "rgba(54, 162, 235, 0.2)",
            "stack": "Stack 0",
        }
        data["datasets"].append(players_dataset)
    return json.dumps(data)
