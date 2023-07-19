from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Keycap


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keycaps'] = Keycap.objects.all()
        return context
