from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowChatHome, name="inicioChat"),
    path('room/<str:room_name>/<str:person_name>', ShowChatPage, name="Showchat"),
]