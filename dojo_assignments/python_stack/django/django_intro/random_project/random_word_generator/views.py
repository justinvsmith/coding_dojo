from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0


    return render(request, "index.html")

def result(request):
    request.session['counter'] += 1

    request.session['count'] = get_random_string(length=14)

    if request.session['counter'] == 10:
        request.session.flush()
        return redirect('/')

    return render(request, "random_word.html")
