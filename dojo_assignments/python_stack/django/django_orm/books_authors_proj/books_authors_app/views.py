from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
def index(request):
    context = {
        "headers" : ['ID', 'Title','Action'],
        "books" : Book.objects.all()
    }
    return render(request, "index.html", context)

def create_book(request):
    create_book = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )

    return redirect('/')

def create_author(request):
    create_author = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def authors(request):
    context = {
        "headers" : ['ID', 'Name', 'Action'],
        "authors" : Author.objects.all(),

    }
    return render(request, "authors.html", context)

def author_page(request, author_id):
    context = {
        "an_author" : Author.objects.get(id=author_id),
        "books" : Book.objects.all(),
    }
    return render(request, "author.html", context)

def books(request, book_id):
    context = {
        "headers" : ['ID', 'Title', 'Action'],
        "authors" : Author.objects.all(),
        "a_book" : Book.objects.get(id=book_id)
    }
    return render(request, "books.html", context)

def add_book(request):
    author_id = request.POST['author_id']
    if request.method == "POST":
        this_author = Author.objects.get(id = request.POST['author_id']) 
        this_book = Book.objects.get(id=request.POST['book_id'])
        this_book.authors.add(this_author)
        
        return redirect(f"authors/{author_id}")
    
def add_author(request):
    book_id = request.POST['book_id']
    if request.method == "POST":
        if request.method == "POST":
            this_author = Author.objects.get(id = request.POST['author_id']) 
        this_book = Book.objects.get(id=request.POST['book_id'])
        this_author.books.add(this_book)

        return redirect(f"books/{book_id}")