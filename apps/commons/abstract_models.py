from django.contrib.auth.models import User
from django.db import models
from model_utils.fields import AutoCreatedField, UUIDField, AutoLastModifiedField


class AbstractModel(models.Model):
    id = UUIDField(
        primary_key=True,
        version=4,
        editable=False,
        verbose_name='Уникальный идентификатор записи по стандарту UUID',
    )
    created = AutoCreatedField(verbose_name='Дата создания')
    modified = AutoLastModifiedField(verbose_name='Дата последнего изменения')
    # creator = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name='Пользователь, создавший объект',
    # )
    # editor = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name='Последний пользователь, отредактировавший запись',
    # )

    class Meta:
        abstract = True
