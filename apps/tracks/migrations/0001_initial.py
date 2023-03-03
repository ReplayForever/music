# Generated by Django 4.1.7 on 2023-03-03 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор записи по стандарту UUID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Дата последнего изменения')),
                ('title', models.CharField(max_length=200, verbose_name='Название трека')),
                ('year', models.DateField(verbose_name='Год выхода трека')),
            ],
            options={
                'verbose_name': 'Аудиозапись',
                'verbose_name_plural': 'Аудиозаписи',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный идентификатор записи по стандарту UUID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Дата последнего изменения')),
                ('title', models.CharField(max_length=200, verbose_name='Название альбома')),
                ('year', models.DateField(verbose_name='Год выхода альбома')),
                ('type', models.IntegerField(choices=[(1, 'Рок'), (2, 'Электроника'), (3, 'Хип-Хоп'), (4, 'Попса')], verbose_name='Тип')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='tracks.track', verbose_name='Трек')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]