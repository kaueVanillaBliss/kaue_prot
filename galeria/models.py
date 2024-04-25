from django.db import models


from django.db import models

class Image(models.Model):
    # Seus campos de modelo aqui
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    class Meta:
        app_label = 'galeria'

