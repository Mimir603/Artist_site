from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='artworks/')
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
