from django.contrib import admin

# Register your models here.
from .models import Entidad, Convocatoria, Caracterizacion, Contacto, Icono, AreasOCDE, Componente, Elegibilidad

#admin.site.register(Entidad)
#admin.site.register(Convocatoria)
#admin.site.register(Caracterizacion)

class ContactoInline(admin.StackedInline):
    model = Contacto
    extra = 0

class CaracterizacionInline(admin.StackedInline):
    model = Caracterizacion
    extra = 0

@admin.register(Icono)
class IconoInline(admin.ModelAdmin):
    model = Icono
    extra = 0

@admin.register(AreasOCDE)
class AreasOCDEInline(admin.ModelAdmin):
    model = AreasOCDE
    extra = 0

    list_display=['area']

@admin.register(Componente)
class ComponenteInline(admin.ModelAdmin):
    model = Componente
    extra = 0

@admin.register(Elegibilidad)
class ElegibilidadInline(admin.ModelAdmin):
    model = Elegibilidad
    extra = 0

@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):
    inlines = [CaracterizacionInline]

#    readonly_fields= ['vigencia',]

    list_display=['tituloConvocatoria', 'estadoConvocatoria']

#    def get_name(self, obj):
#        return obj.author.name

    def get_tags(self, post):
        tags = []
        for tag in post.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)

    get_tags.short_description = 'Etiquetas'
    get_tags.admin_order_field = 'tituloConvocatoria'


    class Meta:
        ordering = ['fechaPublicacion']
        verbose_name_plural = 'Registro de Convocatorias'


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    inlines = [ContactoInline,]
