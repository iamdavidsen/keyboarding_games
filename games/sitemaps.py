from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from games.models import Game


class GamesViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Game.objects.all()

    def lastmod(self, game):
        return game.updated_at