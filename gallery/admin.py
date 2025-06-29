from django.contrib import admin
from .models import Artwork


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date', 'date_uploaded', 'price')
    list_filter = ('published_date',)
    search_fields = ('title', 'description')