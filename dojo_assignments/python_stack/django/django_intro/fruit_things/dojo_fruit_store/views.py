from django.shortcuts import render, HttpResponse

def index(request):
    context ={
        "count" : [0,1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "index.html", context)


def checkout(request):
    print("Got Post Info...........")
    context = {
        "strawberry_count" : int(request.POST['strawberries']),
        "raspberry_count" : int(request.POST['raspberry']),
        "apple_count" : int(request.POST['apple']),
        "name_from_form" : request.POST['name'],
        "id_from_form" : request.POST['id'],
        "count" : int(request.POST['strawberries']) + int(request.POST['raspberry']) + int(request.POST['apple'])
    }

    return render(request, "checkout.html", context)

def success(request):
    pass

