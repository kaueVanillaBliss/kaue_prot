from django.urls import path
from django.conf.urls.static import static
from biocomp_website import settings
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('software/', views.software, name='software'),
    path('galeria/', views.galeria, name='galeria'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('contato/', views.contato, name='contato'),
    path('kaue/', views.kaue, name='kaue'),
    path('pablo/', views.pablo, name='pablo'),
    path('jorge/', views.jorge, name='jorge'),
    path('joao/', views.joao, name='joao'),
    path('karine/', views.karine, name='karine'),
    path('wanderson/', views.wanderson, name='wanderson'),
    path('automodel', views.automodel, name='automodel'),
    path('automodel_client_download', views.automodel_client_download, name='automodel_client_download'),
    path('automodel_server_download', views.automodel_server_download, name='automodel_server_download'),
    path('automodel_tutorial', views.automodel_tutorial, name='automodel_tutorial'),
    path('galeria/', views.image_galeria, name='galeria'),
    path('galeria/full_image/<int:image_id>/', views.full_image, name='full_image'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
