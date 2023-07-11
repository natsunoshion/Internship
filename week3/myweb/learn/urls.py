from django.urls import path

from .views import index, login, register, welcome


urlpatterns = [
    path('', index),
    path('login/', login),
    path('register/', register),
    path('welcome/', welcome),
]
