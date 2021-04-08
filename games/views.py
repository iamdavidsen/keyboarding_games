from django.shortcuts import render

from games.models import Package


def game_view(request, slug):
    package = Package.objects.select_related("game").filter(game__slug=slug).order_by('-id')[0]

    return render(request, "games/game.html", { "package": package })
