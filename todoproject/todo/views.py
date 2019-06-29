from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import TodoModel


def todo(request):
    return HttpResponse('デフォルトページ')


class TodoList(ListView):
    template_name = 'list.html'

    # どのモデルを使うかを指定
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel

    # 【必須】どの項目を編集項目として出すかを指定
    fields = ('title', 'memo', 'priority', 'duedate')
    # 【必須】POST後に遷移するURLを指定　or get_absolute_urlメソッドにて指定
    # class Base の場合は、reverse_lazy, method base の場合は、reverse を使う
    success_url = reverse_lazy('todo:todo_list')


class Tododelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('todo:todo_list')
