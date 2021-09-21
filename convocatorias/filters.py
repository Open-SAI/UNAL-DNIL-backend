import django_filters

from .models import *

class ConvocatoriaFilter (django_filters.FilterSet):
    #name = django_filters.CharFilter (lookup_expr='iexact')
    #filtro_pais = django_filters.RangeFilter(
    #field_name='Convocatoria_Entidad__pais', lookup_expr='range'
    #)

    class Meta:
        model = Convocatoria
        fields = ['entidadID','entidadID_id__pais', 'areasOCDE']
