from django.shortcuts import render

from django.http import HttpResponse #possivelmente remover depois


# Create your views here.


def automodel(request):
    return render(
            request,
            'homepage/automodel.html'
        )

def automodel_client_download(request):
    return render(
            request,
            'homepage/automodel_client_download.html'
        )

def automodel_server_download(request):
    return render(
            request,
            'homepage/automodel_server_download.html'
        )

def automodel_tutorial(request):
    return render(
            request,
            'homepage/automodel_tutorial.html'
        )


# def htp_surflexdock(request):
# 	return HttpResponse("HTP Hello World")
    

def index(request):
    return render(request, 'index.html')
def software(request):
    return render(request, 'software.html')
def quemsomos(request):
    return render(request, 'quemsomos.html')
def galeria(request):
    return render(request, 'galeria.html')
def pesquisa(request):
    return render(request, 'pesquisa.html')
def contato(request):
    return render(request, 'contato.html')
def kaue(request):
    return render(request, 'kaue.html')
def karine(request):
    return render(request, 'karine.html')
def pablo(request):
    return render(request, 'pablo.html')
def jorge(request):
    return render(request, 'jorge.html')
def wanderson(request):
    return render(request, 'wanderson.html')
def joao(request):
    return render(request, 'joao.html')

def image_galeria(request):
    images = Image.objects.all()
    return render(request, 'galeria.html', {'images': images})
def full_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'full_image.html', {'image': image})

