"""data URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/positions/
    path('chart/', views.chart, name="chart"),
    path('tables/', views.tables, name="tables"),
    path('calendar/', views.calendar, name="calendar"),
    path('list/', views.positions_list, name="positions_list"),
    path('type/<str:catename>/', views.search_by_catename, name="search_by_catename"),
    path('detail/<int:positions_pk>/', views.positions_detail, name="positions_detail"),
    path('error/', views.error, name="error"),

]
