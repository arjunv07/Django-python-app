# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_img = models.ImageField(upload_to = 'album_img/')
    album_genre = models.CharField(max_length=200)

    def __str__(self):
        return self.album_name

class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=150)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.name
