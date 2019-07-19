#coding=utf8
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from movies_tickets import query
import os
import re
from movies_tickets.models import MovieBase, MovieDetail, Cinemas
from movies_tickets.serializers import MovieBaseSerializer, MovieDetailSerializer, CinameSerializer, SessionSerializer


star = [8.8, 9.0, 9.1, 9.3]
step = [3, 4, 5]


class MovieBaseAPI(APIView):
    """
    电影清单API
    """
    serializer_class = MovieBaseSerializer

    def get(self, request):
        """
        获取电影信息
        """
        result = []
        movies = MovieBase.objects.all()

        for movie in movies:
            result.append({
                'movie_base_id': movie.id,
                'movie_name': movie.movie_name,
                'time': movie.time,
                "star": random.choice(star),
                'vision': movie.vision,
                'ellipsis': movie.ellipsis,
                "type": MovieDetail.objects.get(id=movie.id).type,
                "pic": "image/" + movie.movie_name + '_pic.jpg',
                "ellipsis_length": len(movie.ellipsis)
            })
        return Response(result)


class MovieDetailAPI(APIView):
    """
    电影列表API
    """
    serializer_class = MovieDetailSerializer

    def get(self, request, movie_base_id):
        """
        获取电影列表
        """
        result = []
        _movie = MovieBase.objects.get(id=movie_base_id)
        movies = MovieDetail.objects.filter(movie_name=_movie.movie_name)
        for movie in movies:
            result.append({
                'movie_detail_id': movie.id,
                'movie_base_id': _movie.id,
                'movie_name': movie.movie_name,
                'time': movie.time,
                "star": random.choice(star),
                "type": movie.type,
                'vision': movie.vision,
                'ellipsis': movie.ellipsis,
                "ellipsis_length": len(movie.ellipsis),
                "duration": movie.duration,
                'introduction': movie.introduction,
                'timg': 'image/' + movie.movie_name + '_timg.jpg',
                'pic': 'image/' + movie.movie_name + '_pic.jpg',
                'stills1': 'image/' + movie.movie_name + '_stills1.jpg',
                'stills2': 'image/' + movie.movie_name + '_stills2.jpg',
                'stills3': 'image/' + movie.movie_name + '_stills3.jpg',
                'stills4': 'image/' + movie.movie_name + '_stills4.jpg',
            })

        return Response(result)


class ALLCinemasApi(APIView):
    serializer_class = MovieDetailSerializer

    def get(self, request, movie_base_id):
        _movie = MovieBase.objects.get(id=movie_base_id)
        movie_name = _movie.movie_name
        result = []
        recent_session = []
        files_list = os.listdir('files')
        for file in files_list:
            cinema = Cinemas.objects.get(cinema_name=query.file_format(file))
            #一个影院的所有电影
            movies = query.getText(file)
            for movie in movies:
                if movie['movie_name'] == movie_name:
                    for data in movie['result'][0][0]['session_result']:
                        recent_session.append(data['begin_time'])
                    recent_session = query.recentList_format(recent_session)
                    result.append({
                        "movie_base_id": movie_base_id,
                        "movie_name": movie_name,
                        "star": movie['star'],
                        "cinema_id": cinema.id,
                        "cinema_name": query.file_format(file),
                        "city": cinema.city,
                        "address": cinema.address,
                        "price": cinema.price,
                        "distance": 13.77 + random.choice(step),
                        "recent_session": recent_session,
                        "movie_session": movie['result']
                    })
                    print(recent_session)
        return Response(result)


class CinemasApi(APIView):

    def get(self, request):
        """
        获取具体电影院信息
        """
        result = []
        cinemas = Cinemas.objects.all()
        for cinema in cinemas:
            result.append({
                "cinema_id": cinema.id,
                "cinema_name": cinema.cinema_name,
                "city": cinema.city,
                "address": cinema.address,
                "price": cinema.price,
                "distance": 13.77 + (cinema.id - 1) * random.choice(step)
            })
        return Response(result)


