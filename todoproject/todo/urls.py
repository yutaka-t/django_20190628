from django.contrib import admin
from django.urls import path, include

from . import views
from .views import TodoList, TodoDetail, TodoCreate, Tododelete

app_name = 'todo'

urlpatterns = [
    path('',  views.todo, name='todo'),
    path('list/',  TodoList.as_view(), name='todo_list'),
    path('detail/<int:pk>',  TodoDetail.as_view(), name='todo_detail'),
    path('create/',  TodoCreate.as_view(), name='todo_create'),
    path('delete/<int:pk>',  Tododelete.as_view(), name='todo_delete'),
]

