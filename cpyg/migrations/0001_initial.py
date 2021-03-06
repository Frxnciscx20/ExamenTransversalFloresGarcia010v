# Generated by Django 4.0.4 on 2022-06-30 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Categoria')),
                ('nombreCategoria', models.CharField(max_length=20, verbose_name='Nombre Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='rut')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('comentario', models.CharField(max_length=20, verbose_name='comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='idProducto')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.ImageField(null=True, upload_to='producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpyg.categoria')),
            ],
        ),
    ]
