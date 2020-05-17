from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new_show),
    path('create', views.create_show),
    path('<int:show_id>', views.one_show),
    path('<int:show_id>/edit', views.edit_show),
    path('<int:show_id>/update', views.update_show),
    path('<int:show_id>/destroy', views.delete_show)
]