from django.utils.translation import gettext_lazy as _
from django.db import models


class Genres(models.IntegerChoices):
    ROCK = 1, _('Рок')
    ELECTRONIC = 2, _('Электроника')
    HIPHOP = 3, _('Хип-Хоп')
    POP = 4, _('Попса')
