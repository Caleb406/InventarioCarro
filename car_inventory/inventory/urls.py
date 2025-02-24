from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    # Página principal - Lista de carros
    path('', CarListView.as_view(), name='car_list'),
    
    # Formulario para agregar nuevo carro
    path('nuevo/', CarCreateView.as_view(), name='car_create'),
    
    # Formulario para editar un carro existente
    path('editar/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    
    # Confirmación para eliminar un carro
    path('eliminar/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
]