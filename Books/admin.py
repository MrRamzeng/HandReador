from django.contrib import admin
from .models import Author, Country, Genre, Series, Book

admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Book)
