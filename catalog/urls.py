from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('books/', views.BookListView.as_view(), name='books'),
]

