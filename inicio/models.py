from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    artista = models.CharField(max_length=100)
    tour = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = RichTextField()
    attachment = models.ImageField(upload_to='attachments', null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.id} - {self.artista} - {self.tour} - {self.fecha}'