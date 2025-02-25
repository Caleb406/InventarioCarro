from django.urls import path
from .views import (
    CarListView, CarCreateView, CarUpdateView, CarDeleteView,
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
)

urlpatterns = [
    # Página principal - Lista de carros
    path('', CarListView.as_view(), name='car_list'),
    
    # Formulario para agregar nuevo carro
    path('nuevo/', CarCreateView.as_view(), name='car_create'),
    
    # Formulario para editar un carro existente
    path('editar/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    
    # Confirmación para eliminar un carro
    path('eliminar/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
    
    # URLs de Clientes
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]