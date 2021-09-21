from django import forms
from .models import Entidad, Convocatoria, Caracterizacion, Contacto, Icono

# Públic Form Convocatoria
class ConvocatoriaForm(forms.ModelForm):
    
    class Meta:
        model = Convocatoria
        fields = "__all__"
