# Generated by Django 3.2.5 on 2021-09-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0013_alter_convocatoria_elegibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='elegibilidad',
            field=models.ManyToManyField(related_name='elegibilidad', to='convocatorias.Elegibilidad', verbose_name='Elegibilidad Convocatoria'),
        ),
    ]
