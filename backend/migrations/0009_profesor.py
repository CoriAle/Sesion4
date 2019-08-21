# Generated by Django 2.0.13 on 2019-08-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_delete_createdupdatedmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Profesores',
                'verbose_name': 'Profesor',
            },
        ),
    ]