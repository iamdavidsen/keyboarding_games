from django.shortcuts import render, redirect

from games.models import Package


def game_view(request, slug):
    packages = Package.objects.select_related("game").filter(game__slug=slug).order_by('-id')

    if packages.count() > 0:
        return render(request, "games/game.html", { "package": packages[0] })

    return redirect('home', permanent=True)


