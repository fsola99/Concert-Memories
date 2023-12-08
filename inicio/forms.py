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
    pass

class ActualizarPostFormulario(BasePostFormulario):
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['artista'].initial = self.instance.artista
            self.fields['tour'].initial = self.instance.tour
            self.fields['fecha'].initial = self.instance.fecha
            self.fields['descripcion'].initial = self.instance.descripcion

    def save(self):
        if self.instance:
            self.instance.artista = self.cleaned_data.get('artista')
            self.instance.tour = self.cleaned_data.get('tour')
            self.instance.fecha = self.cleaned_data.get('fecha')
            self.instance.descripcion = self.cleaned_data.get('descripcion')
            if self.cleaned_data.get('attachment'):
                self.instance.attachment = self.cleaned_data.get('attachment')
            self.instance.save()
        else:
            Post.objects.create(**self.cleaned_data)

class BusquedaPostFormulario(forms.Form):
    artista = forms.CharField(max_length=100, required=False)
