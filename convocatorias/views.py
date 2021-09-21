from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Convocatoria, Entidad, Contacto, Caracterizacion
#from .filtersets import ConvocatoriaFilter
from .filters import ConvocatoriaFilter
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

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

#class ConvocatoriaListView (ListView):
'''
class ConvocatoriaListView (ListView):

    model = Convocatoria
    paginate_by = 2
    filterset_class = ConvocatoriaFilter
    #context_object_name = 'lista_convocatorias'
    #queryset = Convocatoria.objects.all()
    #context_object_name = 'convocatoria_list'
    template_name = 'convocatorias/convocatoria_list.html'
    def get_queryset(self):
        return Convocatoria.objects.filter(estadoConvocatoria__icontains='publicada')
'''

#class ConvocatoriaListView (generic.ListView):
#class ConvocatoriaList (FilterView):
class SearchResultsListView (FilterView):
    model = Convocatoria
    #context_object_name = 'lista_convocatorias'
    #queryset = Convocatoria.objects.all()
    context_object_name = 'convocatorias_search'
    template_name = 'convocatorias/convocatoria_list.html'
    filterset_class = ConvocatoriaFilter
    paginate_by = 6

    def get_queryset (self):
        query = self.request.GET.get('q',  default="")

        consulta = Convocatoria.objects.filter(
        Q(tituloConvocatoria__icontains=query) |
        Q(descripcion__icontains=query)
        ).order_by('fechaPublicacion')

        '''
        #posts per page
        paginator = Paginator(consulta, 3)
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        context = {
            "object_list" : queryset,
        }'''
        return consulta.filter(estadoConvocatoria__icontains='publicada')
        #return Convocatoria.objects.filter(estadoConvocatoria__icontains='publicada')

class ConvocatoriaDetailView (generic.DetailView):
    model = Convocatoria

class ConvocatoriaCreate(CreateView):
    model = Convocatoria
    fields = ['tituloConvocatoria', 'descripcion', 'paginaWebAplicacion']
    template_name =  'convocatorias/enviar.html'

    def get_success_url(self):
         messages.add_message(self.request, messages.INFO, 'Gracias por envíar los datos de la convocatoria...')
         return reverse('convocatorias')