class CinemaDetailAPI(APIView):

    serializer_class = CinameSerializer

    def get(self, request, movie_base_id, cinema_id):
        """
        获取城市行政区列表
        """
        result = []
        _movie = MovieBase.objects.get(id=movie_base_id)
        movie = MovieDetail.objects.get(movie_name=_movie.movie_name)
        cinema = Cinemas.objects.get(id=cinema_id)
        result.append({
            "movie_base_id": _movie.id,
            "movie_detail_id": movie.id,
            "movie_name": movie.movie_name,
            "vision": movie.vision,
            "cinema_id": cinema_id,
            "cinema_name": cinema.cinema_name,
            "time": movie.time[-5:],
            "price": cinema.price,
            "duration": movie.duration,
        })

        return Response(result)


class MovieSessionsAPI(APIView):

    serializer_class = SessionSerializer

    def get(self, request, cinema_name):
        movies = query.getText(cinema_name)
        result = []
        result.append({
            "cinema_name": cinema_name,
            "cinema_session": movies
        })

        return Response(result)


class MovieSessionByDateAPI(APIView):
#     """
#     影院场次API
#     """
    serializer_class = SessionSerializer

    def get(self, request, cinema_name, day):
        movies = query.getText(cinema_name)
        data = query.getData(movies, query.date_format(day))
        result = []
        result.append({
            "cinema_name": cinema_name,
            "cinema_session": data
        })
        return Response(result)


class CinemaSessionByMovieAPI(APIView):
    def get(self, request, movie_base_id, cinema_name):
        result = []
        date_list = []
        other_day = []
        _movie = MovieBase.objects.get(id=movie_base_id)
        movie = MovieDetail.objects.get(movie_name=_movie.movie_name)
        cinema = Cinemas.objects.get(cinema_name=cinema_name)
        session_movies = query.getText(cinema_name)
        for data in session_movies:
            if data['movie_name'] == movie.movie_name:
                # 获取时间列表
                for sessions in data['result']:
                    date_list.append(sessions[0]['date'])
                other_day.append(data['result'][1:])
                result.append({
                    "cinema_id": cinema.id,
                    "cinema_name": cinema_name,
                    "movie_name": movie.movie_name,
                    "movie_base_id": _movie.id,
                    "vision": movie.vision,
                    "duration": movie.duration,
                    "price": cinema.price,
                    "date_list": date_list,
                    "movie_session": data['result'],
                    "other_day": other_day
                })
        return Response(result)

class OrderApi(APIView):
    def get(self, request, movie_base_id, cinema_id, time, begin, end, hall, lang, date, seats_num):
        result = []
        movie = MovieDetail.objects.get(movie_name=MovieBase.objects.get(id=movie_base_id).movie_name)
        cinema = Cinemas.objects.get(id=cinema_id)
        seats_list = re.findall('\d+', seats_num) #6 6_7
        if len(seats_list) == 1:
            row, col = query.getSeats(seats_list[0])
            seats = str(row) + "排" + str(col) + "座"
        else:
            row1, col1 = query.getSeats(seats_list[0])
            row2, col2 = query.getSeats(seats_list[1])
            seats = str(row1) + "排" + str(col1) + "座" + "," + str(row2) + "排" + str(col2) + "座"
        result.append({
            "movie_name": movie.movie_name,
            "seats": seats,
            "price": int(cinema.price) * len(seats_list),
            "time": query.time_format(date) + " " + begin,
            "vision": movie.vision,
            "end": end,
            "hall": hall,
            "lang": lang,
            "duration": movie.duration,
            "cinema_name": cinema.cinema_name,
            "address": cinema.address,
            "introduction": movie.introduction,
            "pic": "image/" + movie.movie_name + '_pic.jpg',
            'timg': 'image/' + movie.movie_name + '_timg.jpg',
            "date": date
        })
        return Response(result)