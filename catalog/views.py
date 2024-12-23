#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, Book, Author, BookInstance, Genre

@login_required
def index(request):
    return render(request, 'index.html', context={})

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author

def catalog(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Auto 'all()' default
    num_users=User.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'catalog.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_users':num_users,
            'num_visits':num_visits # num_visits appended
            },
    )
