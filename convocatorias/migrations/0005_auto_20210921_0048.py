# Generated by Django 3.2.5 on 2021-09-21 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0004_alter_caracterizacion_convocatoriaid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caracterizacion',
            options={'verbose_name_plural': 'Caracterización'},
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='caracterizacionID',
        ),
    ]
