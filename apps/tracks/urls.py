from django.urls import path, include
from rest_framework import routers

from apps.tracks.views import AlbumViewSet, TrackViewSet, SongwriterViewSet

router = routers.DefaultRouter()
router.register('album', AlbumViewSet)
router.register('track', TrackViewSet)
router.register('songwriter', SongwriterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
