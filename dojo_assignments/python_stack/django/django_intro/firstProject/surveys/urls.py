from django.urls import path     
from . import views
urlpatterns = [
    path('surveys', views.list_surveys),
    path('new', views.createNew),
]