from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)
    published = models.BooleanField()
    featured = models.BooleanField()
    seo_title = models.CharField(max_length=60, blank=False, null=False)
    seo_description = models.CharField(max_length=150, blank=False, null=False)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    plays = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Package(models.Model):
    title = models.CharField(blank=False, null=False)
    version = models.CharField(max_length=20, blank=False, null=False)
    published = models.BooleanField()
    game = models.ForeignKey(Game, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
