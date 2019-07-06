#!/usr/bin/env python
# -*- coding：utf-8 -*-
'''
@author: maya
@contact: 1278077260@qq.com
@software: Pycharm
@file: apiview.py
@time: 2019/6/9 22:40
@desc:
'''
# in useraccesscontrol/apiview.py

# 导入Django原生的User模型
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


from rest_framework import generics

from .serializers import UserSerializer  # 这个序列化器暂时还没有编写


# 编写创建用户的视图
class UserCreate(generics.CreateAPIView):
    name = 'user_create'

    # authentication_classes = ()
    def get_authenticators(self):
        return ()

    # permission_classes = ()
    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return UserSerializer


class UserList(generics.ListAPIView):
    name = 'user_list'

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserRetrieve(generics.RetrieveAPIView):
    name = 'user'

    def get_authenticators(self):
        return ()

    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()


class LoginView(APIView):
    name = 'login'

    # permission_classes = ()
    def get_permissions(self):
        return ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                data={
                    'token': user.auth_token.key,
                }
            )
        else:
            return Response(
                data={
                    'error': '认证失败，请确认账号和密码是否正确',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )