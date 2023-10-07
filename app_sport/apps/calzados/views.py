from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import *
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

class AgregarCategoria(CreateView, LoginRequiredMixin):
    model = Categorias
    fields = ['nombre']
    template_name = 'calzados/agregar_categoria.html'
    success_url = reverse_lazy('inicio')


class AgregarCalzados(CreateView, LoginRequiredMixin):
    model = Calzados
    fields = ['titulo', 'autor', 'descripcion', 'imagen', 'categoria']
    template_name = 'calzados/agregar_calzados.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)
    
class ModificarCalzados(LoginRequiredMixin, UpdateView):
    model = Calzados
    fields = ['titulo', 'autor', 'descripcion', 'imagen', 'categoria']
    template_name = 'calzados/agregar_calzados.html'
    success_url = reverse_lazy('apps.calzados:listar_calzados')


class EliminarCalzados(LoginRequiredMixin, DeleteView):
    model = Calzados
    template_name = 'calzados/confirma_eliminar.html'
    success_url = reverse_lazy('apps.calzados:listar_libros')



class ListarCalazados(ListView):
    model = Calzados
    template_name = 'calzados/listar_calzados.html'
    context_object_name = "calzados"
    # -----Paginación------
    # paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context


    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')
    
# class LibroDetalle(DetailView):
#     model = Libros
#     template_name = 'libros/libro.html'
#     context_object_name = 'libro'

def ListarCalzadosPorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre=categoria)
    calzados = Calzados.objects.filter(
        categoria=categorias2[0].id).order_by('fecha_agregado')
    categorias = Categorias.objects.all()
    template_name = 'calzados/listar_calzados.html'
    contexto = {
        'calzados': calzados,
        'categorias': categorias
    }
    return render(request, template_name, contexto)


def calzados_detalle(request, id):
    calzados = Calzados.objects.get(id=id)
    opiniones = Opinion.objects.filter(calzados=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.calzados = calzados
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'calzados': calzados,
        'form': form,
        'opiniones': opiniones,
    }
    template_name = 'calzados/calzados.html'
    return render(request, template_name, contexto)
