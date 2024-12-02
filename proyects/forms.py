from django import forms
from .models import Proyect

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ['nombre', 'rut', 'correo']  # Actualizamos los nombres de los campos
