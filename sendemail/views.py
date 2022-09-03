from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = 'ManuelUrizar1@outlook.com'
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["ManuelUrizar1@outlook.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "sendemail/email.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

def ShowChatHome(request):
    return render(request, 'sendemail/chatHome.html')

def ShowChatPage(request, room_name, person_name):
    return render(request, 'sendemail/chatRoom.html', {'room_name':room_name, 'person_name':person_name})