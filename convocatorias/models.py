from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
#from faicon.fields import FAIconField
#from fontawesome_5.fields import IconField
#from django.core.urlresolvers import reverse

# Create your models here.
class Entidad (models.Model):
    #Entidad Financiadora

    entidadID = models.AutoField(primary_key=True)
    nombreEntidad = models.CharField(max_length=200, help_text='Nombre Entidad Financiadora Convocatoria')
    paginaWeb = models.URLField(max_length=200,help_text='Página Web de la Entidad',null=True)
    pais = CountryField(blank_label='Seleccione el país')
#    logoEntidad = models.ImageField(upload_to='entidad_logos', null=True, blank=True)

    def __str__(self):
        #String object model
        return self.nombreEntidad

    class Meta:
        verbose_name_plural = 'Directorio de Entidades'


class Contacto (models.Model):

    entidadID = models.ForeignKey (Entidad,on_delete=models.CASCADE)

    contactoID = models.AutoField(primary_key=True)
    cargoContacto = models.CharField(max_length=200, help_text='Cargo Contacto',null=True)
    nombreContacto = models.CharField(max_length=200, help_text='Nombre Contacto')
    correoContacto = models.EmailField(max_length=254, help_text='Correo Electrónico Contacto')
    telefonoContacto = models.CharField(max_length=200, null=True, help_text='Teléfono de Contacto')
    telefonoContactoAux = models.CharField(max_length=200, null=True, blank=True, help_text='Teléfono de Contacto Auxiliar')

    class Meta:
        verbose_name_plural = 'Contactos Oficiales'

# Create your models here.
class Icono (models.Model):
    #Entidad Financiadora

    iconoID = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=200, help_text='Temática convocatoria')
    #iconoTematico = FAIconField(null=True)
    #iconoTem = models.ImageField(upload_to='icono_tematica', null=True)
    iconoTematico = models.CharField(max_length=30, help_text='Ingrese Código de Ícono', null=True)
    colorIcono = models.CharField(max_length=30, help_text='Ingrese Color', null=True)

    def __str__(self):
        #String object model
        return self.tema

    class Meta:
        verbose_name_plural = 'Iconografía Etiquetado Convocatoria'

class AreasOCDE (models.Model):
    areaID = models.AutoField(primary_key=True, blank=True)
    area = models.CharField (max_length=255, verbose_name="Área" )

    class Meta:
        verbose_name_plural = 'Áreas OCDE'


    def __str__(self):
        return f'{self.area}'

class Componente (models.Model):
    componenteID = models.AutoField(primary_key=True, blank=True)
    componente = models.CharField (max_length=255, verbose_name="Área" )

    class Meta:
        verbose_name_plural = 'Componentes Convocatoria'

    def __str__(self):
        return f'{self.componente}'

class Elegibilidad (models.Model):
    grupoID = models.AutoField(primary_key=True, blank=True)
    grupo = models.CharField (max_length=255, verbose_name="Área" )

    class Meta:
        verbose_name_plural = 'Elegibilidad Convocatoria'

    def __str__(self):
        return f'{self.grupo}'


class Convocatoria (models.Model):
    #Una entidad puede tener 0 ... n Convocatorias asociadas
    entidadID = models.ForeignKey('Entidad', on_delete=models.PROTECT, null=True, verbose_name="Entidad Otorgante")
    iconoID = models.ForeignKey('Icono', on_delete=models.PROTECT, null=True, verbose_name="Ícono Temático")
    #Una entidad tiene 1 caracterizacion asociada
    #caracterizacionID = models.ForeignKey('Caracterizacion', null=True, blank=True, on_delete=models.PROTECT )
    #caracterizacionID = models.OneToOneField (Caracterizacion,on_delete=models.PROTECT,null=True)

    convocatoriaID = models.AutoField(primary_key=True)
    tituloConvocatoria = models.CharField(max_length=500, help_text='Título de la Convocatoria')
    descripcion = models.TextField(max_length=2000, help_text='Resumen Convocatoria')
    fechaPublicacion = models.DateField(null=True, help_text='Fecha Publicación Convocatoria')
    fechaLimitePostulacion = models.DateField(null=True, help_text='Fecha Límite Postulación')
    paginaWebAplicacion = models.URLField(max_length = 500, null=True, help_text='Página Web para aplicaciones')
    imageRedes = models.ImageField(upload_to='convocatorias_img_preview', null=True, blank=True)

    OP_ESTADO = (
        ('publicada','Publicada'),
        ('revision','En Revisión'),
    )
    estadoConvocatoria = models.CharField(
        choices=OP_ESTADO,
        default='revision',
        max_length=30,
        help_text='¿Públicar la convocatoria?',
        editable=True,
    )

    OP_CREACION = (
            ('enviada','Enviada'),
            ('creada','Creada'),
    )
    creacionConvocatoria = models.CharField(
            choices=OP_CREACION,
            default='creada',
            max_length=30,
            help_text='¿Esta convocatoria fué enviada por la Comunidad Académica?',
            editable=False,
    )

    OP_VIGENCIA = (
            ('cerrada','Cerrada'),
            ('vigente','Vigente'),
    )
    vigencia = models.CharField(
            choices=OP_VIGENCIA,
            default='vigente',
            max_length=30,
            help_text='¿Se encuentra activa la convocatoria?',
            editable=True,
    )

    areasOCDE = models.ManyToManyField (
        to='convocatorias.AreasOCDE',
        related_name='areas_ocde',
        verbose_name="Áreas OCDE"
    )

    Componentes = models.ManyToManyField (
        to='convocatorias.Componente',
        related_name='componentes',
        verbose_name="Componentes Convocatoria"
    )

    elegibilidad = models.ManyToManyField (
            to='convocatorias.Elegibilidad',
            related_name='elegibilidad',
            verbose_name="Elegibilidad Convocatoria"
    )


    tags = TaggableManager()

    def get_elegibilidad_values (self):
        ret = ''
        for elegibilidad in self.elegibilidad.all():
            ret = ret + elegibilidad.grupo + ','

        return ret[:-1]

    def get_componentes_values (self):
        ret = ''
        for componentes in self.Componentes.all():
            ret = ret + componentes.componente + ','

        return ret[:-1]

    def get_areasocde_values (self):
        ret = ''
        for areas in self.areasOCDE.all():
            ret = ret + areas.area + ','

        return ret[:-1]


    class Meta:
