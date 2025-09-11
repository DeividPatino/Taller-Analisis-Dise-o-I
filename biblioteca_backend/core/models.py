from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuario con roles
class Usuario(AbstractUser):
    ROLES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')

# Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# Reservas
class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

# Préstamos
class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)