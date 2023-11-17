from django.shortcuts import render
from django.views import View  # Importa la clase base View

# Crea tu clase de vista heredando de View
class AboutMe(View):
    template_name = 'about/about.html'
    
    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        return render(request, self.template_name)
