from django.urls import path

from .views import index, books



urlpatterns = [
    path('', index, name='index'),


]