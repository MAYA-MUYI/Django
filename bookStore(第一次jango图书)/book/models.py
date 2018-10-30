# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
from django.db import models


class BookDetail(models.Model):
    book_name = models.CharField(max_length=500)
    star = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    cod = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    image_path = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_detail'


class BookHome(models.Model):
    book_name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    star = models.CharField(max_length=10)
    image_path = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'book_home'
