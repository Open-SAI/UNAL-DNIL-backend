# Generated by Django 3.2.5 on 2021-09-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0005_auto_20210921_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracterizacion',
            name='areasOCDE',
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='areasOCDE',
            field=models.ManyToManyField(related_name='areas_ocde', to='convocatorias.AreasOCDE', verbose_name='Áreas OCDE'),
        ),
    ]