# Generated by Django 5.0.4 on 2024-04-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSitio',
            fields=[
                ('idTipo_sitio', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_sitio', models.CharField(max_length=255)),
            ],
        ),
    ]