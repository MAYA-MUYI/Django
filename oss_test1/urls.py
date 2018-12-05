"""oss_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from file import views
from search import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('upload/', views.upload_file, name="upload"),
    path('download/', views.download_file, name="download"),
    path('search/', v.search, name="search"),
    path('search/<src>/', v.detail, name="detail"),
    path('user/', include('user.urls')),
]
