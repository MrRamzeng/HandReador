from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


def image_path(instance, file):
    return f'Authors/{instance.last_name} {instance.first_name}/{file}'


class Author(models.Model):
    last_name = models.CharField(_('Фамилия'), max_length=50)
    first_name = models.CharField(_('Имя'), max_length=50)
    patronymic = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    pseudonym = models.CharField(_('Псевдоним'), max_length=50, blank=True, null=True)
    photo = models.ImageField(_('Фото'), upload_to=image_path, blank=True, null=True)
    date_of_birth = models.DateField(_('Дата рождения'))
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    biography = models.TextField(_('Биография'))

    class Meta:
        verbose_name = _('автор')
        verbose_name_plural = _('авторы')

    def full_name(self):
        return self.pseudonym if self.pseudonym else f'{self.first_name[0]}. {self.last_name}'

    def __str__(self):
        return self.pseudonym if self.pseudonym else f'{self.last_name} {self.first_name}'


class Country(models.Model):
    name = models.CharField(_('Страна'), max_length=50)

    class Meta:
        verbose_name = _('страна')
        verbose_name_plural = _('страны')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(_('Название'), max_length=50)

    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')

    def __str__(self):
        return self.name


class Bibliography(models.Model):
    name = models.CharField(_('Название'), max_length=50)
    books = models.ManyToManyField('Book')

    class Meta:
        verbose_name = 'библиография'
        verbose_name_plural = 'библиографии'

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(_('Серия'), max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(_('Язык'), max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    authors = models.ManyToManyField('Author', verbose_name=_('Авторы'))
    genres = models.ManyToManyField('Genre', verbose_name=_('Жанр'), blank=True)
    image = models.ImageField('Обложка', blank=True, null=True)
    series = models.ForeignKey('Series', on_delete=models.SET_NULL, verbose_name=_('серия'), blank=True, null=True)
    series_number = models.PositiveSmallIntegerField(_('Порядок в серии'), blank=True, null=True)
    publication_date = models.DateField(_('Дата публикации'))
    text = models.TextField('текст')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True, verbose_name='Язык')

    class Meta:
        verbose_name = _('книга')
        verbose_name_plural = _('книги')

    def __str__(self):
        return f'{self.title}'

    def get_series(self):
        if self.series:
            return f'{self.series} ({self.series_number})'

    def get_authors(self):
        if self.authors.count() > 1:
            return {'data': ', '.join([author.full_name() for author in self.authors.all()]), 'title': 'Авторы'}
        return {'title': 'Автор', 'data': self.authors.first().full_name()}

    get_authors.short_description = 'Авторы'

    def get_image(self):
        return mark_safe(f'<img src="{self.image.url}" height="250px" width="167px"/>')

    get_image.short_description = 'Обложка'

    def get_genres(self):
        if self.genres.count() > 1:
            return ', '.join([genre.name for genre in self.genres.all()])
        return self.genres.first().name


class Keycap(models.Model):
    language = models.ForeignKey('Language', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Язык')
    symbol = models.CharField('Кнопка', max_length=10)
    position = models.PositiveIntegerField('Позиция')
    LEFT = 'Левый'
    RIGHT = 'Правый'
    SIDES = (
        (LEFT, 'Левый'),
        (RIGHT, 'Правый')
    )
    LITTLE = 1
    RING = 2
    MIDDLE = 3
    INDEX = 4
    THUMB = 5
    FINGERS = (
        (LITTLE, 'Мизинец'),
        (RING, 'Безымянный'),
        (MIDDLE, 'Средний'),
        (INDEX, 'Указательный'),
        (THUMB, 'Большой')
    )
    side = models.CharField(_('Сторона'), max_length=10, choices=SIDES, default=LEFT)
    finger = models.CharField(_('Палец'), max_length=15, choices=FINGERS, default=LITTLE)

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'
        ordering = ('position',)

    def get_finger(self):
        print(self.finger)

    def __str__(self):
        return f'{self.symbol} - {self.position}'

# class Finger(models.Model):
#
#     def __str__(self):
#         return f'{self.side} - {self.number}'
