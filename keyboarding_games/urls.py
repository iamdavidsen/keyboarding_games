from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from games.sitemaps import GamesViewSitemap
from pages.sitemaps import PagesViewSitemap

sitemaps = {'pages': PagesViewSitemap, 'games': GamesViewSitemap}

urlpatterns = [
                  path('', include('pages.urls')),
                  path('games/', include('games.urls')),
                  path('admin/', admin.site.urls),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
                  path(
                      "robots.txt",
                      TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
                  ),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
