"""Определяет схемы URL для learning_logs."""

from django.urls import path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]