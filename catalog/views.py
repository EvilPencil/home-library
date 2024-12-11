#from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Book, Author, BookInstance, Genre

from django.views import generic

def index(request):
    return render(request, 'index.html', context={})

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
    

def catalog(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Auto 'all()' default
    num_users=User.objects.count()

    return render(
        request,
        'catalog.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_users':num_users
            },
    )
