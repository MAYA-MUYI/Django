import os
from django.shortcuts import get_object_or_404

import oss2
from django.shortcuts import render, redirect
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'Your ACCESS_KEY_ID')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'Your ACCESS_KEY_SECRET')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')
path = os.path.abspath('.')
dir_path = os.path.abspath('static/media')
dirs = os.listdir(path)
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name="maya-music")

def get_filesname():
    files_name = []  # 歌曲名字
    for i in oss2.ObjectIterator(bucket):
        files_name.append(i.key[:-4])
    return files_name

def get_picname(list_):
    pic_name = []  # 图片全称
    for name in list_:
        pic_name.append("https://maya-picture.oss-cn-beijing.aliyuncs.com/"+name+".jpg")
    return pic_name

def get_singer(list_):
    singers = []  # 歌手名字
    for name in list_:
        s_name =  name.split(' - ')[0]
        singers.append(s_name)
    return singers

def search(request):
    search_page = request.POST.get('name')
    # search_page = input("请输入")
    search_song = []
    search_singer = []
    context = {}
    files_name = get_filesname()
    for name in files_name:
        if search_page in name:
            search_song.append(name)
    search_singer = get_singer(search_song)
    search_pic = get_picname(search_song)
    context['search_song'] = search_song
    context['search_singer'] = search_singer
    context['search_pic'] = search_pic
    context['result'] = list(zip(search_song, search_singer, search_pic))
    context['src'] = search_song
    for x,y,z in zip(context['search_song'],context['search_singer'],context['search_pic']):
        print("song:%s singer:%s pic:%s" %(x,y,z))

    return render(request, 'file/search_list.html', context)
    # return render(request, 'file/list.html', context)

def detail(request, src):
    ##   src  ==  歌曲名字
    song_name = []
    singer_name = []
    pic_src = []
    song_name.append(src)
    singer_name.append(src.split(' - ')[0])
    pic_src.append("https://maya-picture.oss-cn-beijing.aliyuncs.com/"+src+".jpg")
    context = {}
    context['result'] = list(zip(song_name,singer_name,pic_src))
    print("song_name:%s,singer:%s,pic:%s" %(song_name, singer_name, pic_src))
    return render(request, 'file/search_detail.html', context)

