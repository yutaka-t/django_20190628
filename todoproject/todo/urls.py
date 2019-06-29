from django.contrib import admin
from django.urls import path, include

from . import views
from .views import TodoList

app_name = 'todo'

urlpatterns = [
    path('',  views.todo, name='todo'),
    path('list/',  TodoList.as_view(), name='todo_list'),
]

