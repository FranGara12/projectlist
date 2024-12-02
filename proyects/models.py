from django.db import models

class Proyect(models.Model):
    nombre = models.CharField(max_length=200)         # Cambiado de title a nombre
    rut = models.CharField(max_length=200)            # Cambiado de description a rut
    correo = models.EmailField(null=True, blank=True) # Cambiado de technology a correo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre







  