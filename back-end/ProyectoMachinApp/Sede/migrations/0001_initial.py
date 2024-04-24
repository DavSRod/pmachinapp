# Generated by Django 5.0.4 on 2024-04-24 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Centro', '0002_rename_descripcion_centro_cen_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede_nombre', models.CharField(max_length=255)),
                ('sede_descripcion', models.TextField()),
                ('sede_direccion', models.CharField(max_length=250)),
                ('sede_fk_centros', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Centro.centro')),
            ],
        ),
    ]