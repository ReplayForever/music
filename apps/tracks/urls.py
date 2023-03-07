from django.urls import path, include
from rest_framework import routers

from apps.tracks.views import AlbumViewSet, TrackViewSet

router = routers.DefaultRouter()
router.register('album', AlbumViewSet)
router.register('track', TrackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
