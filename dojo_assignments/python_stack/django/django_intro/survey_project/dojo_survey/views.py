from django.shortcuts import render, HttpResponse, render

def index(request):
    return render(request, "index.html")

def result(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    referral_from_form = request.POST['referral']
    comments_from_form = request.POST['comments']
    contact_from_form = request.POST['contact']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form,
        "location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
        "referral_on_template" : referral_from_form,
        "comments_on_template" : comments_from_form,
        "contact_on_template" : contact_from_form
    }
    return render(request,"success.html", context)
    

def success(request):
    pass