from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregarlibro/',views.agregar_libro,name='agregar_libro'),
    path('editarlibro/<int:id>', views.editar_libro, name='editar_libro'),
    path('borrarlibro/<int:id>', views.borrar_libro, name='borrar_libro'),
    # Add more URL patterns as needed
]
