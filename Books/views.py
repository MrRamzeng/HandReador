from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


class Books(ListView):
    model = Book
    ordering = 'id'
    template_name = 'books/index.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book.html'
