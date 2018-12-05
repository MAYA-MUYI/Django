from django import template
import os
import oss2
import json

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAIwmIDMn3td8tv')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '7KVaHZZQdOqVsiaftwWOBvLYL2sHaM')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')
path = os.path.abspath('.')
dir_path = os.path.abspath('static/media')
dirs = os.listdir(path)
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name="maya-music")


register = template.Library()

@register.simple_tag
def get_tag_url(object_):
    base_url = "https://maya-music.oss-cn-beijing.aliyuncs.com/"
    files_name = []
    url_list = {}
    # 打印出云端每个文件的名字，将名字存入files_name列表
    for i in oss2.ObjectIterator(bucket):
        files_name.append(i.key[:-4])
    print("************files_name")
    print(files_name)
    # 拼接出所有链接，存入url_list字典
    for name in files_name:
        url_list[name] = base_url + name
    print("********url********")
    print(url_list)
    return url_list[object_]

@register.simple_tag
def get_singer(object_):
    pass


# def get_src(object_):
#     pass





