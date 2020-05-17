from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        "shows" : Show.objects.all(),   
        "headers" : ['ID', 'Title', 'Network', 'Release Date', 'Actions']
    }
    return render(request, "shows.html", context)

def new_show(request): 
    return render(request, "new_show.html")

def create_show(request): 
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/new")
    else:
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        messages.success(request, "Show successfully created")

    return redirect(f"/shows/{new_show.id}")

def one_show(request, show_id): 
    context = {
        "shows" : Show.objects.get(id=show_id)
    }
    return render(request, "view_show.html", context)

def edit_show(request, show_id):
    context = {
        "edit_show" : Show.objects.get(id=show_id),
    }

    return render(request, "edit_show.html", context)

def update_show(request, show_id): 
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    else:
        edit_show = Show.objects.get(id=show_id)
        edit_show.title = request.POST['title']
        edit_show.network = request.POST['network']
        edit_show.release_date = request.POST['release_date']
        edit_show.description = request.POST['description']
        edit_show.save()
    return redirect(f"/shows/{show_id}")

def delete_show(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows/')
