from django.shortcuts import  get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json
import re

def getMovies(request):
    url = "http://127.0.0.1:8000/movies"
    data = json.loads(requests.get(url).text, encoding='utf-8')

    context = {
        "datas": data
    }
    return render(request, 'movie/index.html', context)


def getMoviesDetail(request, movie_id):
    url = "http://127.0.0.1:8000/movies/" + str(movie_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')

    context = {
        "datas": data
    }
    return render(request, 'movie/details.html', context)


def getCinemas(request, movie_base_id):
    url = "http://127.0.0.1:8000/movies/" + str(movie_base_id) + '/allCinemas'
    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data
    }
    return render(request, 'movie/film_cinema.html', context)


def getCinemasDetail(request, movie_base_id, cinema_name):
    url = "http://127.0.0.1:8000/movies/" + str(movie_base_id) + "/cinemaSession/cinema_name=" + cinema_name

    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data
    }
    return render(request, 'movie/tickets.html', context)


def chooseSeat(request, movie_base_id, cinema_id, begin, end, lang, hall, date):
    print(date)
    url = "http://127.0.0.1:8000/movies/" + str(movie_base_id) + "/cinemasDetail/cinema_id=" + str(cinema_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data,
        "begin": begin,
        "end": end,
        "hall": hall,
        "lang": lang,
        "date": date
    }
    return render(request, 'movie/choose_seat.html', context)


def getOrder(request, movie_base_id, cinema_id, time, begin, end, lang, hall, date, seats_num):
    url = "http://127.0.0.1:8000/order/" + str(movie_base_id) + "/" + str(cinema_id) + "/" + time + "/" + begin + "/" + end + "/" + hall + "/" + lang + "/" + date + "/" +  seats_num
    data = json.loads(requests.get(url).text, encoding='utf-8')
    print(data)
    context = {
        "datas": data,
    }
    return render(request, 'movie/order.html', context)

@csrf_exempt
def ajax_get(request):
    data = json.loads(request.body)
    index_list = data['seats']
    if len(index_list) == 1:
        num = re.findall('\d+', index_list[0])[0]
    else:
        num =re.findall('\d+', index_list[0])[0] + '_' + re.findall('\d+', index_list[1])[0]
    context = {
        "seats_num": num
    }
    print(context)
    return JsonResponse(context)