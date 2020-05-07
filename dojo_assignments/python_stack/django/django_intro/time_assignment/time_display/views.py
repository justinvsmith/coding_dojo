from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime 

now = datetime.now()

def index(request):
    context = {
        "date" : now.strftime("%b %d, %Y"),
        "time" : now.strftime("%I:%M %p"),
        "intro" : "The current time and date:"
    }
    return render(request, "index.html", context)