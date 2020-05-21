from django.shortcuts import render, HttpResponse, redirect

def list_users(request):
    return HttpResponse("placeholder to later display all the list of users")

def createNew(request):
    return redirect("/users/register")

def logIn(request):
    return HttpResponse("placeholder for users to log in")

def registerUser(request):
    return HttpResponse("placeholder for users to create a new user record")