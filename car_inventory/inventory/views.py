from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente

class CarListView(ListView):
    model = Car
    template_name = 'inventory/car_list.html'
    context_object_name = 'cars'

class CarCreateView(CreateView):
    model = Car
    template_name = 'inventory/car_form.html'
    fields = ['marca', 'modelo', 'año', 'precio', 'color', 'kilometraje', 'disponible']
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'inventory/car_form.html'
    fields = ['marca', 'modelo', 'año', 'precio', 'color', 'kilometraje', 'disponible']
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'inventory/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
    

class ClienteListView(ListView):
    model = Cliente
    template_name = 'inventory/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'inventory/cliente_form.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'activo']
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'inventory/cliente_form.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'activo']
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'inventory/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')