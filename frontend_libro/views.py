from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from .models import Libro

def index(request):
    libros = Libro.objects.all()
    return render(request, 'frontend_libro/index.html', {'libros': libros})

def agregar_libro(request):
    if request.method == "POST":
        if request.POST['titulo'] and request.POST['precio'] and request.POST['autor'] :
            nuevo_libro=Libro(
               titulo=request.POST['titulo'],
               precio=request.POST['precio'],
               autor=request.POST['autor'],
            )
            nuevo_libro.save()
            return redirect('index')
        else:
            return redirect('agregar_libro.html')
    return render(request,'frontend_libro/agregar_libro.html')


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == "POST":
        if request.POST['titulo'] and request.POST['autor'] and request.POST['precio']:
            libro.titulo = request.POST['titulo']
            libro.precio = request.POST['precio']
            libro.autor = request.POST['autor']
            libro.save()
            return redirect('index')

    return render(request, 'frontend_libro/editar_libro.html', {'libro': libro})


def borrar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('index')

    