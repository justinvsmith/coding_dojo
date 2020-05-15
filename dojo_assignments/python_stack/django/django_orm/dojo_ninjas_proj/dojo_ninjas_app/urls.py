from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new_ninja', views.newNinja),
    path('new_dojo', views.newDojo)
]