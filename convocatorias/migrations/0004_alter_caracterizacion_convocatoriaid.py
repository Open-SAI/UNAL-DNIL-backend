# Generated by Django 3.2.5 on 2021-09-21 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0003_auto_20210921_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracterizacion',
            name='convocatoriaID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='convocatorias.convocatoria'),
        ),
    ]
