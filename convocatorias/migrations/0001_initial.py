# Generated by Django 3.2.5 on 2021-08-09 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloConvocatoria', models.CharField(help_text='Título de la Convocatoria', max_length=500)),
                ('descripcion', models.TextField(help_text='Resumen Convocatoria', max_length=2000)),
                ('fechaPublicacion', models.DateField(blank=True, help_text='Fecha Publicación Convocatoria', null=True)),
            ],
            options={
                'verbose_name_plural': 'Registro de Convocatorias',
                'ordering': ['fechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEntidad', models.CharField(help_text='Nombre Entidad Financiadora Convocatoria', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Caracterizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoFinanciacion', models.CharField(help_text='¿Qué tipo de financiación aplica para la convocatoria?', max_length=500)),
                ('montoBeneficio', models.CharField(help_text='¿Qué monto tiene la convocatoria?', max_length=500)),
                ('periodica', models.CharField(blank=True, choices=[('no', 'No'), ('si', 'Sí')], default='n', help_text='¿Esta convocatoria es periódica?', max_length=2)),
                ('periodicidad', models.CharField(blank=True, choices=[('trimestral', 'trimestral'), ('anual', 'anual'), ('bianual', 'bianual'), ('na', 'no aplica')], default='na', help_text='¿qué periodicidad maneja esta convocatoria?', max_length=30)),
                ('ambito', models.CharField(blank=True, choices=[('local', 'local'), ('departamental', 'departamental'), ('nacional', 'nacional'), ('internacional', 'internacional'), ('na', 'no aplica')], default='na', help_text='¿cuál es el ámbito de la convocatoria?', max_length=30)),
                ('areasConvocatoria', models.CharField(blank=True, choices=[('ocde', 'OCDE'), ('ods', 'Objetivos ODS'), ('na', 'no aplica')], default='na', help_text='¿áreas de la convocatoria?', max_length=30)),
                ('convocatoriaID', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='convocatorias.convocatoria')),
            ],
        ),
    ]