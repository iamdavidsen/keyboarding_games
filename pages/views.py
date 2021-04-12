from django.shortcuts import render

from games.models import Game


def home_view(request):
    featured_games = Game.objects.filter(published=True, featured=True)
    games = Game.objects.filter(published=True)

    return render(request, "pages/home.html", { 'featured_games': featured_games, 'games': games })
