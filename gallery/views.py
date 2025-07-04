import base64

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import ContentFile
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Artwork
from .forms import ContactForm
from .serializers import ArtworkSerializer


def gallery_view(request):
    artworks = Artwork.objects.all().order_by('-date_uploaded')
    return render(request, 'gallery/gallery_page.html', {'artworks': artworks})


def contact_view(request):
    success = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
            form = ContactForm()
    return render(request, 'gallery/contact.html', {
        'form': form,
        'success': success
    })


class ArtworkListAPI(APIView):
    def get(self, request):
        artworks = Artwork.objects.all().order_by('-date_uploaded')
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)


@csrf_exempt
def artwork_create_api(request):
    if request.metho == 'POST':
        try:
            data = json.loads(request.body)
            image_data = data.get('image_base64')
            title = data.get('title')
            description = data.get('description')
            published_date = data.get('published_date')

            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(imgstr), name=f'{title}.{ext}')

            artwork = Artwork.objects.create(
                title=title,
                description=description,
                published_date=published_date,
                image=image_file,
            )

            return JsonResponse({'message': 'Artwork created', 'id': artwork.id})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

