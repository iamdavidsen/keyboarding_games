from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from games.models import Game


class PagesViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return Game.objects.order_by('-id')[0].updated_at
