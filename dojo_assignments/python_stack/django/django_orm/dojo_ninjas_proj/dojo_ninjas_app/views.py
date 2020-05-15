from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
def index(request):
    context = {
        "dojos" : Dojo.objects.all(),
    }
    return render(request, "index.html", context)

def newNinja(request):
    new_ninja = Ninja.objects.create(
        dojo_id = Dojo.objects.get(id=int(request.POST['dojo_id'])),
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    return redirect('/')

def newDojo(request):
    new_dojo = Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        desc = request.POST['desc']
    )
    return redirect('/')
