# Generated by Django 4.0.6 on 2022-07-07 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=16)),
                ('mes', models.CharField(max_length=2)),
                ('anio', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]