from rest_framework.generics import ListAPIView
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkListAPIView(ListAPIView):
    queryset = Artwork.objects.all().order_by('-published_date')
    serializer_class = ArtworkSerializer
