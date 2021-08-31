from django.shortcuts import render
from django.views import generic

from .models import Convocatoria, Entidad, Contacto, Caracterizacion

# Create your views here.
'''
def convocatorias(request):
    
    num_entidades = Entidad.objects.all().count()
    num_convocatorias = Convocatoria.objects.all().count()
    
    context = {
            'num_entidades' : num_entidades,
            'num_convocatorias' : num_convocatorias,
    }
    
    return render(request, 'convocatorias.html', context=context)
'''
def index(request):
    return render(request, 'index.html', {})

class ConvocatoriaListView (generic.ListView):
    model = Convocatoria
    context_object_name = 'lista_convocatorias'
    queryset = Convocatoria.objects.all()
    template_name = 'convocatorias/convocatoria_list.html'

class ConvocatoriaDetailView (generic.DetailView):
    model = Convocatoria
