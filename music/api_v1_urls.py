from django.urls import include, path


urlpatterns = [
    path('music/', include('apps.tracks.urls')),
    path('auth/', include('dj_rest_auth.urls'))
]
