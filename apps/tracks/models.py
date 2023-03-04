from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.commons.abstract_models import AbstractModel


class Album(AbstractModel):

    class Genres(models.IntegerChoices):
        ROCK = 1, _('Рок')
        ELECTRONIC = 2, _('Электроника')
        HIPHOP = 3, _('Хип-Хоп')
        POP = 4, _('Попса')

    title = models.CharField(blank=False, max_length=200, verbose_name='Название альбома')
    year = models.DateField(verbose_name='Год выхода альбома')
    genre = models.IntegerField(choices=Genres.choices, verbose_name='Тип')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title


class Track(AbstractModel):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Альбом',
        related_name='track',
    )
    title = models.CharField(blank=False, max_length=200, verbose_name='Название трека')
    year = models.DateField(verbose_name='Год выхода трека')

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'

    def __str__(self):
        return self.title
