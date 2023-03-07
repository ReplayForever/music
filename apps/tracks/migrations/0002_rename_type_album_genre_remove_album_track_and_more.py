# Generated by Django 4.1.7 on 2023-03-04 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='type',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='album',
            name='track',
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='track', to='tracks.album', verbose_name='Альбом'),
            preserve_default=False,
        ),
    ]