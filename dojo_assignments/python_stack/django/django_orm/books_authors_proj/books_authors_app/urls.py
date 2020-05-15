from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new_book', views.create_book),
    path('new_author', views.create_author),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.author_page),
    path('books/<int:book_id>', views.books),
    path('add_book', views.add_book),
    path('add_author', views.add_author)
]