from django.urls import path     
from . import views
urlpatterns = [
    path('', views.wall_home),
    path('new_msg', views.newMessage),
    path('post_msg', views.postMessage)
]