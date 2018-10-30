from django.db import models

# Create your models here.


class MovieModels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    link = models.CharField(max_length=100, null=False)
