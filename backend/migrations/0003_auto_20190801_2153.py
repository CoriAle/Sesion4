# Generated by Django 2.0.13 on 2019-08-02 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_gato_pez'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gato',
            old_name='peso',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='pez',
            old_name='peso',
            new_name='edad',
        ),
    ]
