from django.shortcuts import render

from django.shortcuts import render
from .models import Image

def image_galeria(request):
    images = Image.objects.all()
    return render(request, 'galeria/galeria.html', {'images': images})

def full_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'full_image.html', {'image': image})