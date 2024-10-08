# Generated by Django 5.1.1 on 2024-09-30 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('contacto', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Subgrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgrupos', to='inventarios.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_barra', models.CharField(max_length=13, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventarios.grupo')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventarios.marca')),
                ('proveedores', models.ManyToManyField(to='inventarios.proveedor')),
                ('subgrupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventarios.subgrupo')),
            ],
        ),
    ]
