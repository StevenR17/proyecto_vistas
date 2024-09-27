from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
#importamos las vistas genericas del framework
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#importamos el model pais
from .models import Pais

# Create your views here.


# Vista para listar los países
class PaisListView(ListView):
    model = Pais
    template_name = 'pais_list.html'
    context_object_name = 'paises'

# Vista para crear un nuevo país
class PaisCreateView(CreateView):
    model = Pais
    template_name = 'catalogo/pais_form.html'
    fields = ['nombre', 'codigo']
    success_url = reverse_lazy('pais_list')

# Vista para actualizar un país existente
class PaisUpdateView(UpdateView):
    model = Pais
    template_name = 'catalogo/pais_form.html'
    fields = ['nombre', 'codigo']
    success_url = reverse_lazy('pais_list')

# Vista para eliminar un país
class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'catalogo/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
