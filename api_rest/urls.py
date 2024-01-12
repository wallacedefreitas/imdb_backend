from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('user/manager/', views.user_manager),
    path('user/all', views.get_all_users),
    path('comments/manager/', views.comment_manager),
    path('comments/all', views.get_all_comments),
    path('hello/', views.hello_world),

]
