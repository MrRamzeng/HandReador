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
        context['keys_m'] = [15, 28]
        context['keys_l'] = [14, 29, 41]
        context['keys_xl'] = [42, 53]
        context['keys_xxl'] = [55, 56]
        context['keycaps'] = Keycap.objects.all()
        return context
