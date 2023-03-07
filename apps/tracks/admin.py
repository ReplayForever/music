from django.contrib import admin

from apps.tracks.models import Album, Track, Songwriter


class AlbumAdmin(admin.ModelAdmin):
    pass


class TrackAdmin(admin.ModelAdmin):
    pass


class SongwriterAdmin(admin.ModelAdmin):
    pass


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Album, AlbumAdmin)
_register(Track, TrackAdmin)
_register(Songwriter, SongwriterAdmin)
