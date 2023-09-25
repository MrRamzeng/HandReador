from django.contrib import admin

from .models import Author, Country, Genre, Keycap, Symbol, Book, Language, Series

admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Keycap)
admin.site.register(Symbol)
admin.site.register(Series)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'title', 'get_authors']
    list_per_page = 20
    list_display_links = ['title']

    fieldsets = (
        (
            'О книге',
            {
                'fields': (
                    'authors', 'genres', ('series', 'series_number'),
                    ('title', 'image', 'language', 'publication_date'),
                )
            }
        ),
        (
            None,
            {
                'fields': ('text',)
            }
        )
    )

    @admin.display(description='Авторы')
    def get_authors(self, obj):
        return obj.get_authors()['data']
