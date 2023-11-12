from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Post
from inicio.forms import CrearPostFormulario, BusquedaPostFormulario, ActualizarPostFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def posts(request):
    formulario = BusquedaPostFormulario(request.GET)
    if formulario.is_valid():
        artista_a_buscar = formulario.cleaned_data.get('artista')
        listado_de_posts = Post.objects.filter(artista__icontains=artista_a_buscar)
    
    formulario = BusquedaPostFormulario()
    return render(request, 'inicio/posts.html', {'formulario': formulario, 'listado_de_posts': listado_de_posts})

@login_required
def crear_post(request):
    if request.method == 'POST':
        formulario = CrearPostFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            artista = info_limpia.get('artista')
            tour = info_limpia.get('tour')
            fecha = info_limpia.get('fecha')
            descripcion = info_limpia.get('descripcion')
            attachment = info_limpia.get('attachment')
            
    
            post = Post(artista=artista.lower(), tour=tour, fecha=fecha, descripcion=descripcion, attachment=attachment)
            post.save()
            
            return redirect('posts')
        else:
            return render(request, 'inicio/crear_post.html', {'formulario': formulario})
        
    formulario = CrearPostFormulario()
    return render(request, 'inicio/crear_post.html', {'formulario': formulario})

@login_required
def eliminar_post(request, post_id):
    post_a_eliminar = Post.objects.get(id=post_id)
    post_a_eliminar.delete()
    return redirect("posts")

@login_required
def actualizar_post(request, post_id):
    post_a_actualizar = Post.objects.get(id=post_id)
    
    if request.method == "POST":
        formulario = ActualizarPostFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            post_a_actualizar.artista = info_nueva.get('artista')
            post_a_actualizar.tour = info_nueva.get('tour')
            post_a_actualizar.fecha = info_nueva.get('fecha')
            post_a_actualizar.descripcion = info_nueva.get('descripcion')
            post_a_actualizar.attachment = info_nueva.get('attachment')
            
            post_a_actualizar.save()
            return redirect('posts')
        else:
            return render(request, 'inicio/actualizar_posts.html', {'formulario': formulario})
    
    
    formulario = ActualizarPostFormulario(initial={'artista': post_a_actualizar.artista, 'tour': post_a_actualizar, 'fecha': post_a_actualizar.fecha,'descripcion': post_a_actualizar.descripcion,'attachment': post_a_actualizar.attachment})
    return render(request, 'inicio/actualizar_post.html', {'formulario': formulario})

def detalle_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'inicio/detalle_post.html', {'post': post})
