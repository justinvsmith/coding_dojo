from django.urls import path     
from . import views
urlpatterns = [
    path('', views.list_users),
    path('new', views.createNew),
    path('login', views.logIn),
    path('register', views.registerUser)
]