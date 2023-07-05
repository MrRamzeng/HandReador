from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Country, Genre, Series, Book, Language

admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Language)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_cover', 'title', 'authors_admin']
    list_per_page = 20
    list_display_links = ['title']

    fieldsets = (
        (
            'О книге',
            {
                'fields': ('authors', 'genres', ('title', 'image', 'language'), )
            }
        ),
        (
            None,
            {
                'fields': ('text', )
            }
        )
    )

    def book_cover(self, obj):
        return mark_safe(f'<img scr="{obj.image.url}" height="250px" width="167px"/>')

    book_cover.short_description = 'Обложка'

    def authors_admin(self, obj):
        if obj.authors.count() > 1:
            return ', '.join([author.full_name() for author in obj.authors.all()])
        else:
            return obj.authors.first().full_name()

    authors_admin.short_description = 'авторы'
