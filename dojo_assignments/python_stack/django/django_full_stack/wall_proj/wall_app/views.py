from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def wall_home(request): 
    context = {
        "users" : User.objects.all()
    }
    return render(request, "wall.html", context)


def newMessage(request):
    new_message = Message.objects.create(
        message = request.POST['message']
    )
    return redirect('/wall/post_msg')

def postMessage(request):
    context = {
        'messages' : Message.objects.all()
    }
    return render(request, "wall.html", context)