#        ordering = ['fechaPublicacion']
        verbose_name_plural = 'Registro de Convocatorias'
#       verbose_name = 'Registro de Convocatorias'

    def __str__(self):
        #String object model
        return f'{self.tituloConvocatoria}'

    def get_absolute_url(self):
        #url access item
        #return reverse('convocatoria-detail',args[str(self.id)])
        return reverse('convocatoria-detail',args=[str(self.convocatoriaID)])



'''
    def save(self):
        if (present.date() < fechaLimitePostulacion):
            return False
        else:
            return True
'''



#class Caracterizacion (models.Model):
class Caracterizacion (models.Model):
    #Datos Caracterización Convocatoria
    #convocatoriaID = models.ForeignKey ('Convocatoria', on_delete=models.PROTECT, null=True)
    convocatoriaID = models.OneToOneField (Convocatoria,on_delete=models.CASCADE, null=True)


    tipoFinanciacion = models.CharField(max_length=500, help_text='¿Qué tipo de financiación aplica para la convocatoria?', verbose_name="Tipo de Financiación")
    montoBeneficio = models.CharField(max_length=500, help_text='¿Qué monto tiene la convocatoria?', verbose_name="Monto del Beneficio")
    descripcionBeneficio = models.CharField(max_length=2000, help_text='Descripción Beneficio Otorgado',null=True, verbose_name="Descripción del Beneficio Otorgado")

    OP_PERIODICA = (
            ('no','No'),
            ('si','Sí'),
    )
    periodica = models.CharField(
            max_length=2,
            choices=OP_PERIODICA,
            blank=True,
            default='n',
            help_text='¿Esta convocatoria es periódica?',
    )
    OP_PERIODICIDAD = (
            ('trimestral','trimestral'),
            ('anual','anual'),
            ('bianual','bianual'),
            ('na','no aplica'),
    )
    periodicidad = models.CharField(
            max_length=30,
            choices=OP_PERIODICIDAD,
            blank=True,
            default='na',
            help_text='¿qué periodicidad maneja esta convocatoria?',
    )
    OP_AMBITO = (
            ('local','local'),
            ('departamental','departamental'),
            ('nacional','nacional'),
            ('internacional','internacional'),
            ('na','no aplica'),
    )
    ambito = models.CharField(
            max_length=30,
            choices=OP_AMBITO,
            blank=True,
            default='na',
            help_text='¿cuál es el ámbito de la convocatoria?',
            verbose_name="Ámbito"
    )
    OP_AREAS_CONV = (
            ('ciencias_naturales','Ciencias Naturales'),
            ('ingenieria_tecnologia','Ingeniería y Tecnología'),
            ('ciencias_salud','Ciencias Médicas y de Salud'),
            ('ciencias_agricolas','Ciencias Agrícolas'),
            ('ciencias_sociales','Ciencias Sociales'),
            ('humanidades','Humanidades'),
            ('multidisciplinarias','Multidisciplinarias'),
    )
    areasConvocatoria = models.CharField(
            max_length=30,
            choices=OP_AREAS_CONV,
            blank=True,
            default='na',
            help_text='¿áreas de la convocatoria?',
    )

#    areasOCDE = models.ManyToManyField (
#        to='convocatorias.AreasOCDE',
#        related_name='areas_ocde',
#        verbose_name="Áreas OCDE"
#    )

    class Meta:
        verbose_name_plural = "Caracterización"
    #def __id__(self):
    #    return self.id
