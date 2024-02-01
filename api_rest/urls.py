from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('ator/all', views.get_all_actors),
    path('ator/get', views.get_actor),
    path('ator/post', views.post_actor),
    path('diretor/all', views.get_all_directors),
    path('diretor/get', views.get_director),
    path('diretor/post', views.post_director),
    path('filme/all', views.get_all_films),
    path('filme/get', views.get_film),
    path('filme/post', views.post_film),
    path('filme/del', views.delete_film),
    path('filme/put', views.put_film),
    path('filme/films_by_actor', views.get_films_by_actor),
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/logout', views.logout),
]