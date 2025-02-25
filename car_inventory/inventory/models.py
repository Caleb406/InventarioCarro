from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Car(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cars', null=True, blank=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    kilometraje = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"