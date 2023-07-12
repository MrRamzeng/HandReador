from django.urls import path
from .views import Books, BookDetailView

urlpatterns = [
    path('', Books.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book'),
]