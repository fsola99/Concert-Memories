from django.urls import path
from inicio.views import inicio, posts, crear_post, eliminar_post, actualizar_post, detalle_post

urlpatterns = [
    path('', inicio, name='inicio'),
    path('posts/', posts, name='posts'),
    path('posts/crear/', crear_post, name='crear_post'),
    path('posts/<int:post_id>/', detalle_post, name='detalle_post'),
    path('posts/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post'),
    path('posts/<int:post_id>/actualizar/', actualizar_post, name='actualizar_post'),
]
