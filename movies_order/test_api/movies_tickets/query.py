#!/usr/bin/env python
# -*- coding：utf-8 -*-
'''
@author: maya
@contact: 1278077260@qq.com
@software: Pycharm
@file: query.py
@time: 2019/6/4 11:03
@desc:
'''
import re
import os
import json
table = {ord(f):ord(t) for f,t in zip(
     u'，。！？【】（）％＃＠＆１２３４５６７８９０',
     u',.!?[]()%#@&1234567890')}



def getText(name):
    if os.path.splitext(name)[-1] == '.json':
        with open('files/' + name, 'rb') as f:
            data = json.loads(f.read())
    else:
        with open('files/' + name + '.json', 'rb') as f:
            data = json.loads(f.read())
    return data

def date_format(day):
    date_list = re.findall('\d+', str(day))
    if len(date_list) == 2:
        date_list[0] = str(int(date_list[0]))
        date_list[1] = str(int(date_list[1]))
    elif len(date_list) == 3:
        date_list = date_list[1:]
        date_list[0] = str(int(date_list[0]))
        date_list[1] = str(int(date_list[1]))
    else:
        print("Error")
    return date_list[0] + '-' + date_list[1]


def recentList_format(recent_session):
    recent_session = list(set(recent_session))
    recent_session.sort()
    if len(recent_session) > 45:
        recent_session = recent_session[::5][:8]
    elif len(recent_session) >= 30:
        recent_session = recent_session[::3][:8]
    elif len(recent_session) >= 17:
        recent_session = recent_session[::2][:8]
    elif len(recent_session) > 8:
        recent_session = recent_session[:8]
    else:
        recent_session = recent_session
    return recent_session

def getData(movies, day):
    '''
    获取特定日期的电影场次
    :param movies:
    :param day:
    :return:
    '''
    today_result = []
    print(json.dumps(movies, ensure_ascii=False))
    #每一部电影
    for movie in movies:
        movie_name = movie['movie_name']
        if movie['star']:
            star = movie['star']
        else:
            star = "暂无评分"
        if movie['result']:
            # 所有天数的场次
            movie_sessions = movie['result']
            for session in movie_sessions:
                today = session[0]
                today_date = today["date"]
                today_session = today["session_result"]
                if day == today_date:
                    today_result.append({
                        "movie_name": movie_name,
                        "star": star,
                        "today_session": today_session
                    })
        else:
            return None
    return today_result



def test():
    files_list = os.listdir('files')
    a = files_list[0]
    with open('files/' + a, 'rb') as f:
        data = json.loads(f.read())
    return data



def file_format(file_name):
    return os.path.splitext(file_name)[0].translate(table)

def getSeats(num):
    return int(num)//17 + 1, int(num) % 17

def time_format(time):
    print(time)
    return re.findall('\d+', time)[0] + '月' + re.findall('\d+', time)[1] + '日'



if __name__ == '__main__':
    print(getSeats(198))
