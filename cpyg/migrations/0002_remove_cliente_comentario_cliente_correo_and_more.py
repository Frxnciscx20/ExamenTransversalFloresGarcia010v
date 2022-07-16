# Generated by Django 4.0.4 on 2022-07-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpyg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='comentario',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='correo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='direccion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefono'),
        ),
    ]
