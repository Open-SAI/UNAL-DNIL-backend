# Generated by Django 3.2.5 on 2021-09-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0010_elegibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocatoria',
            name='Elegibilidad',
            field=models.ManyToManyField(related_name='grupo_elegibilidad', to='convocatorias.Elegibilidad', verbose_name='Elegibilidad Convocatoria'),
        ),
    ]
