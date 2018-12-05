from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import unquote
from django.http import FileResponse
import os
import oss2
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
import shutil
import json


access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'Your ACCESS_KEY_ID')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'Your ACCESS_KEY_SECRET')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')
path = os.path.abspath('.')
dir_path = os.path.abspath('static/media')
dirs = os.listdir(path)
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name="maya-music")
now_pwd = os.getcwd()

def index(request):
    base_url = "https://maya-music.oss-cn-beijing.aliyuncs.com/"
    files_name = []
    url_list = []
    data = []
    # 打印出云端每个文件的名字，将名字存入files_name列表
    for i in oss2.ObjectIterator(bucket):
        files_name.append(i.key[:-4])
    # 拼接出所有链接，存入url_list字典
    for name in files_name:
        url_list.append(base_url + name + '.mp3')
    for song, src in zip(files_name, url_list):
        data.append({'song': song, 'src': src, 'singer': "黄耀明", 'img': 'static/css/img/hym.jpg', 'lyric': 'anyong'})
    return render(request, 'index.html', {'list': json.dumps(data, ensure_ascii=False)})


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#状态码为200则返回文本否则抛出异常
        r.encoding = 'utf-8'
        # r.encoding = r.apparent_encoding

        return r.text
    except:
        return "产生异常"

def get_data(html):
    src = BeautifulSoup(html, 'html.parser', from_encoding='utf-8').find('audio', {'id': 'audio'}).get('src')
    return src


def upload_file(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(dir_path, myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        with open(oss2.to_unicode(dir_path+"/"+myFile.name), 'rb') as f:
            bucket.put_object(myFile.name, f)
        temp_path = ".\static"
        os.chdir(os.path.abspath(temp_path))
        shutil.rmtree("media")
        os.mkdir("media")
        os.chdir(now_pwd)
        return redirect(request.GET.get('from', reverse('home')))


def download_file(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    url = "http://127.0.0.1:8000/"
    html = getHTMLText(url)
    src = get_data(html)
    file_name = unquote(src, 'utf-8').split('com/')[1]
    temp_path2 = ".\static\cloud"
    os.chdir(os.path.abspath(temp_path2))
    print("***************")
    print("cloud:", os.getcwd())
    bucket.get_object_to_file(file_name, file_name)
    file = open(file_name, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="music.mp3"'
    # file.close()
    # os.remove(file_name)
    os.chdir(now_pwd)
    return response
           # redirect(request.GET.get('from', reverse('home')))

    # return redirect(request.GET.get('from', reverse('home')))

