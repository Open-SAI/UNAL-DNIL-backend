from django.contrib import admin

# Register your models here.
from .models import Entidad, Convocatoria, Caracterizacion, Contacto

#admin.site.register(Entidad)
#admin.site.register(Convocatoria)
#admin.site.register(Caracterizacion)

class ContactoInline(admin.StackedInline):
    model = Contacto
    extra = 0 

class CaracterizacionInline(admin.StackedInline):
    model = Caracterizacion

@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):
    inlines = [CaracterizacionInline]

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    inlines = [ContactoInline,]
