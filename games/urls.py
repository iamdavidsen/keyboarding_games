from django.urls import path

from games.views import game_view

urlpatterns = [
    path('<slug:slug>', game_view, name="game"),
]
