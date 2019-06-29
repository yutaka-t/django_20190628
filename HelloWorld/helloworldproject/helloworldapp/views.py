from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def hello_function(request):
    return HttpResponse('Hello')


# class Based View
# ある程度自動化される。
class HelloworldView(TemplateView):
    template_name = 'hello.html'

