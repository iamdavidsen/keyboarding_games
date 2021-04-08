from django.shortcuts import render

from games.models import Game


def home_view(request):
    games = Game.objects.filter(published=True)

    return render(request, "pages/home.html", { 'games': games })
