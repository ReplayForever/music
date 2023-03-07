from django.urls import path, include
from rest_framework import routers

from apps.tracks.views import AlbumViewSet

router = routers.DefaultRouter()
router.register('', AlbumViewSet)

urlpatterns = [
    path('album', include(router.urls)),
]