from django import forms
from django.forms.widgets import FileInput
from inicio.models import Post
from ckeditor.fields import RichTextFormField

class BasePostFormulario(forms.Form):
    artista = forms.CharField(max_length=100)
    tour = forms.CharField(max_length=100)
    fecha = forms.DateField()
    descripcion = RichTextFormField()
    attachment = forms.ImageField(required=False, widget=FileInput())

class CrearPostFormulario(BasePostFormulario):
    class Meta:
        model = Post
        fields = ['artista', 'tour', 'fecha', 'descripcion', 'attachment']

class ActualizarPostFormulario(BasePostFormulario):
    class Meta:
        model = Post
        fields = ['artista', 'tour', 'fecha', 'descripcion', 'attachment']

class BusquedaPostFormulario(forms.Form):
    artista = forms.CharField(max_length=100, required=False)
