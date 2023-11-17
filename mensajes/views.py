# mensajes/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Mensaje
from django.contrib.auth.models import User

@login_required
def listar_mensajes(request):
    try:
        mensajes = Mensaje.objects.filter(receptor=request.user)
    except Mensaje.DoesNotExist:
        mensajes = []
        
    return render(request, 'mensajes/lista_mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensajes(request, receptor_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido', '')
        receptor = User.objects.get(pk=receptor_id)

        mensaje = Mensaje(emisor=request.user, receptor=receptor, contenido=contenido)
        mensaje.save()

        # Redirige a la lista de mensajes después de enviar
        return redirect('lista_mensajes')

    # Renderiza el formulario para enviar mensajes
    receptor = User.objects.get(pk=receptor_id)
    return render(request, 'mensajes/enviar_mensaje.html', {'receptor': receptor})

class ListaUsuariosView(ListView):
    model = User
    template_name = 'mensajes/lista_usuarios.html'
    context_object_name = 'usuarios'
