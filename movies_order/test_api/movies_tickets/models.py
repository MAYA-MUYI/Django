# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Cinemas(models.Model):
    cinema_name = models.CharField(max_length=50)
    address = models.TextField()
    price = models.CharField(max_length=2)
    city = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cinemas'


class MovieBase(models.Model):
    movie_name = models.CharField(max_length=20)
    ellipsis = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    vision = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_base'


class MovieDetail(models.Model):
    movie_name = models.CharField(max_length=20)
    ellipsis = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    vision = models.CharField(max_length=10, blank=True, null=True)
    duration = models.CharField(max_length=3)
    introduction = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_detail'
