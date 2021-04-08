from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
import uuid

import os
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('games', filename)


class Category(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Game(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)
    published = models.BooleanField()
    featured = models.BooleanField()
    slug = models.SlugField()
    seo_title = models.CharField(max_length=60, blank=False, null=False)
    seo_description = models.CharField(max_length=150, blank=False, null=False)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    plays = models.IntegerField()
    tags = TaggableManager()
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'slug': self.slug})


class Package(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    version = models.CharField(max_length=20, blank=False, null=False)
    published = models.BooleanField()
    game = models.ForeignKey(Game, blank=False, null=False, on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False, upload_to=content_file_name)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.title + " " + self.version
