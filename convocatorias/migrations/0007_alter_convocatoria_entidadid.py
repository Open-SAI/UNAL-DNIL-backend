# Generated by Django 3.2.5 on 2021-08-10 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0006_convocatoria_entidadid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='entidadID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='convocatorias.entidad', verbose_name='Entidad Otorgante'),
        ),
    ]