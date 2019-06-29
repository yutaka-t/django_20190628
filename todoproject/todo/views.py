from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

from .models import TodoModel


def todo(request):
    return HttpResponse('デフォルトページ')


class TodoList(ListView):
    template_name = 'list.html'

    # どのモデルを使うかを指定
    model = TodoModel
