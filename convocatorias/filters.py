import django_filters
from .models import *

class ConvocatoriaFilter (django_filters.FilterSet):
    #name = django_filters.CharFilter (lookup_expr='iexact')

    class Meta:
        model = Convocatoria
        fields = ['entidadID']
