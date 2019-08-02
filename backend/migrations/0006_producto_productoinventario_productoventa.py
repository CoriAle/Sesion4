# Generated by Django 2.0.13 on 2019-08-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20190801_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('producido', models.DateTimeField(auto_now_add=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ProductoInventario',
            fields=[
            ],
            options={
                'verbose_name': 'ProductoInventario',
                'proxy': True,
                'verbose_name_plural': 'ProductoInventarios',
                'ordering': ['producido'],
                'indexes': [],
            },
            bases=('backend.producto',),
        ),
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
            ],
            options={
                'verbose_name': 'ProductoVenta',
                'proxy': True,
                'verbose_name_plural': 'ProductoVentas',
                'ordering': ['precio'],
                'indexes': [],
            },
            bases=('backend.producto',),
        ),
    ]
