from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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