from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc


name = 'boardapp'

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
]
