from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .api_views import ArtworkListAPIView
from .views import artwork_create_api

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register_view, name='register'),
    path('artworks/', ArtworkListAPIView.as_view(), name='artwork-list'),
    path('api/', include('gallery.api_urls')),
    path('api/artworks/create/', artwork_create_api, name='artwork-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
