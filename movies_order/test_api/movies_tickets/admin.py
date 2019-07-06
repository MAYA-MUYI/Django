from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MovieBase, MovieDetail, Cinemas

#注册两个app
@admin.register(MovieBase)
class MovieBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'ellipsis', 'time', 'vision')

@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cinema_name', 'address', 'price', 'city')

@admin.register(MovieDetail)
class MovieDetailAdmin(admin.ModelAdmin):
    list_display = ('id','movie_name', 'ellipsis', 'time', 'vision', 'duration', 'introduction', 'type')
