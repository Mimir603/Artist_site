from django.urls import path
from .views import ArtworkListAPI

urlpatterns = [
    path('api/artworks/', ArtworkListAPI.as_view(), name='artwork-list-api'),
]