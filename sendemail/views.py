from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def ShowChatHome(request):
    return render(request, 'sendemail/chatHome.html')

def ShowChatPage(request, room_name, person_name):
    return render(request, 'sendemail/chatRoom.html', {'room_name':room_name, 'person_name':person_name})