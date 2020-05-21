from django.shortcuts import render, HttpResponse, redirect

def list_surveys(request):
    return HttpResponse("placeholder to later display all the list of users")

def createNew(request):
    return HttpResponse("placeholder for users to add a new survey")
