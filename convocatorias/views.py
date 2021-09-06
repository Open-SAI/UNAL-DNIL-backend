from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView

from .models import Convocatoria, Entidad, Contacto, Caracterizacion
#from .filtersets import ConvocatoriaFilter
from .filters import ConvocatoriaFilter

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

#class ConvocatoriaListView (generic.ListView):
#class ConvocatoriaList (FilterView):
class SearchResultsListView (FilterView):
    model = Convocatoria
    #context_object_name = 'lista_convocatorias'
    #queryset = Convocatoria.objects.all()
    context_object_name = 'convocatorias_list'
    template_name = 'convocatorias/convocatoria_list.html'
    filterset_class = ConvocatoriaFilter
    paginate_by = 50

class ConvocatoriaDetailView (generic.DetailView):
    model = Convocatoria
