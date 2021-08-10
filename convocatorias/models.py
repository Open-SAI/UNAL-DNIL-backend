from django.db import models



# Create your models here.
class Entidad (models.Model):
    #Entidad Financiadora

    nombreEntidad = models.CharField(max_length=200, help_text='Nombre Entidad Financiadora Convocatoria')
    paginaWeb = models.URLField(max_length=200,help_text='Página Web de la Entidad',null=True)

    def __str__(self):
        #String object model
        return self.nombreEntidad

    class Meta:
        verbose_name_plural = 'Entidades'

class Contacto (models.Model):
    cargoContacto = models.CharField(max_length=200, help_text='Cargo Contacto',null=True)
    nombreContacto = models.CharField(max_length=200, help_text='Nombre Contacto')
    correoContacto = models.EmailField(max_length=254, help_text='Correo Electrónico Contacto')
    
    entidadID = models.ForeignKey (Entidad,on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Contactos Oficiales'



class Convocatoria (models.Model):
    #Convocatoria
    #Una entidad puede tener 0 ... n Convocatorias asociadas
    entidadID = models.ForeignKey('Entidad', on_delete=models.PROTECT, null=True, verbose_name="Entidad Otorgante")
    #Una entidad tiene 1 caracterizacion asociada
    #caracterizacionID = models.ForeignKey('Caracterizacion', null=True, blank=True, on_delete=models.RESTRICT)
    #caracterizacionID = models.OneToOneField (Caracterizacion,on_delete=models.PROTECT,null=True)

    tituloConvocatoria = models.CharField(max_length=500, help_text='Título de la Convocatoria')
    descripcion = models.TextField(max_length=2000, help_text='Resumen Convocatoria')
    fechaPublicacion = models.DateField(null=True, blank=True, help_text='Fecha Publicación Convocatoria')

    class Meta:
        ordering = ['fechaPublicacion']
        verbose_name_plural = 'Registro de Convocatorias'

    def __str__(self):
        #String object model
        return self.tituloConvocatoria
    
    def get_absolute_url(self):
        #url access item
        return reverse('convocatoria-detail',args[str(self.id)])

#class Caracterizacion (models.Model):
class Caracterizacion (models.Model):
    #Datos Caracterización Convocatoria
    #convocatoriaID = models.ForeignKey ('Convocatoria', on_delete=models.PROTECT, null=True)
    convocatoriaID = models.OneToOneField (Convocatoria,on_delete=models.CASCADE, null=True)


    tipoFinanciacion = models.CharField(max_length=500, help_text='¿Qué tipo de financiación aplica para la convocatoria?')
    montoBeneficio = models.CharField(max_length=500, help_text='¿Qué monto tiene la convocatoria?')

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
    )
    OP_AREAS_CONV = (
            ('ocde','OCDE'),
            ('ods','Objetivos ODS'),
            ('na','no aplica'),
    )
    areasConvocatoria = models.CharField(
            max_length=30,
            choices=OP_AREAS_CONV,
            blank=True,
            default='na',
            help_text='¿áreas de la convocatoria?',
    )
    
    #def __id__(self):
    #    return self.id


