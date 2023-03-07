from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.commons.abstract_models import AbstractModel


class Songwriter(AbstractModel):
    name = models.CharField(max_length=200, verbose_name='Группа')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Album(AbstractModel):

    class Genres(models.IntegerChoices):
        ROCK = 1, _('Рок')
        ELECTRONIC = 2, _('Электроника')
        HIPHOP = 3, _('Хип-Хоп')
        POP = 4, _('Попса')

    songwriter = models.ForeignKey(
        Songwriter,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
        related_name='album',
    )
    title = models.CharField(max_length=200, verbose_name='Название альбома')
    year = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1800), MaxValueValidator(2050)],
        verbose_name='Год выхода альбома',
    )
    genre = models.IntegerField(choices=Genres.choices, verbose_name='Тип')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title


class Track(AbstractModel):
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Альбом',
        related_name='track',
    )
    songwriter = models.ManyToManyField(
        Songwriter,
        verbose_name='Исполнитель',
        related_name='tracks',
    )
    title = models.CharField(blank=False, max_length=200, verbose_name='Название трека')
    year = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1800), MaxValueValidator(2050)],
        verbose_name='Год выхода трека',
    )

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'

    def __str__(self):
        return self.title
