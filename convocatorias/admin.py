from django.contrib import admin

# Register your models here.
from .models import Entidad, Convocatoria, Caracterizacion

#admin.site.register(Entidad)
#admin.site.register(Convocatoria)
#admin.site.register(Caracterizacion)

class CaracterizacionInline(admin.StackedInline):
    model = Caracterizacion
#    fk_name = 'convocatoriaID' 

@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):

    inlines = [CaracterizacionInline]

@admin.register(Entidad)
class ConvocatoriaAdmin(admin.ModelAdmin):

    inlines = []
