#coding=utf8

from django.urls import path
from movies_tickets.views import MovieBaseAPI, MovieDetailAPI, CinemasApi, CinemaDetailAPI, MovieSessionsAPI, ALLCinemasApi, MovieSessionByDateAPI, CinemaSessionByMovieAPI, OrderApi

urlpatterns = [
    path('movies', MovieBaseAPI.as_view()),
    path('movies/<int:movie_base_id>', MovieDetailAPI.as_view()),
    path('movies/<int:movie_base_id>/allCinemas', ALLCinemasApi.as_view()),
    path('movies/<int:movie_base_id>/cinemasDetail/cinema_id=<int:cinema_id>', CinemaDetailAPI.as_view()),
    path('movies/<int:movie_base_id>/cinemaSession/cinema_name=<str:cinema_name>', CinemaSessionByMovieAPI.as_view()),
    path('cinemas', CinemasApi.as_view()),
    path('cinemas/sessions/<str:cinema_name>', MovieSessionsAPI.as_view()),
    path('cinemas/sessions/<str:cinema_name>/<str:day>', MovieSessionByDateAPI.as_view()),
    path('order/<int:movie_base_id>/<int:cinema_id>/<str:time>/<str:begin>/<str:end>/<str:hall>/<str:lang>/<str:date>/<str:seats_num>', OrderApi.as_view()),

]
