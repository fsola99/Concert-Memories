# mensajes/urls.py
from django.urls import path
from .views import listar_mensajes, enviar_mensajes, ListaUsuariosView

urlpatterns = [
    path('mensaje/', listar_mensajes, name='lista_mensajes'),
    path('mensaje/enviar/<int:receptor_id>/', enviar_mensajes, name='enviar_mensaje'),
    path('usuarios/', ListaUsuariosView.as_view(), name='lista_usuarios'),
]
