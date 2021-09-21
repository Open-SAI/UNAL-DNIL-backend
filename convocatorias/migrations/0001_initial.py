# Generated by Django 3.2.5 on 2021-09-21 02:51

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreasOCDE',
            fields=[
                ('areaID', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=255, verbose_name='Área')),
            ],
            options={
                'verbose_name_plural': 'Áreas OCDE',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('entidadID', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEntidad', models.CharField(help_text='Nombre Entidad Financiadora Convocatoria', max_length=200)),
                ('paginaWeb', models.URLField(help_text='Página Web de la Entidad', null=True)),
                ('pais', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Directorio de Entidades',
            },
        ),
        migrations.CreateModel(
            name='Icono',
            fields=[
                ('iconoID', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(help_text='Temática convocatoria', max_length=200)),
                ('iconoTem', models.ImageField(null=True, upload_to='icono_tematica')),
            ],
            options={
                'verbose_name_plural': 'Iconografía Etiquetado Convocatoria',
            },
        ),
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('convocatoriaID', models.AutoField(primary_key=True, serialize=False)),
                ('tituloConvocatoria', models.CharField(help_text='Título de la Convocatoria', max_length=500)),
                ('descripcion', models.TextField(help_text='Resumen Convocatoria', max_length=2000)),
                ('fechaPublicacion', models.DateField(help_text='Fecha Publicación Convocatoria', null=True)),
                ('fechaLimitePostulacion', models.DateField(help_text='Fecha Límite Postulación', null=True)),
                ('paginaWebAplicacion', models.URLField(help_text='Página Web para aplicaciones', max_length=500, null=True)),
                ('estadoConvocatoria', models.CharField(choices=[('publicada', 'Publicada'), ('revision', 'En Revisión')], default='revision', help_text='¿Públicar la convocatoria?', max_length=30)),
                ('creacionConvocatoria', models.CharField(choices=[('enviada', 'Enviada'), ('creada', 'Creada')], default='creada', editable=False, help_text='¿Esta convocatoria fué enviada por la Comunidad Académica?', max_length=30)),
                ('vigencia', models.CharField(choices=[('cerrada', 'Cerrada'), ('vigente', 'Vigente')], default='vigente', help_text='¿Se encuentra activa la convocatoria?', max_length=30)),
                ('entidadID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='convocatorias.entidad', verbose_name='Entidad Otorgante')),
                ('iconoID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='convocatorias.icono', verbose_name='Ícono Temático')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Registro de Convocatorias',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('contactoID', models.AutoField(primary_key=True, serialize=False)),
                ('cargoContacto', models.CharField(help_text='Cargo Contacto', max_length=200, null=True)),
                ('nombreContacto', models.CharField(help_text='Nombre Contacto', max_length=200)),
                ('correoContacto', models.EmailField(help_text='Correo Electrónico Contacto', max_length=254)),
                ('telefonoContacto', models.CharField(help_text='Teléfono de Contacto', max_length=200, null=True)),
                ('telefonoContactoAux', models.CharField(blank=True, help_text='Teléfono de Contacto Auxiliar', max_length=200, null=True)),
                ('entidadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocatorias.entidad')),
            ],
            options={
                'verbose_name_plural': 'Contactos Oficiales',
            },
        ),
        migrations.CreateModel(
            name='Caracterizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoFinanciacion', models.CharField(help_text='¿Qué tipo de financiación aplica para la convocatoria?', max_length=500, verbose_name='Tipo de Financiación')),
                ('montoBeneficio', models.CharField(help_text='¿Qué monto tiene la convocatoria?', max_length=500, verbose_name='Monto del Beneficio')),
                ('descripcionBeneficio', models.CharField(help_text='Descripción Beneficio Otorgado', max_length=2000, null=True, verbose_name='Descripción del Beneficio Otorgado')),
                ('periodica', models.CharField(blank=True, choices=[('no', 'No'), ('si', 'Sí')], default='n', help_text='¿Esta convocatoria es periódica?', max_length=2)),
                ('periodicidad', models.CharField(blank=True, choices=[('trimestral', 'trimestral'), ('anual', 'anual'), ('bianual', 'bianual'), ('na', 'no aplica')], default='na', help_text='¿qué periodicidad maneja esta convocatoria?', max_length=30)),
                ('ambito', models.CharField(blank=True, choices=[('local', 'local'), ('departamental', 'departamental'), ('nacional', 'nacional'), ('internacional', 'internacional'), ('na', 'no aplica')], default='na', help_text='¿cuál es el ámbito de la convocatoria?', max_length=30, verbose_name='Ámbito')),
                ('areasConvocatoria', models.CharField(blank=True, choices=[('ciencias_naturales', 'Ciencias Naturales'), ('ingenieria_tecnologia', 'Ingeniería y Tecnología'), ('ciencias_salud', 'Ciencias Médicas y de Salud'), ('ciencias_agricolas', 'Ciencias Agrícolas'), ('ciencias_sociales', 'Ciencias Sociales'), ('humanidades', 'Humanidades'), ('multidisciplinarias', 'Multidisciplinarias')], default='na', help_text='¿áreas de la convocatoria?', max_length=30)),
                ('OCDEareas', models.ManyToManyField(related_name='areas_ocde', to='convocatorias.AreasOCDE', verbose_name='Áreas OCDE')),
                ('convocatoriaID', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='convocatorias.convocatoria')),
            ],
        ),
    ]
